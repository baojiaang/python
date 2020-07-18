import pandas as pd
import matplotlib.pyplot as plt


file_path= "IMDB-Movie-Data.csv"
df=pd.read_csv(file_path)

rating_mean = df["Rating"].mean()
print(rating_mean)
director_list = df["Actors"].str.split(",").tolist()
nums=set([i for j in director_list for i in j])
print(nums)
max_runtime = df["Runtime (Minutes)"].max()
max_index = df["Runtime (Minutes)"].argmax()
print(max_index)
print(max_runtime)

# rating
rating_data = df["Rating"].values
max_rate = rating_data.max()
min_rate = rating_data.min()

print(max_rate-min_rate)
fig,ax = plt.subplots()
ax.hist(rating_data,int(max_rate-min_rate//0.5))


_x= [min_rate]
i = min_rate
while i<=max_rate+0.5:
    i+=0.5
    _x.append(i)

plt.xticks(_x)   # x轴坐标
plt.show()
