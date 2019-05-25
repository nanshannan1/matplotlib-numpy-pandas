import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,100,50)
y1 = x * 0.25
y2 = x * 0.5
y3 = x * 1
y4 = x * 2
d = np.linspace(1,10000,50)

plt.figure('Scatter', facecolor='lightgray')
plt.title('Scatter', fontsize=20)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.scatter(x, y1, s=60, c=d, cmap='jet_r', alpha=0.5)
plt.scatter(x, y2, s=60, c=d, cmap='jet', alpha=0.5)
plt.scatter(x, y3, s=60, c=d, cmap='gray_r', alpha=0.5)
plt.scatter(x, y4, s=60, c=d, cmap='gray', alpha=0.5)

plt.show()