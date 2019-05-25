import numpy as np
import matplotlib.pyplot as plt

# 生成曲线上各点的x, y坐标， 然后用一个直线连接起来
x = np.linspace(-np.pi, np.pi, 200)
cos_y = np.cos(x)
sin_y = np.sin(x)

# 设置坐标的范围
plt.xlim(x.min()*1.1, x.max()*1.1)
plt.ylim(min(cos_y.min(), sin_y.min())*1.1, max(cos_y.max(), sin_y.max())*1.1)

# 设置坐标轴的刻度标签
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi * 3 / 4, np.pi],
           [r'$-\pi$', r'$-\frac{\pi}{2}$', r'0',
            r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])
plt.yticks([-1, -0.5, 0.5, 1])

# 将矩形坐标轴改成十字坐标轴
# 获取当前的坐标轴对象
ax = plt.gca()
ax.yaxis.set_ticks_position('left')

# 将左边的框至于数据坐标的原点
ax.spines['left'].set_position(('data', 0))

# 将水平坐标刻度置于底边框
ax.xaxis.set_ticks_position('bottom')

# 将底边框置于数据坐标原点
ax.spines['bottom'].set_position(('data', 0))

# 将右边框和底边框设置成为无色
ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')

# 用直线连接曲线上各点
plt.plot(x, cos_y, linestyle='--', linewidth=1, color='dodgerblue')
plt.plot(x, sin_y, linestyle=':', linewidth=1.2, color='orangered')

# 显示图形
plt.show()