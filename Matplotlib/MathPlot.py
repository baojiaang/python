import numpy as np
import matplotlib.pyplot as plt

f = lambda x, a: np.cos(np.pi * a * x) * np.exp(-x)
a_vals = np.linspace(0, 2, 10)
x_data = np.linspace(0,5,100)
fig, ax = plt.subplots()
for a in a_vals:
    ax.plot(x_data,f(x_data,a))
plt.show()
