from bs4 import BeautifulSoup
import json
import pandas as pd
import collections

def handle_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        text = ""
        for row in file.readlines():
            text += row
        site = BeautifulSoup(text, 'xml')
        for clothing in site.find_all("clothing"):
            item = {}
            for el in clothing.contents:
                if el.name is None:
                    continue
                elif el.name == "rating":
                    item[el.name] = float(el.get_text().strip())
                elif el.name == "price" or el.name == "reviews":
                    item[el.name] = int(el.get_text().strip())
                elif el.name == "new":
                    item[el.name] = el.get_text().strip() == "+"
                elif el.name == "exclusive" or el.name == "sporty":
                    item[el.name] = el.get_text().strip() == "yes"
                else:
                    item[el.name] = el.get_text().strip()
            items.append(item)
    return item

#handle_file("4_32.xml")
items = []
for i in range(1, 100):
    file_name = f"4_32/{i}.xml"
    result = handle_file(file_name)
    items.append(result)
    if i < 100:
        print(result)
#print(len(items))

items = sorted(items, key=lambda x: x['price'])
#
with open("result_all_4_json", "w", encoding="utf-8") as f:
     f.write(json.dumps(items))

filtered_items = []
for building in items:
    if building['price'] > 800000:
          filtered_items.append(building)

with open("result_filtr_4_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(filtered_items))

#result = []

df = pd.DataFrame(items)
pd.set_option('display.float_format', '{:.2f}'.format)
data1 = df['reviews']
print(data1.describe())  #  статистические х-ки

words = df['category']
data2 = collections.Counter(words)
print(data2)  # частота