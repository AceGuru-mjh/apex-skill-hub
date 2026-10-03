#!/usr/bin/env python3
"""Apex Skill Hub 注册表校验器（CI 用，零依赖）。

校验规则（任何一条失败即退出码 1）：
 1. index.json 可解析、schema 正确、count 与 skills[] 实际条数一致；
 2. 每个条目字段齐全（id/name/version/description/category/tags/scope/author/file）；
 3. id 全局唯一、格式合法（小写字母数字连字符）；
 4. file 指向的 manifest 文件存在、可解析、schema=apex-skill-v1；
 5. manifest 的 id/name/version/category/scope 与索引条目一致（防索引漂移）；
 6. category 属于宿主 App SkillCategory 24 域词表；
 7. scope ∈ {agent, coding, all}；bundled 恒 false（仓库技能 ≠ 内置）；
 8. promptInjection 非空且 ≥ 800 字符（正文质量下限）；
 9. 索引与单文件体积在 App 下载上限内（索引 ≤ 2MB、单技能 ≤ 2MB）；
10. 全仓无凭据泄漏（ghp_/github_pat_/AKIA 指纹扫描）。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.json")
SKILLS_DIR = os.path.join(ROOT, "skills")

LEGAL_CATEGORIES = {
    "career", "knowledge", "lifestyle", "emotional", "social", "data",
    "business", "finance", "tech", "language", "health", "fitness",
    "education", "parenting", "home", "travel", "creative", "writing",
    "entertainment", "productivity", "communication", "safety", "digital",
    "coding",
}
LEGAL_SCOPES = {"agent", "coding", "all"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,48}$")
SECRET_RE = re.compile(r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16})")

errors = []


def err(msg: str) -> None:
    errors.append(msg)


def main() -> int:
    # ── index.json ──
    try:
        with open(INDEX, encoding="utf-8") as fp:
            index = json.load(fp)
    except Exception as e:  # noqa: BLE001
        print(f"FATAL: index.json 不可解析: {e}")
        return 1

    if index.get("schema") != "apex-skill-hub-v1":
        err(f"schema 应为 apex-skill-hub-v1，实际 {index.get('schema')!r}")
    entries = index.get("skills")
    if not isinstance(entries, list) or not entries:
        err("skills[] 缺失或为空")
        print("\n".join(f"ERROR: {e}" for e in errors))
        return 1
    if index.get("count") != len(entries):
        err(f"count={index.get('count')} 与 skills[] 实际 {len(entries)} 不一致")

    index_size = os.path.getsize(INDEX)
    if index_size > 2 * 1024 * 1024:
        err(f"index.json {index_size}B 超过 App 2MB 拉取上限")

    seen_ids = set()
    for ent in entries:
        eid = ent.get("id", "<missing>")
        for field in ("id", "name", "version", "description", "category",
                      "tags", "scope", "author", "file"):
            if field not in ent:
                err(f"[{eid}] 索引条目缺字段 {field}")
        if not ID_RE.match(str(eid)):
            err(f"[{eid}] id 格式非法")
        if eid in seen_ids:
            err(f"[{eid}] id 重复")
        seen_ids.add(eid)
        if ent.get("category") not in LEGAL_CATEGORIES:
            err(f"[{eid}] category 非法: {ent.get('category')!r}")
        if ent.get("scope") not in LEGAL_SCOPES:
            err(f"[{eid}] scope 非法: {ent.get('scope')!r}")

        # ── manifest 一致性 ──
        rel = ent.get("file", "")
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            err(f"[{eid}] file 指向的文件不存在: {rel}")
            continue
        try:
            with open(path, encoding="utf-8") as fp:
                man = json.load(fp)
        except Exception as e:  # noqa: BLE001
            err(f"[{eid}] manifest 不可解析: {e}")
            continue
        if man.get("schema") != "apex-skill-v1":
            err(f"[{eid}] manifest schema 应为 apex-skill-v1")
        for field in ("id", "name", "version", "category", "scope"):
            if man.get(field) != ent.get(field):
                err(f"[{eid}] manifest.{field}={man.get(field)!r} 与索引 {ent.get(field)!r} 不一致")
        if man.get("bundled") is not False:
            err(f"[{eid}] 仓库技能 bundled 必须为 false")
        pi = man.get("promptInjection", "")
        if not isinstance(pi, str) or len(pi) < 800:
            err(f"[{eid}] promptInjection 过短（{len(pi)} < 800）")
        if os.path.getsize(path) > 2 * 1024 * 1024:
            err(f"[{eid}] manifest 超过 App 2MB 下载上限")

    # ── 反向检查：skills/ 下无游离文件（未被索引收录）──
    for name in sorted(os.listdir(SKILLS_DIR)):
        if not name.endswith(".json"):
            continue
        sid = name[:-5]
        if sid not in seen_ids:
            err(f"skills/{name} 未被 index.json 收录（游离文件）")

    # ── 凭据泄漏扫描 ──
    for dirpath, _dirs, files in os.walk(ROOT):
        if ".git" in dirpath:
            continue
        for name in files:
            if not name.endswith((".json", ".md", ".py", ".yml", ".yaml")):
                continue
            p = os.path.join(dirpath, name)
            try:
                with open(p, encoding="utf-8") as fp:
                    if SECRET_RE.search(fp.read()):
                        err(f"疑似凭据泄漏: {p}")
            except OSError:
                pass

    if errors:
        print(f"\n校验失败，共 {len(errors)} 处：")
        for e in errors:
            print(f"  ERROR: {e}")
        return 1

    cats: dict = {}
    for ent in entries:
        cats.setdefault(ent["category"], 0)
        cats[ent["category"]] += 1
    print(f"OK: {len(entries)} 个技能，{len(cats)} 个域，索引 {index_size}B")
    for c in sorted(cats):
        print(f"  {c}: {cats[c]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
