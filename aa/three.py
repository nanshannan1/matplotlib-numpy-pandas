import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 解决中文的乱码问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 读取数据
df_01 = pd.read_csv('/sjfx/cc/datasets/tips.csv')

# 吸烟的人
smoker = df_01[df_01['smoker'] != 'No']
male_smoker = smoker[smoker['sex'] == 'Male']
Female_smoker = smoker[smoker['sex'] == 'Female']

# 不吸烟的人
no_smoker = df_01[df_01['smoker'] == 'No']
male_no_smoker = no_smoker[no_smoker['sex'] == 'Male']
Female_no_smoker = no_smoker[no_smoker['sex'] == 'Female']

# 将提取的数据放置在画板上
plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.scatter(male_smoker['total_bill'], male_smoker['tip'], label='男性吸烟顾客')
plt.scatter(male_no_smoker['total_bill'],
            male_no_smoker['tip'], label='男性不吸烟顾客')
plt.xlabel('消费总金额')
plt.ylabel('小费金额')
plt.title('sex=Male')
plt.legend()

plt.subplot(2, 1, 2)
plt.scatter(Female_smoker['total_bill'],
            Female_smoker['tip'], label='女性吸烟顾客')
plt.scatter(Female_no_smoker['total_bill'],
            Female_no_smoker['tip'], label='女性不吸烟顾客')

plt.xlabel('消费总金额')
plt.ylabel('小费金额')
plt.title('sex=Female')
plt.legend()
plt.show()
