import matplotlib.pyplot as plt
import numpy as np

plt.style.use(['science', 'no-latex'])

# 可以用 with: plt.style.context(['science','scatter'])
# 或者 直接 plt.style.use(['science', 'no-latex'])
# science科学画图  scatter 散点  ieee风格 high-vis高对比风格 vibrant风格


#
# fig,ax = plt.subplots()
# x = [1,2,3]
# y = [1,2,3]
#
# ax.plot(x,y)
# plt.show()


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


x = np.linspace(0.75, 1.25, 201)
fig, ax = plt.subplots()
for p in [10, 20, 50]:
    ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
ax.set(xlabel='Voltage (mV)')
ax.set(ylabel='Current ($\mu$A)')
ax.autoscale(tight=True)
plt.show()