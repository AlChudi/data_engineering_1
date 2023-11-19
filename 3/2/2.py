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
        products = site.find_all("div", attrs={'class': 'product-item'})


        for product in products:
            item = dict()
            item['id'] = product.a['data-id']
            item['link'] = product.find_all('a')[1]['href']
            item['img_url'] = product.find_all("img")[0]['src']
            item['title'] = product.find_all("span")[0].get_text().strip()
            item['price'] = int(product.price.get_text().replace("₽", "").replace(" ", "").strip())
            item['bonus'] = int(product.strong.get_text().replace("+ начислим ", "").replace(" бонусов", "").strip())
            props = product.ul.find_all("li")
            for prop in props:
                item[prop['type']] = prop.get_text().strip()

            items.append(item)
    return item

#handle_file("2_32.html")
items = []
for i in range(1, 37):
    file_name = f"2_32/{i}.html"
    result = handle_file(file_name)
    items.append(result)
    if i < 100:
        print(result)

items = sorted(items, key=lambda x: x['price'], reverse=True)
print(items)

with open("result_all_2_json", "w", encoding="utf-8") as f:
     f.write(json.dumps(items))

filtered_items = []
for building in items:
    if building['bonus'] > 3000:
        filtered_items.append(building)

with open("result_filtr_2_json", "w", encoding="utf-8") as f:
    f.write(json.dumps(filtered_items))

# result = []

df = pd.DataFrame(items)
pd.set_option('display.float_format', '{:.2f}'.format)
data1 = df['price']
# print(data1.describe())  #  статистические х-ки

words = df['camera']
data2 = collections.Counter(words)
# print(data2)  # частота камер
