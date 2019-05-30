import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 解决中文的乱码问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

df_01 = pd.read_csv('/sjfx/cc/datasets/tips.csv')
print(df_01.head(5))

# 2.2 在同一图中绘制:吸烟顾客与不吸烟顾客的消费金额与小费之间的散点图
smoker = df_01[df_01['smoker'] != 'No']
no_smoker = df_01[df_01['smoker'] == 'No']

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.scatter(smoker['total_bill'], smoker['tip'])
plt.xlabel('消费的总金额')
plt.ylabel('小费的金额')
plt.title('吸烟顾客')

plt.subplot(2, 1, 2)
plt.scatter(no_smoker['total_bill'], no_smoker['tip'])
plt.xlabel('消费的总金额')
plt.ylabel('小费的金额')
plt.title('不吸烟顾客')
plt.show()