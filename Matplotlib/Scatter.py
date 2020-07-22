import matplotlib.pyplot as plt
import numpy as np

x_data = 100*np.random.randn(100)
y_data = 100*np.random.randn(100)

fig,ax =plt.subplots()
ax.scatter(x_data,y_data)
plt.show()