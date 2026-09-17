# 带娃.skill

> 让任意 Agent 安装后，成为 0-6 岁育儿现场 Copilot。

带娃.skill 优先回答三个问题：**现在怎么做、下一句话怎么说、如果还不配合怎么办**。不是育儿百科，而是家长在现场可以直接照着做的行动指南。

## 它解决什么问题

| 常见提问 | 普通百科回答 | 带娃.skill 回答 |
|---|---|---|
| 孩子不肯刷牙 | 讲刷牙的重要性 | 3 个当下动作 + 1 句可直接说的话 + 不配合时的下一步 |
| 每天早晨都在催 | 讲时间管理理论 | 固定流程 + 视觉清单 + 7 天改善方案 |
| 关电视就哭 | 讲屏幕时间的危害 | 先判断（切换问题/情绪问题）→ 现场处理 → 预防方案 |
| 我快要吼了 | 讲情绪管理 | 先给家长降级动作，再处理孩子 |

## 安装

### Claude Code / Claude Desktop（个人技能目录）

```bash
git clone https://github.com/leoliao19911017-stack/daiwa.skill.git
mkdir -p ~/.claude/skills
cp -r daiwa.skill ~/.claude/skills/daiwa
```

Windows（PowerShell）：

```powershell
git clone https://github.com/leoliao19911017-stack/daiwa.skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse -Force daiwa.skill "$env:USERPROFILE\.claude\skills\daiwa"
```

重启会话后即可生效。技能触发词：带娃、育儿、孩子哭闹、不肯吃饭、不肯睡觉、怎么跟孩子说 等。

### 其他 Agent

任意支持「技能/知识包」的 Agent，把 `SKILL.md` 设为入口（entrypoint），按需加载 `knowledge/` 下的知识文件即可，零依赖、无需联网。

## 目录结构

```
daiwa.skill/
├── SKILL.md              # 入口：角色、决策链、默认输出格式、行为准则
├── manifest.json         # 技能清单与知识索引
├── CHANGELOG.md          # 版本记录
├── knowledge/            # 知识库
│   ├── age_stages.md         # 0-6 岁年龄能力校准
│   ├── development_norms.md  # 「这正常吗」发展参照
│   ├── principles.md         # 通用处理原则
│   ├── routines.md           # 固定流程与预防冲突
│   ├── scenarios/            # 14 个高频场景（吃饭、睡觉、刷牙、如厕、打人、公共场合哭闹…）
│   ├── scripts/              # 现场话术（边界、选择、情绪、鼓励）
│   ├── infant/               # 0-1 岁专项（喂养、安抚、睡眠、游戏、分离）
│   ├── caregiver_regulation.md # 家长情绪降级
│   ├── family_alignment.md   # 多人照护统一口径
│   ├── myths.md              # 常见育儿误区
│   ├── safety_daily.md       # 日常安全预防
│   ├── medical_escalation.md # 医疗/急救升级
│   └── safety.md             # 安全风险升级处理
├── examples/             # 输出风格示例（toddler / preschool / school_age）
└── evals/                # 评测用例（eval_cases.jsonl）
```

## 核心决策链

```
安全风险 → 年龄阶段 → 生理/情绪状态 → 具体场景 → 行为功能
→ 家长目标 → 最小可执行动作 → 现场话术 → 下一层处理 → 长期改善
```

## 设计原则

- **先看年龄，再看状态，再看行为** —— 不脱离发展阶段谈对错
- **接纳情绪，但边界不因哭闹自动改变**
- **不贴标签** —— 不把孩子称为懒、坏、熊、故意作对
- **可执行优先** —— 每个回答都有能直接说出口的话
- **不说教** —— 一次只给 1-3 个可持续方法
- **安全兜底** —— 医疗/急救情境自动升级处理

## 适用范围

- 0-6 岁（0-72 个月）
- 覆盖：日常流程、吃饭、睡觉、屏幕时间、哭闹、边界、幼儿园、社交、家庭协作、安全

## License

[MIT](LICENSE)
