from scipy import optimize

def f(x,para):
    return x[0]**2+x[1]**2+para

# fun：目标函数，返回单值，
# x0：初始迭代点，
# method：求解方法


res = optimize.minimize(f,[1,10],args=(10),method='SLSQP')
print(res)