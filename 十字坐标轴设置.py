import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
cos_y = np.cos(x)
sin_y = np.sin(x)

ax = plt.gca()
ax.spines['left'].set_position(('axes', 0.5))
ax.spines['bottom'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', -3))

ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')

plt.plot(x, cos_y, linestyle='-', linewidth=1, color='red')
plt.plot(x, sin_y, linestyle=':', linewidth=2, color='green')

plt.show()