import pandas as pd
import numpy as np
data = pd.read_csv('./wine.data')

# delete columns
data = data.drop(data.columns[[0,3,6,8,11,12,13]], axis = 1)
print(data.head())


# set columns
data.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']

data.iloc[0:1,0] = np.nan

data.iloc[:,0].fillna(10,inplace=True)

random = np.random.randint(10,size=10)
data['alcohol'][random]= np.nan

data = data.dropna(axis=0,how="any")
data = data.reset_index()
print(data.head())