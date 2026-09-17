#!/usr/bin/env python3
"""场景测试运行器：路由预测 + rubric 知识锚点 + 一致性检查

用法: python tools/run_scenario_tests.py
退出码: 0 全部通过 / 1 存在 FAIL
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
K = ROOT / "knowledge"
fails, warns, passes = [], [], 0

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
index = json.loads((K / "scenario_index.json").read_text(encoding="utf-8"))

def read(p):
    return (K / p).read_text(encoding="utf-8") if p else ""

cases = []
for line in (ROOT / "evals/scenario_tests.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        cases.append(json.loads(line))

print(f"共 {len(cases)} 条场景测试用例\n")

# ---------- 逐用例检查 ----------
for c in cases:
    cid, problems, notes = c["id"], [], []

    # 1. 目标文件存在
    content = ""
    for t in c.get("targets", []):
        if not (K / t).exists():
            problems.append(f"目标文件不存在: {t}")
        else:
            content += "\n" + read(t)
    content += "\n" + skill  # SKILL.md 也算知识来源

    # 2. rubric 锚点在知识库中可支撑（semantic_only 用例交给 LLM 判定，跳过）
    if not c.get("semantic_only"):
        missing = [r for r in c.get("rubric", []) if r not in content]
        if missing:
            notes.append(f"锚点未直接命中(需语义判断): {missing}")

    # 3. 路由预测: 用 scenario_index 模拟检索
    if not c.get("skip_routing") and c.get("targets"):
        hits = set()
        for key, files in index.items():
            if key in c["input"]:
                hits.update(files)
        if not hits:
            notes.append("路由: 无索引关键词命中 → agent 需自行判断")
        else:
            tgts = set(c["targets"])
            inter = tgts & hits
            same_dir = any(Path(t).parent == Path(h).parent for t in tgts for h in hits)
            if not inter and not same_dir:
                problems.append(f"路由偏差: 索引命中 {sorted(hits)} 与目标 {sorted(tgts)} 不相交")

    if problems:
        fails.append((cid, problems))
    elif notes:
        warns.append((cid, notes))
    else:
        passes += 1

# ---------- 仓库级一致性检查 ----------
# 家庭卡字段三方一致 (SKILL.md == family_alignment == schema 键数)
fa = read("family_alignment.md")
seg = re.search(r"## 家庭统一模式.*?(?=\n## )", skill, re.S)
sk_cards = set(re.findall(r"【(.+?)】", seg.group(0))) if seg else set()
fa_cards = set(re.findall(r"【(.+?)】", fa))
schema = json.loads((K / "family_card_schema.json").read_text(encoding="utf-8"))
if sk_cards != fa_cards:
    fails.append(("cons-card", [f"SKILL.md 卡字段 {sorted(sk_cards)} != family_alignment {sorted(fa_cards)}"]))
elif len(fa_cards) != len(schema):
    fails.append(("cons-card", [f"卡片字段 {len(fa_cards)} 个 != schema 键 {len(schema)} 个"]))
else:
    passes += 1

# 场景索引全覆盖
actual = {"scenarios/" + f.name for f in (K / "scenarios").iterdir()}
indexed = {t for ts in index.values() for t in ts}
gap = actual - indexed
if gap:
    fails.append(("cons-index", [f"场景未索引: {sorted(gap)}"]))
else:
    passes += 1

# ---------- 汇总 ----------
for cid, ps in fails:
    for p in ps:
        print(f"FAIL  {cid}: {p}")
for cid, ns in warns:
    for n in ns:
        print(f"WARN  {cid}: {n}")

print("-" * 46)
print(f"PASS {passes} / WARN {len(warns)} / FAIL {len(fails)}")
sys.exit(1 if fails else 0)
