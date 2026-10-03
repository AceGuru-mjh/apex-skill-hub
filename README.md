# Apex Skill Hub

**Apex Agent 官方技能仓库** —— 67 个精选专业/效率型技能、14 个域，从应用内「市场 → Skills → 官方仓库」按需安装。

[English](#english) below.

## v2 重组说明（2026-10）

本仓库完成了一次全面重组：

1. **生活类技能全部退役**（原 62 个中删除 45 个：烹饪/美妆/情感/健身/旅行/宠物等）；
2. **保留 17 个专业通用技能**并归入宿主 App 的 24 域分类体系（原 `AGENT`/`PRODUCTIVITY` 旧词表废弃）；
3. **新增 50 个技能**，改名 + 中文重写优化 + 分类，来源三路：
   - [anthropics/skills](https://github.com/anthropics/skills)（官方技能库）：文档四件套 / MCP 构建 / 技能创作 / 前端设计 / E2E 测试等 12 个；
   - [obra/superpowers](https://github.com/obra/superpowers)（MIT）：TDD / 完工验证 / 计划 / 评审双向 / worktree / 并行调度等 8 个；
   - **Android-Guru-Agent 内置迁移**（改名优化迁入，APK 不再打包）：API 契约 / 根因调试 / SQL 调优 / A/B 实验 / 商业模式 / 面试备战 / 提示词工程等 30 个。

## 仓库结构

```
index.json                 # 注册表（apex-skill-hub-v1）：全部技能的元数据索引
skills/<id>.json           # 每个技能一份完整 manifest（apex-skill-v1 格式）
scripts/validate.py        # 注册表校验器（CI 用，零依赖）
.github/workflows/validate.yml
```

## 技能矩阵（67 个 · 14 域）

| 域 | 数量 | 代表技能 |
|---|---|---|
| coding 编程开发 | 18 | api-contract-design、root-cause-debugging、tdd-workflow、mcp-server-builder、sql-query-tuning、regex-forge |
| career 职场进阶 | 9 | resume-crafter、interview-coach、behavioral-interview-star、okr-alignment-craft |
| productivity 效率工具 | 9 | time-gtd、brainstorm-partner、verification-before-done、execution-planner、pdf/docx/xlsx/pptx-toolkit |
| data 数据分析 | 7 | ab-test-verdict、cohort-deep-dive、pandas-data-wrangling、metrics-tree-design |
| business 商业思维 | 6 | business-model-craft、unit-economics-lab、pricing-strategy-lab、financial-statement-reader |
| language 语言学习 | 4 | translation-master、business-english-polish、academic-english-editor |
| writing 专业写作 | 3 | writing-coach、prd-architect 同源的 tech-writing 迁移、brand-voice-guardian |
| safety 安全应急 | 2 | privacy-guard、phishing-defense-shield |
| education 学习方法 | 2 | exam-tutor、study-methods |
| communication 沟通表达 | 2 | public-speaking、internal-comms-writer |
| tech 数码科技 | 2 | prompt-craft-toolbox、ai-tools-playbook |
| finance 财务理财 | 1 | finance-literacy |
| knowledge 百科知识 | 1 | legal-consult |
| creative 创意写作 | 1 | visual-canvas-designer |

`scope` 分布：`coding` 24 / `agent` 34 / `all` 9 —— 市场按 Agent / Coding 工位分级过滤。

## index.json 格式

```json
{
  "schema": "apex-skill-hub-v1",
  "count": 67,
  "skills": [
    {
      "id": "root-cause-debugging",
      "name": "根因定位调试法",
      "version": "1.0.0",
      "description": "……",
      "category": "coding",
      "tags": ["调试", "根因", "debugging"],
      "scope": "coding",
      "author": "Apex",
      "file": "skills/root-cause-debugging.json"
    }
  ]
}
```

- `category`：合法取值 = 宿主 App `SkillCategory` 24 域小写连字符 key（本仓当前用到 14 个）；
- `scope`：`agent`（Agent 工位）/ `coding`（Coding 工位）/ `all`（双工位）；
- `file`：相对本仓库根目录的 manifest 路径，App 通过
  `https://raw.githubusercontent.com/AceGuru-mjh/apex-skill-hub/main/<file>` 拉取。

## 技能 manifest 格式（apex-skill-v1）

```json
{
  "schema": "apex-skill-v1",
  "id": "root-cause-debugging",
  "name": "根因定位调试法",
  "version": "1.0.0",
  "description": "一句话描述（会进入系统提示词的技能目录）",
  "author": "Apex",
  "license": "MIT",
  "bundled": false,
  "promptInjection": "【方法论全文】……"
}
```

`promptInjection` 为渐进披露正文（1200-2600 汉字，三段式：触发场景 / 方法论 / 输出格式约定）：安装且启用后，模型经 `skill_activate` 或 `/skill:<id>` 装备时注入系统提示词。

## CI 校验（GitHub Actions）

每次 push / PR 自动执行 `.github/workflows/validate.yml`：

1. `scripts/validate.py`：索引与全量 manifest 交叉校验（schema / 字段齐全 / id 唯一 / 索引↔正文一致 / category 合法 / bundled 恒 false / promptInjection 质量下限 / 2MB 体积红线 / 凭据泄漏扫描）；
2. main 分支推送后：逐条 smoke test 全部技能的 raw.githubusercontent.com 可达性（App 实际下载路径 200 检查）。

## 收录约定

- 新技能提 PR：`skills/<id>.json` + `index.json` 增加条目，CI 全绿即合并；
- `id` 规则：`^[a-z0-9][a-z0-9-]{1,48}$`（小写字母数字连字符）；
- `description` 60-100 字高信息密度（首句进入技能目录，越精炼越利于模型选择）；
- **不收生活/娱乐类技能**（本仓库定位：专业 + 生产力）。

---

# English

**Official skill repository for Apex Agent** — 67 curated professional & productivity skills across 14 domains, installed on demand from the in-app Market (Market → Skills → Official Hub).

**v2 reorg (Oct 2026)**: all 45 lifestyle skills retired; 17 professional keepers recategorized into the host app's 24-domain taxonomy; 50 new skills added — renamed, rewritten in Chinese and optimized from three sources: [anthropics/skills](https://github.com/anthropics/skills) (12), [obra/superpowers](https://github.com/obra/superpowers) (MIT, 8), and the Android-Guru-Agent bundled set (30, migrated out of the APK so the market downloads them on demand).

Structure: `index.json` is the metadata registry (`apex-skill-hub-v1`); each skill body lives in `skills/<id>.json` (`apex-skill-v1` manifest). The app fetches the index from `raw.githubusercontent.com`, filters by market tier (`scope`: agent/coding/all), and downloads a single manifest per install. CI (GitHub Actions) cross-validates index ↔ manifests, enforces category/scope vocabularies, size limits and secret-leak scanning, plus a raw-URL reachability smoke test on `main`.

Contributions: add `skills/<id>.json` plus an `index.json` entry in a PR. Professional & productivity skills only.
