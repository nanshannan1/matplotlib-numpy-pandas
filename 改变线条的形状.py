import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
cosy = np.cos(x) / 2
siny = np.sin(x)

plt.plot(x, cosy, linestyle="-", linewidth=1, color="red")
plt.plot(x, siny, linestyle=":", linewidth=2.5, color="green")

plt.show()