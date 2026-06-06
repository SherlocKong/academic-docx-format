# Academic DOCX Format

一个面向学术论文、毕业论文、期刊投稿稿件和补充材料的 DOCX 格式审查与安全修改 Agent Skill。

它不替代通用 `docx` skill，也不负责从零生成普通 Word 文档。它负责在调用 DOCX 工具前后建立一套稳定、可审计、防误伤的工作流：

> 环境预检 → 项目接手 → 只读勘测 → 用户审批 → 修改计划 → 时间戳副本 → 定点修改 → 三层回归验证 → 项目记录更新

## 适用场景

- 严格审查学术 DOCX 的字体、字号、行距、段距和页面设置
- 检查公式、变量、单位、上下标和公式编号
- 检查表格、图片、caption、交叉引用和参考文献格式
- 对照期刊、学校规范或模板生成格式审查报告
- 在不破坏无关内容和结构的前提下执行定点格式修改
- 检查用户或 Agent 修改后是否产生格式回归
- 联合检查最终 DOCX、PDF、匿名元数据和投稿目录

## 核心原则

1. 修改前必须完成只读勘测并形成 Markdown 报告。
2. 用户审批后，必须先生成明确执行计划并消除所有模糊项。
3. 永不直接覆盖输入 DOCX；主要修改必须创建带时间戳的新副本。
4. 只修改批准范围，禁止顺手清理无关问题。
5. 所有 Word 操作必须基于已安装的 `docx` skill。
6. 修改后必须通过内容、OOXML/package 和视觉渲染三层验证。
7. `AGENTS.md` 只作为精简项目索引；完整格式任务记录存放在独立的 `*_format_audit.md`。

## 工作模式

- `audit-only`：只读严格审查并生成格式总览报告
- `targeted-format-repair`：基于已批准报告执行定点修改
- `format-regression-check`：检查手动或自动修改造成的格式回归
- `final-package-check`：检查 DOCX、PDF、元数据和投稿目录
- `project-bootstrap`：检查环境并建立精简的 `AGENTS.md` 项目索引

## 安装

将仓库中的 [`academic-docx-format`](academic-docx-format/) 目录复制到 Agent 的 skills 目录。

以 Codex 默认目录为例：

```bash
git clone https://github.com/SherlocKong/academic-docx-format.git
cp -R academic-docx-format/academic-docx-format ~/.codex/skills/
```

安装后建议运行：

```bash
python3 ~/.codex/skills/academic-docx-format/scripts/preflight.py --json
```

若本地依赖冲突，可为本 skill 创建独立虚拟环境。详细步骤见：

[`references/environment-setup.md`](academic-docx-format/references/environment-setup.md)

## 使用示例

```text
使用 $academic-docx-format 严格审查这份学术 DOCX 的公式和上下标格式。
本轮只勘测、定位并生成报告，不修改 Word。
```

```text
使用 $academic-docx-format，根据我已批准的格式勘测报告生成修改计划。
不要覆盖原文件，不要修改批准范围以外的内容。
```

## 目录结构

```text
academic-docx-format/
├── SKILL.md
├── agents/
├── assets/
├── references/
└── scripts/
```

- `SKILL.md`：核心门禁、模式路由和操作顺序
- `references/`：审查、修复、科研格式、环境和验证规范
- `assets/`：`AGENTS.md`、格式总览报告和定点勘测报告模板
- `scripts/`：环境预检、时间戳副本和只读 DOCX 盘点工具

## 隐私与安全

仓库不包含论文示例、作者信息、项目数据、DOCX/PDF 文件、执行日志或虚拟环境。

辅助脚本可能在运行时向终端输出本机文件路径和哈希值。公开分享执行日志前，请自行检查并脱敏。

## 许可证

本项目采用 [MIT License](LICENSE) 开源。
