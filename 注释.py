
import numpy as np
import matplotlib.pyplot as plt

# 生成曲线上各个点的x,y坐标，然后用一段段直线连起来
x = np.linspace(-np.pi, np.pi, 200)  # 产生一个等差数列

cos_y = np.cos(x) / 2
sin_y = np.sin(x)

# 计算特殊点的坐标
xo = np.pi * 3 / 4
yo_cos = np.cos(xo) / 2
yo_sin = np.sin(xo)


# 设置坐标范围
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(min(cos_y.min(), sin_y.min()) * 1.1,
max(cos_y.max(), sin_y.max()) * 1.1)

# 设置坐标轴刻度标签
plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi * 3 / 4, np.pi],
           [r'$-\pi$', r'$-\frac{\pi}{2}$', r'0',
            r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$'])

# plt.yticks([])
plt.yticks([-1, -0.5, 0.5, 1])

# 将矩形坐标轴改成十字坐标轴：
# 获取当前坐标轴对象
ax = plt.gca() # get current axis

# 将垂直坐标刻度置于左边框
ax.yaxis.set_ticks_position('left')

# 将左边框置于数据坐标原点
ax.spines['left'].set_position(('data', 0))

# 将水平坐标刻度置于底边框
ax.xaxis.set_ticks_position('bottom')

# 将底边框置于数据坐标原点
ax.spines['bottom'].set_position(('data', 0))

# 将右边框和顶边框设置成无色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


# 用直线连接曲线上各点
plt.plot(x, cos_y, linestyle='--', linewidth=1, color='dodgerblue', label=r'$y=\frac{1}{2}cos(x)$')
plt.plot(x, sin_y, linestyle=':', linewidth=1.2, color='orangered', label=r'$y=sin(x)$')

# 绘制特殊点
plt.plot([xo, xo], [yo_cos, yo_sin], linestyle='--', linewidth=1, color='limegreen')
plt.scatter([xo, xo], [yo_cos, yo_sin], s=60, edgecolor='limegreen', facecolor='white', zorder=3)

# 添加注释
plt.annotate(r'$\frac{1}{2}cos(\frac{3\pi}{4})=-\frac{\sqrt{2}}{2}$',
             xy=(xo, yo_cos), xycoords='data', xytext=(-90, -40), textcoords='offset points',
             fontsize=14, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.2'))

plt.annotate(r'$sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$', xy=(xo, yo_sin),
             xycoords='data', xytext=(20, 20), textcoords='offset points',
             fontsize=14, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0'))


plt.legend(loc='upper left')

# 显示图形
plt.show()