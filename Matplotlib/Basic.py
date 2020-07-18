import matplotlib.pyplot as plt
import numpy as np
A = np.arange(1,5)
B = A**2
C = A**3
fig,ax=plt.subplots()
ax.plot(A,B)