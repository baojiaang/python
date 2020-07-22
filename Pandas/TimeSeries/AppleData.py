import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("./appl_1980_2014.csv")
print(data.dtypes)

data['Date'] = pd.to_datetime(data['Date'])

data = data.set_index('Date')
print(data.head())

# 根据时间重采样
data_re = data.resample('BM').mean()
print(data_re)

time = (data.index.max()-data.index.min()).days
print(time)

x_data = data.index
y_data = data['Adj Close']

print(x_data)
print(y_data)

fig, ax = plt.subplots()
ax.plot(x_data,y_data)
plt.title('Apple Stock')
plt.show()