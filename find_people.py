import json, re, sys, difflib
rows = json.load(open("D:/GIT/HTX_AWR_2026/htx_lb.json", encoding="utf-8"))
people = [l.strip() for l in open("D:/GIT/HTX_AWR_2026/people.txt", encoding="utf-8") if l.strip()]
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
for q in people:
    toks = [norm(t) for t in q.split()]
    exact, partial = [], []
    for r in rows:
        n = norm(r["name"])
        hits = sum(t in n for t in toks)
        if hits == len(toks): exact.append(r)
        elif hits and len(toks) > 1 and any(len(t) >= 4 and t in n for t in toks): partial.append(r)
    fuzzy = [r for r in rows if r not in exact and difflib.SequenceMatcher(None, norm(q), norm(r["name"])).ratio() >= 0.75]
    print(f"\n### {q}")
    for lbl, lst in (("MATCH", exact), ("FUZZY", fuzzy), ("PARTIAL", partial[:8])):
        for r in lst: print(f"  {lbl:7} #{r['rank']:<5} {r['result']:>7}  {r['name'].strip()}")
    if not (exact or fuzzy or partial): print("  (none)")
