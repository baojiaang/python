import numpy as np
import pandas as pd

index = pd.read_excel(r"D:\Py\data\baidu_index_0625.xlsx")
prov_id = pd.read_excel(r"D:\Py\data\province_id.xlsx")
city_id = pd.read_excel(r"D:\Py\data\city_id.xlsx")

# 处理缺失值
index = index.fillna(0)

index['date'] = pd.to_datetime(index['date'])
index['date'] = index['date'].dt.strftime('%B')

index['keyword'] = index['keyword'].apply(lambda x: x.strip(' \r\n\t').upper())

new_index_mean = index.groupby(['keyword', 'date'])['_index'].sum()

print(new_index_mean)

prov_index = pd.read_excel(r"D:\Py\data\province_index_0625.xlsx")
# 同样对日期进行格式化处理
prov_index['date'] = prov_index['date'].apply(lambda x: x.split("|")[0])
prov_index['date'] = pd.to_datetime(prov_index['date'])
prov_index['date'] = prov_index['date'].dt.strftime('%B')  # 将日期转换成月份

prov_index['keyword'] = prov_index['keyword'].apply(lambda x: x.strip(' \r\n\t').upper())
prov_index.head()  # display first five data
