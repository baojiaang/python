import numpy as np
import scipy.spatial
# Reverse a vector (first element becomes last)
# z = np.arange(50)
# z = z[::-1]
# print(z)

# Create a 3x3 matrix with values ranging from 0 to 8
# z = np.arange(9).reshape(3,3)
# print(z)

# Find indices of non-zero elements from [1,2,0,0,4,0]
# indexes =np.nonzero([1,0,1,1,0,1,0])
# print(indexes)

# Create a 3x3 identity matrix
# z = np.eye(3)
# print(z)

# Create a 3x3x3 array with random values
# z = np.random.random((3,3,3))
# print(z)

# Create a 8x8 matrix and fill it with a checkerboard pattern
# z = np.zeros((8,8),dtype=int)
# z[1::2,::2] = 1
# z[::2,1::2] = 1
# print(z)

# How to get all the dates corresponding to the month of July 2016?
# z = np.arange('2020-01','2020-06',dtype='datetime64[D]')
# print(z)

# How to compute ((A+B)*(-A/2)) in place (without copy)?
# a = np.ones(3)*1
# b = np.ones(3)*1
# c = np.ones(3)*1
# np.add(a,b,out=b)
# np.divide(a,2,out=a)
# np.negative(a,out=a)
# np.multiply(a,b,out=a)
# print(a)

# Extract the integer part of a random array of positive numbers using 4 different methods
# z = np.random.uniform(0,10,7)
# print(z-z%1)
# print(z//1)
# print(np.floor(z))
# print(z.astype(int))
# print(np.trunc(z))

# Create a vector of size 10 with values ranging from 0 to 1, both excluded
# z = np.linspace(0,1,11,endpoint=False)[1:]
# print(z)

# Create random vector of size 10 and replace the maximum value by 0
# z = np.random.random(10)
# z[z.argmax()]=1
# print(z)

# Create a structured array with x and y coordinates covering the [0,1]x[0,1] area  网格点矩阵
# z = np.zeros((5,5), [('x',float),('y',float)])
# z['x'],z['y'] = np.meshgrid(np.linspace(0,1,5),np.linspace(0,1,5))
# print(z)

# How to find the closest value (to a given scalar) in a vector?
# z = np.arange(100)
# v = np.random.uniform(0,100)
# index = (np.abs(z-v)).argmin()
# print(z[index])

# Create a structured array representing a position (x,y) and a color (r,g,b)
# z = np.zeros(10, [ ('position', [ ('x', float, 1),
#                                   ('y', float, 1)]),
#                    ('color',    [ ('r', float, 1),
#                                   ('g', float, 1),
#                                   ('b', float, 1)])])
# print(z)

# Consider a random vector with shape (100,2) representing coordinates, find point by point distances
# z = np.random.random((10,2))
# d = scipy.spatial.distance.cdist(z,z)
# print(d)

# Subtract the mean of each row of a matrix
# x = np.random.rand(5,10)
# y = x- x.mean(axis=1,keepdims=True)
# print(y)

# How to sort an array by the nth column?
# z = np.random.random((3,3))
# print(z)
# z = z[z[:,1].argsort()]
# print(z)

# How to tell if a given 2D array has null columns?
z = np.random.randint(0,3,(3,10))
print(~z.any(axis=0).any())