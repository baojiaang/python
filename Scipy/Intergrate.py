import scipy.integrate
from numpy import exp
import pandas as pd

def f(x):
    return exp(-x**2)


i=scipy.integrate.quad(f,0,1)
print(i)

list=[1,2,3,4,5]
for i,n in enumerate(list):
    if((i+1)%3==0):
        print(n)

prov_id = pd.read_excel(r"D:\Py\data\province_id.xlsx")
city_id = pd.read_excel(r"D:\Py\data\city_id.xlsx")