import json
import pickle

with open("./4/price_info_32.json") as f:
    price_info = json.load(f)

with open("./4/products_32.pkl", "rb") as f:
    products = pickle.load(f)


def update_price(product, price_info):
    method = price_info["method"]
    if method == "sum":
        product["price"] += price_info["param"]
    elif method == "sub":
        product["price"] -= price_info["param"]
    elif method == "percent+":
        product["price"] *= (1 + price_info["param"])
    elif method == "percent-":
        product["price"] *= (1 - price_info["param"])

    product["price"] = round(product["price"], 2)

price_info_dict = dict()

for item in price_info:
    price_info_dict[item["name"]] = item

#print(products)

for product in products:
    current_price_info = price_info_dict[product["name"]]
    update_price(product, current_price_info)

#print(products)


with open("products_updated.pkl", "wb") as f:
    f.write(pickle.dumps(products))