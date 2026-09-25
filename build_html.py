# Builds index.html from template.html + htx_lb.json (run htx_lb.py first to refresh the data)
import json, os, datetime
d = "D:/GIT/HTX_AWR_2026/"
rows = json.load(open(d + "htx_lb.json", encoding="utf-8"))
ts = datetime.datetime.fromtimestamp(os.path.getmtime(d + "htx_lb.json")).strftime("%d %b %Y %H:%M")
data = {"ts": ts, "rows": [[r["_id"], r["rank"], r["name"], r["result"]] for r in rows]}
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", r"<\/")
html = open(d + "template.html", encoding="utf-8").read().replace("/*__DATA__*/", blob)
open(d + "index.html", "w", encoding="utf-8").write(html)
print("wrote index.html", len(rows), "rows,", len(html) // 1024, "KB")
