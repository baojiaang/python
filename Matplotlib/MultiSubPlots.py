import numpy as np
import matplotlib.pyplot as plt

x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)

y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(np.pi*x2)

fig,axes=plt.subplots(2,1)
axes[0].plot(x1,y1)
axes[1].plot(x2,y2)

plt.show()

