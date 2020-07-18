import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

file_path = "starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)


# grouped = df.groupby("Country")
# print(grouped)

# for i,j in grouped:
#     print(i)
#     print("*"*100)
#     print(j,type(j))
#     print()

# 聚合
# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["AU"])

# 每个省
# china_data = df[df["Country"] == "CN"]
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
# print(grouped)

# 多条件分组，返回series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))

# 多条件分组，返回dataframe
# grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()


# print(grouped1,type(grouped1))
# print("-"*100)

# 排名前十国家
# data = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10]
# _x = data.index
# _y = data.values
#
# fig, ax= plt.subplots()
# ax.bar(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x)
# plt.show()

# 中国店铺前十城市
df = df[df["Country"]=="CN"]
data = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:10]
x = data.index
y = data.values

fig, ax =plt.subplots()
ax.barh(range(len(x)),y)
plt.yticks(range(len(x)),x)
plt.show()