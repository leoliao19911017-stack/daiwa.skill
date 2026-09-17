# CHANGELOG

## v1.2.0
- 新增 Dad Mode 与 7 个爸爸专用知识模块
- 强化儿童保护优先级，新增 child_protection.md
- safety.md 改为路由器，减少重复
- 新增 8 个高频缺失场景
- 新增 scenario_index.json 与 family_card_schema.json
- 统一家庭执行卡字段
- 新增超范围策略
- eval 改用 rubric/forbidden 语义评估结构并增加压力测试
- 新增 evidence map、书籍/博客 source map
- 新增 .gitattributes、validator、GitHub Action、MIT manifest 字段
- examples/school_age.jsonl 更名为 age_5_6.jsonl
- 清理 SKILL.md 章节编号残留

### 引用消化与修复（迭代）
- 修复：SKILL.md 家庭统一卡字段与 family_alignment.md / family_card_schema.json / validator 同步，并补安全覆盖规则
- 修复：scenario_index.json 补齐 9 个未索引场景（出门、公共场合、屏幕、分离焦虑、分享、睡觉、发脾气、如厕、收玩具）及爸爸/保护类关键词，覆盖率 13/22 → 全量
- 消化 How to Talk（Faber & King，C级）→ 新增 `scripts/cooperation.md`（描述问题/给信息/短词提示）
- 消化 Playful Parenting（Cohen，C级）→ `dad_play.md` 新增游戏化启动工具与禁用条件
- 消化 Serve and Return（哈佛儿童发展中心，B级）→ `dad_talk_reading.md` 命名底层原则
- 消化 Special Time（Listen / Hand in Hand，C级）→ `working_dad_reconnection.md` 补命名协议
- 消化 Good Inside（Becky Kennedy，C级）→ `sibling_conflict.md` 新增"两个真实"与"行为与人分开"句式
- 新增 `examples/dad_mode.jsonl`（3 条 Dad Mode 输出示例），注册进 manifest
- README 恢复安装说明与目录结构
- 引用抽查：2026 ECRQ meta-analysis 经 CrossRef 核实真实存在；其余 DOI/链接可达

## v1.1.0

### 新增
- development_norms.md：这正常吗 / 是否需要观察
- routines.md：固定流程与预防冲突
- caregiver_regulation.md：家长情绪降级
- family_alignment.md：多人照护统一
- myths.md：常见育儿误区
- safety_daily.md：日常安全
- medical_escalation.md：医疗升级
- infant/：0-1岁安抚、睡眠、喂养、游戏、分离

### 更新
- SKILL.md：新增新手父母模式、预防优先、目标拆解、不确定性表达、回答质量自检
- manifest.json：更新知识索引
- principles.md：新增发展校准、流程优先、目标拆解
- eval_cases.jsonl：新增新手父母与0-1岁场景评测

### 保留
- 原有 0-6 岁年龄阶段
- 原有场景库
- 原有话术模块
- 原有 examples
