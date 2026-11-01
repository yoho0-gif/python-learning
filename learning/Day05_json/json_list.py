products = [
    {
        "name": "滑鼠",
        "price": 500
    },
    {
        "name": "鍵盤",
        "price": 1200
    },
    {
        "name": "螢幕",
        "price": 4500
    }
]

total_price = 0
most_expensive_product = 0
most_expensive_product_name = ""
for product in products:
    print(product["name"] ,product["price"])
    total_price = total_price + product["price"]
    if product["price"] > most_expensive_product:
        most_expensive_product = product["price"]
        most_expensive_product_name = product["name"]
print("總價:" + str(total_price))
print("最貴商品:" + most_expensive_product_name + str(most_expensive_product))

# total_price = 0
# most_expensive_price = 0
# most_expensive_name = ""

# for product in products:
#     print(f'{product["name"]}：{product["price"]} 元')

#     total_price += product["price"]

#     if product["price"] > most_expensive_price:
#         most_expensive_price = product["price"]
#         most_expensive_name = product["name"]

# print(f"總價：{total_price} 元")
# print(f"最貴商品：{most_expensive_name} ({most_expensive_price} 元)")