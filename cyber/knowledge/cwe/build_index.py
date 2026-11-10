# Convertit le XML MITRE CWE en index JSON léger (un objet par CWE).
import json, sys, xml.etree.ElementTree as ET

src, dst = sys.argv[1], sys.argv[2]
ns = {"c": "http://cwe.mitre.org/cwe-7"}
root = ET.parse(src).getroot()
out = []
for w in root.iter("{http://cwe.mitre.org/cwe-7}Weakness"):
    desc = (w.findtext("c:Description", default="", namespaces=ns) or "").strip()
    ext = (w.findtext("c:Extended_Description", default="", namespaces=ns) or "").strip()
    out.append({
        "id": f"CWE-{w.get('ID')}",
        "name": w.get("Name"),
        "status": w.get("Status"),
        "abstraction": w.get("Abstraction"),
        "description": " ".join(desc.split()),
        "extended": " ".join(ext.split())[:800],
    })
out.sort(key=lambda x: int(x["id"].split("-")[1]))
with open(dst, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(len(out), "CWE écrites dans", dst)
