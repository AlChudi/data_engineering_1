from bs4 import BeautifulSoup
import re
import json
import pandas as pd
import collections

def handle_file(file_name):
    with (open (file_name, encoding="utf-8") as file):
        text = ""
        for row in file.readlines():
            text += row


        site = BeautifulSoup(text, 'html.parser')
        # print(site.prettify())

        item = dict()
        item['city'] = site.find_all("span", string=re.compile("Город:"))[0].get_text().split(":")[1].strip()
        item['title'] = site.find_all("h1")[0].get_text().split(":")[1].strip()
        address0 = site.find_all("p")[0].get_text().split("Индекс:")
        item['street'] = address0[0].split(":")[1].strip()
        item['zipcode'] = address0[1].strip()
        # print(item['street'])
        # print(item['zipcode'])
        item['floors'] = int(site.find_all("span", attrs={'class': 'floors'})[0].get_text().split(":")[1].strip())
        item['year'] = int(site.find_all("span", attrs={'class': 'year'})[0].get_text().replace("Построено в", "").strip())
        parking1 = site.find_all("span", string=re.compile("Парковка"))[0].get_text().split(":")[1].strip()
        item['parking'] = parking1 == 'есть'
        item['img.url'] = site.find_all("img")[0]['src']
        item['rating'] = float(site.find_all("span", string=re.compile("Рейтинг"))[0].get_text().split(":")[1].strip())
        item['views'] = int(site.find_all("span", string=re.compile("Просмотры"))[0].get_text().split(":")[1].strip())

        return item

handle_file("1_32.html")

items = []
for i in range(1, 999):
    file_name = f"1_32/{i}.html"
    result = handle_file(file_name)
    items.append(result)
    if i < 100:
        print(result)

items = sorted(items, key=lambda x: x['views'], reverse=True)

with open("result_all_1_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(items))

filtered_items = []
for building in items:
    if building['floors'] >= 6:
        filtered_items.append(building)

with open("result_filtr_1_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(filtered_items))

result = []

df = pd.DataFrame(items)
pd.set_option('display.float_format', '{:.2f}'.format)
data1 = df['floors']
#  print(data1.describe())  #  статистические х-ки

words = df['city']
data2 = collections.Counter(words)
#  print(data2)  # частота городов


