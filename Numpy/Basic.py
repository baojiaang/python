import numpy as np


t1 = np.arange(1,10,2)
type(t1)
print(t1)
print(t1.dtype)

t5=np.array([1,1,1],dtype=bool)
t6=t5.astype("int8")
print(t5)
print(t6)

t7=np.array([np.random.random() for i in range(10)])
print(t7)
t8=np.round(t7,1) # round 保留小数
print(t8)


array=np.array([1,3,5,9,11])
array[array<10]=10
print(array)
np.where()