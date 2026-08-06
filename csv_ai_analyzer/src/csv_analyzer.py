from csv_loader import load_csv
import json

def summarize_sales(data):
    if not data:
        return None

    total_orders = len(data)
    total_amount = 0
    product_sales = {}
    daily_sales = {}


    for row in data:
        amount = int(row["金額"])
        total_amount += amount


        product = row["商品"]
        product_sales[product] = product_sales.get(product, 0) + amount
        

        daily = row["日期"]
        daily_sales[daily] = daily_sales.get(daily, 0) + amount

    average_sales = total_amount / total_orders
    best_product = max(product_sales, key=product_sales.get)
    best_product_sales = product_sales[best_product]
    best_order = max(data, key=lambda x: int(x["金額"]))

    summary = {
        "每日銷售額": daily_sales,
        "總訂單": total_orders,
        "總金額": total_amount,
        "平均訂單金額": average_sales,
        "最暢銷商品": best_product,
        "最暢銷商品銷售額": best_product_sales,
        "最高單筆訂單": best_order
    }

    return summary


summary = summarize_sales(load_csv("csv_ai_analyzer/src/sample/sales.csv"))
print(json.dumps(summary, ensure_ascii=False, indent=4))


