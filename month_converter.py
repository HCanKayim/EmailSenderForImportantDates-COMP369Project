import json

item_list = []

with open("./data.json", "r") as f:
    data = json.load(f)

for ele in data:

    item_dict = {}

    print(ele)

    month = ele['date'].split()[1]

    match(month):
        case('OCAK'):
            date = ele['date'] = f"{ele['date'].split()[0]} January"
        case('ŞUBAT'):
            date = ele['date'] = f"{ele['date'].split()[0]} February"
        case('MART'):
            date = ele['date'] = f"{ele['date'].split()[0]} March"
        case('NİSAN'):
            date = ele['date'] = f"{ele['date'].split()[0]} April"
        case('MAYIS'):
            date = ele['date'] = f"{ele['date'].split()[0]} May"
        case('HAZİRAN'):
            date = ele['date'] = f"{ele['date'].split()[0]} June"
        case('TEMMUZ'):
            date = ele['date'] = f"{ele['date'].split()[0]} July"
        case('AĞUSTOS'):
            date = ele['date'] = f"{ele['date'].split()[0]} August"
        case('EYLÜL'):
            date = ele['date'] = f"{ele['date'].split()[0]} September"
        case('EKİM'):
            date = ele['date'] = f"{ele['date'].split()[0]} October"
        case('KASIM'):
            date = ele['date'] = f"{ele['date'].split()[0]} November"
        case('ARALIK'):
            date = ele['date'] = f"{ele['date'].split()[0]} December"

    item_dict['date'] = date
    item_dict['name'] = ele['name']
    item_list.append(item_dict)


with open("./data.json", 'w') as f:
    json.dump(item_list, f, indent=4)
    

