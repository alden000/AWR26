import json, urllib.request
base="https://api.42campaign.io/app/applications/htxawr2026/virtualOverallResults?virtualRunID=6a69f64b7accd8dcb3994158&perPage=100&page="
rows=[];p=1
while True:
    r=urllib.request.Request(base+str(p),headers={"User-Agent":"Mozilla/5.0 Chrome/128.0","Origin":"https://htxawr2026.42campaign.io"})
    d=json.load(urllib.request.urlopen(r))
    if p==1: print({k:v for k,v in d.items() if k!='data'})
    if not d.get("data"): break
    rows+=d["data"]; p+=1
    if p>200: break
json.dump(rows,open("D:/GIT/HTX_AWR_2026/htx_lb.json","w",encoding="utf-8"),ensure_ascii=False)
print(len(rows),"rows")
