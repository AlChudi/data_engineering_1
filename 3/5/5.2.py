from bs4 import BeautifulSoup
import json
import pandas as pd
import collections

def handle_file(file_name):
    items = list()
    with open(file_name, encoding='utf-8') as file:
        text = ""
        for row in file.readlines():
            text += row

        site = BeautifulSoup(text, 'html.parser')
        products = site.find_all("div", attrs={'class': 'product-info'})

        for product in products:
            item = dict()
            image = product.find_all("div", attrs={'title'})[0]
            item['title'] = image.find_all("a")[0].get_text().strip()
            item['img'] = product.find_all("img")[0]['src']
            item['weight'] = product.find_all("div", attrs={'class': 'product-weight'})[0].get_text('').strip().replace("\xa0", " ").strip()
            item['price'] = int(product.find_all("div", attrs={'class': 'price-current'})[0].get_text().split("\n")[1].replace(" ","").strip())

            items.append(item)

    return items

#handle_file("5.2.html")

items = []
for i in range(1, 10):
    file_name = f"5.2_32/{i}.html"
    items += handle_file(file_name)

items = sorted(items, key=lambda x: x['price'], reverse=True)

with open("result_all_5.2_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(items))

filtered_items = []
for building in items:
    if building['price'] > 5000:
        filtered_items.append(building)

# print(len(items))
# print(len(filtered_items))

with open("result_filtr_5.2_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(filtered_items))

df = pd.DataFrame(items)
pd.set_option('display.float_format', '{:.2f}'.format)
data1 = df['price']
print(data1.describe())  #  статистические х-ки

words = df['weight']
data2 = collections.Counter(words)
print(data2)  # частота

