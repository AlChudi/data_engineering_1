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
        item = dict()
        item['name'] = site.find_all("name")[0].get_text().strip()
        item['constellation'] = site.find_all("constellation")[0].get_text().strip()
        item['spectral-class'] = site.find_all("spectral-class")[0].get_text().strip()
        item['radius'] = int(site.find_all("radius")[0].get_text().strip())
        item['rotation'] = site.find_all("rotation")[0].get_text().strip()
        item['age'] = site.find_all("age")[0].get_text().strip()
        item['distance mln km'] = float(site.find_all("distance")[0].get_text().strip().replace(" million km", "")) # чтобы был числовой формат
        item['absolute-magnitude'] = site.find_all("absolute-magnitude")[0].get_text().strip()

        return item


#handle_file("3_32.xml")

items = []
for i in range(1, 500):
    file_name = f"3_32/{i}.xml"
    result = handle_file(file_name)
    items.append(result)
    if i < 200:
        print(result)

items = sorted(items, key=lambda x: x['distance mln km'], reverse=True)
print(items)
with open("result_all_3_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(items,ensure_ascii=False)) # для отображения кириллицы

filtered_items = []
for building in items:
    if building['radius'] >= 400000000:
        filtered_items.append(building)

with open("result_filtr_3_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(filtered_items)) #без кириллицы

result = []
#
df = pd.DataFrame(items)
pd.set_option('display.float_format', '{:.2f}'.format)
data1 = df['distance mln km']
print(data1.describe())  #  статистические х-ки

words = df['constellation']
data2 = collections.Counter(words)
print(data2)  # частота