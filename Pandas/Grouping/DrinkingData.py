import pandas as pd

data = pd.read_csv('./drinks.csv')
grouped = data.groupby(by='continent')

print(grouped['beer_servings'].mean())

# aggregation
agg = grouped['spirit_servings'].agg(['mean','max','min'])
print(agg)

sum_grouped = grouped.sum()
print(sum_grouped)

