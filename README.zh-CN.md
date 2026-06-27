# resource-radar-public

[English](README.md) | 简体中文

一个公开安全、Agent 中立、工具中立的资源雷达起步模板：用于收集公开资源、规范化元数据、评估质量信号、跟踪生命周期，并生成可审查报告，而不暴露私有候选池。

这个仓库是私有资源雷达工作流的公开模板和示例。它刻意保持通用：可以服务 GitHub 项目、技术文档、研究资源、书签目录、Agent Skills、学习资料，以及其它有价值的公开资源。

## 从这里开始

| 你想做什么 | 入口 |
| --- | --- |
| 查看生成的示例报告 | [`outputs/demo-report.md`](outputs/demo-report.md) |
| 查看示例资源记录 | [`data/demo/`](data/demo) |
| 理解评分和生命周期策略 | [`policies/`](policies) |
| 本地运行示例 | `python -B scripts/run_demo.py --check` |
| 理解整套系统 | [`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md) |

## 系统位置

本仓库是
[`open-resource-governance`](https://github.com/yiheng8023/open-resource-governance)
生态中的一个公开资源发现链路。

```text
open-resource-governance
  -> 负责全局地图、公开/私有边界和发布闸门

resource-radar-public
  -> 提供公开安全资源结构、评分/生命周期示例、示例报告和验证

私有 resource-radar
  -> 可以保存真实候选池、快照、账号相关自动化和审查笔记

research-bookmarks-public
  -> 可以为后续发现提供公开来源种子

agent-skills-curated
  -> 只在单独准入后消费已审查 Skill 候选
```

如果你只需要资源雷达模式，从本仓开始即可。若要理解整个仓库家族关系，请看总仓拓扑：
[`open-resource-governance/docs/system-topology.md`](https://github.com/yiheng8023/open-resource-governance/blob/main/docs/system-topology.md)。

## 它解决什么问题？

好资源如果没有结构化治理，很快会变成噪音：

- 链接散落在 stars、书签、笔记、聊天记录和本地文件里；
- star 数被误当成质量；
- 许可证、新鲜度、维护状态、可信度没有记录；
- 私人偏好和公开资源混在一起；
- 下游系统分不清它是工具、参考资料、Skill 候选、学习资源、书签种子，还是应该拒绝的资源。

`resource-radar-public` 提供一个小而可复现的模式：

```text
公开候选资源
-> 规范化记录
-> 评分与生命周期策略
-> 确定性报告
-> 审查闸门
-> 面向下游的专用结果
```

## 本仓库提供什么

- 公开安全的资源记录结构。
- 仅使用公开、官方或通用示例的资源记录。
- 与书签链路对齐的通用领域分类。
- 可配置的评分和生命周期策略。
- 确定性的示例报告生成器。
- 用于检查数据结构、生成产物和明显私有数据误入的验证脚本。
- 公私边界、来源政策、自动化边界和下游关系文档。

## 本仓库不负责什么

本仓库不负责：

- 存储私有候选池；
- 大规模抓取网页或 GitHub；
- 给外部账号加星、取消星标、打标签或做外部变更；
- 判断某个资源一定可以商用；
- 安装工具、Agent Skills、插件、MCP server 或浏览器书签；
- 替代法律、安全、许可证或维护者审查。

## 与私有雷达的关系

配对的私有仓是 `resource-radar`。

```text
resource-radar
  私有来源、真实候选池、快照、审查笔记、账号相关自动化

resource-radar-public
  公开资源结构、示例记录、评分/生命周期示例、报告、验证
```

私有自动化可以消费这个公开模板，但公开用户不需要访问私有仓库，也能理解并运行示例。

## Agent 中立与工具中立

本仓库不是 Codex 专属、Claude 专属，也不是某个 Agent 专属。Agent Skills 只是可能的下游方向之一。其它方向可以是书签、软件工具、学习资源、参考目录、数据集、文档来源，或未来的项目专用结果。

## 快速开始

```bash
git clone https://github.com/yiheng8023/resource-radar-public.git
cd resource-radar-public
python -B scripts/run_demo.py --check
python -B scripts/verify.py
```

重新生成示例报告：

```bash
python -B scripts/run_demo.py
```

生成产物：

- [`outputs/demo-report.md`](outputs/demo-report.md)
- [`outputs/demo-report.json`](outputs/demo-report.json)

## 目录结构

```text
data/demo/              公开安全示例资源记录
docs/                   设计、边界、来源政策、关系图
outputs/                确定性生成的示例报告
policies/               评分与生命周期策略示例
policies/domain-taxonomy.json
                        通用公开领域分类
schemas/                资源记录结构
scripts/                示例生成与验证脚本
```

## 资源生命周期

示例使用保守的状态模型：

| 状态 | 含义 |
| --- | --- |
| `candidate` | 值得跟踪，但尚未审查进入下游 |
| `watch` | 有潜力，但需要补充新鲜度、许可证或质量证据 |
| `reference` | 适合作为公开参考或基线 |
| `adopt` | 足够强，可考虑进入下游方向 |
| `reject` | 不应晋级；仅在证据有价值时保留 |
| `retired` | 曾经有用，但现在不再推荐 |

状态不是最终裁决，只是审查辅助。

## 质量信号

公开示例刻意把 star 视为可选弱信号。评分更偏向容易审计的证据：

- 官方或权威来源；
- 文档清晰；
- 维护活跃或信息新鲜；
- 相关场景下有测试、release 或质量流程；
- 许可证清晰；
- 下游适配度；
- 私有数据和账号耦合风险低。

## 下游方向

一个资源可以映射到多个方向：

- `tool`
- `reference`
- `learning`
- `bookmark_seed`
- `skill_candidate`
- `dataset`
- `workflow`
- `standard`

这样不会把所有好资源都硬塞进 Agent Skill 仓库。

## 验证方式

公开验证会检查：

- 必需文件存在；
- 资源 ID 唯一；
- 示例记录符合公开安全结构；
- 生成报告确定且已更新；
- 公开文件不包含明显私有字段；
- URL 是 HTTPS 公开引用；
- 策略文件符合预期结构版本。

## 安全边界

这里只能放公开安全数据。不要加入私有书签、凭据、token、本地路径、账号状态、个人偏好、私有审查笔记、浏览器/session 数据或私有候选列表。

## 许可证

MIT。见 [`LICENSE`](LICENSE)。
