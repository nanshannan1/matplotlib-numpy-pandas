import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 解决中文的乱码问题
plt.rcParams["font.sans-serif"] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# 加载数据并显示前五行记录
tips = pd.read_csv("./datasets/tips.csv")
print(tips.head(5))

# 在同一张图中绘制：吸烟的顾客与不吸烟的顾客消费金额与小费之间的散点图
smoker = tips[tips['smoker'] != 'No']
no_smoker = tips[tips['smoker'] == 'No']

# 也可以直接写 plt.subplot(1, 2, 1)
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)


x = smoker['total_bill']
y = smoker['tip']
plt.scatter(x, y, s=20, c="red", label='吸烟顾客')
plt.legend()

x1 = no_smoker['total_bill']
y1 = no_smoker['tip']

plt.scatter(x1, y1, s=20, c="green", label='不吸烟顾客')

#  在同一图中绘制:女性与男性中吸烟与不吸烟顾客的消费金额与
# 小费之间的散点图关系
ax2 = fig.add_subplot(1, 2, 2)
w_s = smoker[smoker['sex'] == 'Male']
w_n_s = no_smoker[no_smoker['sex'] == 'Male']
f_s = smoker[smoker['sex'] == 'Female']
f_n_s = no_smoker[no_smoker['sex'] == 'Male']

plt.scatter(w_s['total_bill'], w_s['tip'], label='吸烟女性')
plt.scatter(f_s['total_bill'], f_s['tip'], label='吸烟男性')
plt.scatter(w_n_s['total_bill'], w_n_s['tip'], label='不吸烟女性')
plt.scatter(f_n_s['total_bill'], f_n_s['tip'], label='不吸烟男性')


plt.legend()
plt.show()



