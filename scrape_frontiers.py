import urllib.request
import re

url = "https://www.frontiersin.org/journals"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    names = re.findall(r'"name":"([^"]+)"', html)
    journals = sorted(list(set(n for n in names if "Frontiers in" in n or "Acta" in n or "Science" in n or "Medicine" in n or n.startswith("Frontiers "))))
    
    with open("journals_list.md", "w") as f:
        f.write("# Available Frontiers Sub-Journals\n\n")
        f.write("You can set the `journal` option in your Quarto YAML header to any of the following:\n\n```yaml\nformat:\n  frontiers-pdf:\n    journal: \"Frontiers in Cardiovascular Medicine\"\n```\n\n### Journal List\n\n")
        for j in journals:
            f.write(f"- {j}\n")
    print(f"Generated journals_list.md with {len(journals)} entries")
except Exception as e:
    print("Error:", e)
