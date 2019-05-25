import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
cosy = np.cos(x) / 2
siny = np.sin(x)

plt.plot(x, cosy)
plt.plot(x, siny)
plt.show()