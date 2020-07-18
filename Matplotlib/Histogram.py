import matplotlib
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10000000)

mu=100
sigma=15
x=mu+sigma*np.random.randn(437)

num_bins=50

fig,ax=plt.subplots()

n,bins,pathches=ax.hist(x,num_bins,density=True)

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

ax.plot(bins,y,'--')
ax.set(xlabel="smarts",ylabel="probability density",title=r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()