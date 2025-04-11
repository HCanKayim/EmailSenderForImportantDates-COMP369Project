import json

with open("./data.json", 'r') as f:
    data = json.load(f)

seen_appids = set()
filtered_apps = []

for ele in data:
    name = ele['name']
    if name not in seen_appids:
        seen_appids.add(name)
        filtered_apps.append(ele)

with open("./data.json", 'w') as f:
    json.dump(filtered_apps, f, indent=4)