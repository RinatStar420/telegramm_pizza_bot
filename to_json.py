import json

ar = []
with open('mat.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('mat.json', 'w', encoding='utf-8') as w:
    json.dump(ar, w)