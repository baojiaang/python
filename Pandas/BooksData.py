import pandas as pd
import matplotlib.pyplot as plt


file_path = "./books.csv"
df = pd.read_csv(file_path)

# print(df.head())
# print(df.info())

# 不同年份书的平均评分 去掉NAN
data = df[pd.notnull(df["original_publication_year"])]
grouped = data["average_rating"].groupby(by=[data["original_publication_year"]]).mean()

x=grouped.index
y=grouped.values

fig,ax=plt.subplots()
ax.plot(range(len(x)),y)
print(len(x))
# 更换x轴
plt.xticks(list(range(len(x)))[::10],x[::10].astype(int),rotation=45)
plt.show()