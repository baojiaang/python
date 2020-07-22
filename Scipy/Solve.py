from scipy import optimize
import math


def f(x):
    return [
        5*x[1]+3,
        4*x[0]**2 - 2*math.sin(x[1]*x[2]),
        x[1]*x[2] - 1.5
    ]


res = optimize.fsolve(f,[9,8,5])
print(res)