import matplotlib
import matplotlib.pyplot as plt
import numpy as np


t=np.arange(0.0,5.0,0.05)    #return array
s=np.sin(t)

fig,ax=plt.subplots()
ax.plot(t,s)

ax.set(xlabel="time",ylabel="value",title="pic")
ax.grid()

#fig.savefig("SicPic.png")
plt.show()