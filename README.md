# Apex Skill Hub

**Apex Agent 官方技能仓库** —— 精选生活/通用型 Agent 技能，按需从应用内「市场 → Skills → 官方仓库」直接安装。

[English](#english) below.

## 仓库结构

```
index.json            # 注册表（apex-skill-hub-v1）：全部技能的元数据索引
skills/<id>.json      # 每个技能一份完整 manifest（apex-skill-v1 格式）
```

## index.json 格式

```json
{
  "schema": "apex-skill-hub-v1",
  "count": 62,
  "skills": [
    {
      "id": "cooking-master",
      "name": "家常菜大师",
      "version": "1.0.0",
      "description": "……",
      "category": "AGENT",
      "tags": ["cooking"],
      "scope": "agent",
      "author": "Apex",
      "file": "skills/cooking-master.json"
    }
  ]
}
```

- `scope`：`agent`（Agent 工位）/ `coding`（Coding 工位）/ `all`（双工位）
- `file`：相对本仓库根目录的 manifest 路径，App 通过
  `https://raw.githubusercontent.com/AceGuru-mjh/apex-skill-hub/main/<file>` 拉取

## 技能 manifest 格式（apex-skill-v1）

与 App 内置技能完全同构：

```json
{
  "schema": "apex-skill-v1",
  "id": "cooking-master",
  "name": "家常菜大师",
  "version": "1.0.0",
  "description": "一句话描述（会进入系统提示词的技能目录）",
  "author": "Apex",
  "license": "MIT",
  "scope": "agent",
  "tools": [],
  "promptInjection": "【方法论全文】……"
}
```

`promptInjection` 为渐进披露正文：安装且启用后，模型经 `skill_activate` 或 `/skill:<id>` 装备时注入系统提示词。

## 设计原则（学习 opencode）

1. **注册表 + 单文件分发**：`index.json` 只放元数据（小体积、可分页过滤），技能正文按需单文件拉取；
2. **市场直装**：App 市场浏览本仓库 → 一键安装 → 与本地技能同权管理（启用/禁用/卸载）；
3. **内置只保留少量核心**：APK 内只打包 13 个强技能（8 coding + 3 agent + 2 通用），其余全部收敛到本仓库，保持安装包轻量、技能可持续更新（改仓库即生效，无需发版）。

## 收录约定

- 新技能提 PR：`skills/<id>.json` + `index.json` 增加条目
- `id` 规则：`[A-Za-z0-9_.-]`，禁止 `..` / 前导点 / 路径分隔符
- `description` ≤ 72 字符首句会进入技能目录（越精炼越利于模型选择）

---

# English

**Official skill repository for Apex Agent** — curated life & general-purpose Agent skills, installed on demand from the in-app Market (Market → Skills → Official Hub).

Structure: `index.json` is the metadata registry (`apex-skill-hub-v1`); each skill body lives in `skills/<id>.json` using the `apex-skill-v1` manifest format. The app fetches the index from `raw.githubusercontent.com`, lists entries per market tier (`scope`: agent/coding/all), and downloads a single manifest file on install — the same distribution pattern used by opencode's remote skill registries.

Contributions welcome: add `skills/<id>.json` plus an `index.json` entry in a PR.
