import pandas as pd

cars_data1 = pd.read_csv('./cars1.csv')
cars_data2 = pd.read_csv('./cars2.csv')

cars_data1 = cars_data1.loc[:,"mpg":"car"]
print(cars_data1.head())

cars = cars_data1.append(cars_data2)
print(cars.shape)