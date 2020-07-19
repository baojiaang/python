import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
print(data.info())


# count values
counted = data['Gender'].value_counts()
print(counted)

