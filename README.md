# Apex Skill Hub

**Apex Agent 官方技能仓库** —— 132 个精选专业/效率型技能、14 个域（v3.1 新增 15 个逆向工程技能，补齐逆向领域空白），从应用内「市场 → Skills → 官方仓库」按需安装；配合宿主 v1.4.6+ 技能目录热加载，安装即生效免重启。

[English](#english) below.

## v3.1 逆向工程扩容说明（2026-10）

1. **新增 15 个原创逆向工程方法论技能**（此前逆向领域为空白），全部原创中文三段式结构（触发场景 → 方法论维度 → 输出格式约定，密度双口径自检达标），与逆向工作流闭环对应：
   - **入口侦察**（4）：APK 逆向侦察（指纹/加固判定/攻击面测绘）、字符串资源侦察（特征正则集/变形还原）、加固脱壳恢复（脱壳四路/修复四查）、恶意样本分诊（安全域）；
   - **核心分析**（5）：Smali 改写工艺、Native SO 逆向（JNI 桥/算法还原）、Frida Hook 工艺、二进制静态分析、动态行为追踪；
   - **专项深化**（4）：反检测对抗（检测面全景/绕过四级）、协议逆向工艺、加密常量识别（魔数指纹库/国密）、漏洞模式审计；
   - **产出交付**（2）：补丁改写工艺（smali/ARM 两层落刀）、逆向报告写作（结论先行/证据链规范）；
2. 技能间互相引用形成工作流闭环：侦察 → 脱壳 → so/协议分析 → 对抗反检测 → 补丁验证 → 报告交付；
3. 总数 117 → **132**（coding 46→60，safety 3→4）；新技能 scope 以 coding 为主，恶意样本分诊等 3 个为 all；
4. 配套 apex-mcp-hub v2.3.0 的 reverse-engineering 类（15 台 MCP）——技能教「怎么想」，MCP 给「用什么工具」。

## v3 扩容说明（2026-10）

1. **新增 50 个「编码与完成复杂任务」技能**，全部原创中文方法论（三段式结构：触发场景 → 方法论维度 → 输出格式约定，密度双口径自检达标），四路主题：
   - **架构与分布式**（12）：系统设计蓝图、微服务拆分、事件驱动、分布式一致性、缓存策略、消息队列、API 版本演进、错误处理与重试、并发模型、数据库建模、NoSQL 建模、实时系统；
   - **语言与代码工艺**（13）：TypeScript 类型、Python 性能、Go 并发、Rust 所有权、JVM 调优、React 性能、状态管理、CSS 布局、Web 无障碍、代码库阅读、绞杀迁移、依赖升级、破坏性变更灰度；
   - **DevOps 与质量工程**（13）：容器化、K8s 排障、Terraform IaC、流水线、单仓多包、Gradle 调优、可观测埋点、结构化日志、SRE 金信号、SLI/SLO、压测、混沌工程、安全加固；
   - **复杂任务执行与协作**（12）：技术方案、ADR、估算、事故复盘、值班手册、多步研究综合、代理编排、Git 高级操作、Linux CLI、Shell 安全脚本、SQL 窗口函数、GraphQL 设计。
2. 总数 67 → **117**；`scope` 分布 coding 67 / agent 35 / all 15；
3. 配套宿主 Android-Guru-Agent v1.4.6：MCP 本地运行容错（看门狗 + 指数退避自动重连）+ 技能目录热加载（文件指纹监听，市场外变化免重启生效）。

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

## 技能矩阵（132 个 · 14 域）

| 域 | 数量 | 代表技能 |
|---|---|---|
| coding 编程开发 | 60 | api-contract-design、root-cause-debugging、tdd-workflow、system-design-blueprint、apk-re-recon、native-so-re、frida-hook-craft、protocol-re-craft、unpack-dex-recovery、crypto-const-recognize、vuln-pattern-audit |
| productivity 效率工具 | 15 | time-gtd、verification-before-done、execution-planner、technical-spec-writing、agent-orchestration-playbook、pdf/docx/xlsx/pptx-toolkit |
| tech 数码科技 | 15 | kubernetes-troubleshooting、docker-craft-containerization、terraform-iac-craft、sre-golden-signals、gradle-build-tuning、linux-cli-mastery、prompt-craft-toolbox |
| career 职场进阶 | 9 | resume-crafter、interview-coach、behavioral-interview-star、okr-alignment-craft |
| data 数据分析 | 8 | ab-test-verdict、cohort-deep-dive、pandas-data-wrangling、sql-window-functions、metrics-tree-design |
| business 商业思维 | 6 | business-model-craft、unit-economics-lab、pricing-strategy-lab、financial-statement-reader |
| language 语言学习 | 4 | translation-master、business-english-polish、academic-english-editor |
| safety 安全应急 | 4 | privacy-guard、phishing-defense-shield、security-hardening-review、malware-triage |
| education 学习方法 | 2 | exam-tutor、study-methods |
| communication 沟通表达 | 2 | public-speaking、internal-comms-writer |
| knowledge 百科知识 | 2 | legal-consult、multi-step-research-synthesis |
| finance 财务理财 | 1 | finance-literacy |
| writing 专业写作 | 3 | writing-coach、brand-voice-guardian、video-script-writer |
| creative 创意写作 | 1 | visual-canvas-designer |

`scope` 分布：`coding` 79 / `agent` 35 / `all` 18 —— 市场按 Agent / Coding 工位分级过滤。


## index.json 格式

```json
{
  "schema": "apex-skill-hub-v1",
  "count": 132,
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

**Official skill repository for Apex Agent** — 132 curated professional skills across 14 domains (v3.1: +15 original reverse-engineering skills — APK recon, smali editing, native SO analysis, Frida hooking, anti-re bypass, protocol RE, crypto constant recognition, unpacking, binary static/dynamic analysis, vulnerability pattern audit, malware triage, patching, and RE report writing; v3: +50 coding & complex-task skills), installed on demand from the in-app Market. Works with host v1.4.6+ hot-reload: install takes effect without restart. Pairs with apex-mcp-hub v2.3's `reverse-engineering` MCP category — skills teach the methodology, MCPs provide the tools.

**v2 reorg (Oct 2026)**: all 45 lifestyle skills retired; 17 professional keepers recategorized into the host app's 24-domain taxonomy; 50 new skills added — renamed, rewritten in Chinese and optimized from three sources: [anthropics/skills](https://github.com/anthropics/skills) (12), [obra/superpowers](https://github.com/obra/superpowers) (MIT, 8), and the Android-Guru-Agent bundled set (30, migrated out of the APK so the market downloads them on demand).

Structure: `index.json` is the metadata registry (`apex-skill-hub-v1`); each skill body lives in `skills/<id>.json` (`apex-skill-v1` manifest). The app fetches the index from `raw.githubusercontent.com`, filters by market tier (`scope`: agent/coding/all), and downloads a single manifest per install. CI (GitHub Actions) cross-validates index ↔ manifests, enforces category/scope vocabularies, size limits and secret-leak scanning, plus a raw-URL reachability smoke test on `main`.

Contributions: add `skills/<id>.json` plus an `index.json` entry in a PR. Professional & productivity skills only.
