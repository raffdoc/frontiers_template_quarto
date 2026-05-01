import urllib.request
import re

url = "https://www.frontiersin.org/journals"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.finditer(r'href="(https://www\.frontiersin\.org/journals/[^"]+)">(.*?)</a>', html)
    journals = []
    seen = set()
    for m in matches:
        title = m.group(2).strip()
        link = m.group(1).strip()
        if "<" in title or "View" in title: continue
        if link not in seen:
            seen.add(link)
            journals.append(f"- [{title}]({link})")
    
    with open("journals_list.md", "w") as f:
        f.write("# Available Frontiers Journals\n\n")
        f.write("\n".join(sorted(journals)))
    print(f"Generated journals_list.md with {len(journals)} entries")
except Exception as e:
    print(e)
