# 带娃.skill v1.2.0

> 让任意 Agent 安装后，成为 0-6 岁育儿现场 Copilot，**特别优化爸爸带娃与职场爸爸场景**。

安装到 Agent 后，优先回答：
- 现在怎么做？
- 下一句话怎么说？
- 如果还不配合怎么办？

不是育儿百科，而是家长在现场可以直接照着做的行动指南。

| 常见提问 | 普通百科回答 | 带娃.skill 回答 |
|---|---|---|
| 孩子不肯刷牙 | 讲刷牙的重要性 | 3 个当下动作 + 1 句可直接说的话 + 不配合时的下一步 |
| 每天早晨都在催 | 讲时间管理理论 | 固定流程 + 视觉清单 + 7 天改善方案 |
| 我下班回家孩子只要妈妈 | 讲父亲角色重要性 | 阶段性偏好判断 + 不强迫亲近 + 固定照护锚点方案 |

## v1.2 新增
- **Dad Mode**：全职爸爸回归职场、下班重连、有限时间连接、幼儿园参与、爸爸内疚与修复（`knowledge/fatherhood/`）
- **儿童保护优先级**：第三方体罚/虐待/性安全风险最高优先路由（`knowledge/child_protection.md`）
- 新增 8 个高频场景：说谎、怕黑/噩梦、二胎同胞、被欺负、死亡悲伤、身体隐私、语言担忧、能力倒退
- 场景中文索引（`knowledge/scenario_index.json`）、家庭执行卡 schema
- 超龄策略（>6 岁）、证据分级（A 研究 / B 机构 / C 实践框架）
- 语义 rubric 评测 + 压力测试（含恶意请求、中英混合），`tools/validate.py` + GitHub Action

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

重启会话后生效。触发词：带娃、育儿、孩子哭闹、不肯吃饭、不肯睡觉、怎么跟孩子说、爸爸带娃 等。

## 目录结构

```
daiwa.skill/
├── SKILL.md              # 入口：角色、风险优先级、Dad Mode、决策链、输出格式
├── manifest.json         # 技能清单与知识索引
├── knowledge/
│   ├── scenario_index.json   # 中文关键词 → 场景文件路由
│   ├── child_protection.md   # 儿童保护（最高优先级）
│   ├── age_stages.md / development_norms.md / development_red_flags.md
│   ├── scenarios/            # 22 个高频场景
│   ├── fatherhood/           # 爸爸模块（7 个文件）
│   ├── scripts/              # 现场话术（边界/选择/情绪/鼓励/合作）
│   ├── infant/               # 0-1 岁专项
│   └── …                     # routines / myths / family_alignment / safety 等
├── references/           # 证据分级地图 + 书单/博客来源
├── examples/             # 输出风格示例（含 dad_mode）
├── evals/                # 语义 rubric 评测用例
└── tools/validate.py     # 结构校验
```

## License

MIT

## Evidence

见 `references/evidence_map.md`（研究/机构/实践框架分级）与 `references/books_and_blogs.md`（书单与博客来源）。
