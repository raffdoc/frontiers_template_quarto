import urllib.request
import re

url = "https://www.frontiersin.org/journals"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Use a regex to find all journal titles. They usually are inside <a> tags or similar
    # In next.js apps, they are typically inside a JSON blob like <script id="__NEXT_DATA__" type="application/json">
    match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, re.DOTALL)
    if match:
        import json
        data = json.loads(match.group(1))
        # Need to blindly dump keys looking for journals
        print("Found __NEXT_DATA__")
    else:
        print("No NEXT_DATA found, checking for NUXT...")
        match2 = re.search(r'window\.__NUXT__=(.*?);</script>', html, re.DOTALL)
        if match2:
            print("Found __NUXT__")
        else:
            print("Just regexing 'href=\"/journals/([a-z-]+)\"'")
            matches = set(re.findall(r'href="/journals/([^"]+)"', html))
            print(f"Found {len(matches)} journal links")
except Exception as e:
    print(f"Error: {e}")
