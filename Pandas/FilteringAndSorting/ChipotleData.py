import pandas as pd


url = "./chipotle.tsv"

data = pd.read_csv(url, sep ='\t') # \t delimiter
# for value in data.item_price:
#     print(value)
#     print(type(value))
prices = [float(value[1:-1]) for value in data.item_price]   # 去除$符号
data.item_price = prices
data_filtered = data.drop_duplicates(['item_name','quantity','choice_description'])  # 去重  列名

price_per_item = data[['item_name','item_price']]
print(price_per_item.sort_values(by='item_price',ascending=False).head())
