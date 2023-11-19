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
        item = dict()
        item['title'] = site.find_all("h1")[0].get_text().strip()
        item['price'] = int(site.find_all("div", attrs={'class': 'price-current'})[0].get_text().split("\n")[1].replace(" ", "").strip())
        item['weight'] = site.find_all("div", attrs={'class': 'product-weight'})[0].get_text('').strip().replace("\xa0", " ").strip()
        item['code'] = site.find_all("div", attrs={'class': 'product-code'})[0].get_text().split(":")[1].strip()
        item['type'] = site.find_all("div", attrs={'class': 'product-attrubute'})[0].get_text().split(":")[1].replace(" ", "").strip()
        item['size'] = site.find_all("div", attrs={'class': 'product-attrubute'})[1].get_text().split(":")[1].strip()
        item['age'] = site.find_all("div", attrs={'class': 'product-attrubute'})[2].get_text().split(":")[1].strip()
        item['class'] = site.find_all("div", attrs={'class': 'product-attrubute'})[3].get_text().split(":")[1].strip()
        item['use'] = site.find_all("div", attrs={'class': 'product-attrubute'})[4].get_text().split(":")[1].strip()
        #print(item)

        return item

#handle_file("5_32.html")

items = []
for i in range(1, 13):
    file_name = f"5_32/{i}.html"
    result = handle_file(file_name)
    items.append(result)
    if i < 100:
        print(result)

items = sorted(items, key=lambda x: x['price'], reverse=True)
with open("result_all_5_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(items))

filtered_items = []
for building in items:
    if building['price'] > 800:
        filtered_items.append(building)

# print(len(items))
# print(len(filtered_items))

with open("result_filtr_5_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(filtered_items))

# result = []

df = pd.DataFrame(items)
pd.set_option('display.float_format', '{:.2f}'.format)
data1 = df['price']
print(data1.describe())  #  статистические х-ки

words = df['class']
data2 = collections.Counter(words)
print(data2)  # частота