import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

# 导入数据并查看切片
chipo = pd.read_csv("./datasets/chipo.csv")

# 统计[item_name]中每种商品出现的频率，绘制柱状图
count_item_name = chipo.groupby('item_name').count().sort_values(by='Unnamed: 0', ascending=False)
# print(count_item_name)
count_item_name = count_item_name['Unnamed: 0']
count_item_name = count_item_name.head()

fig = plt.figure()
# 绘制柱状图
ax1 = fig.add_subplot(1, 2, 1)
x = count_item_name.index
y = count_item_name.values
plt.bar(x, y, label='商品名')
plt.title('购买次数最多的商品排名')
plt.xlabel('商品的名称')
plt.ylabel('出现的订单次数')
plt.legend(loc='upper right')

ax2 = fig.add_subplot(1, 2, 2)
# 根据[order_id]分组，求出每个订单花费的总金额，
# 然后根据每笔订单的总金额和其商品总数量画在散点图(如上)
chipo.item_price = [float(value[1:-1]) for value in chipo.item_price]
orders = chipo.groupby('order_id').sum()
x = orders.item_price
y = orders.quantity

plt.scatter(x, y, s=50, c='green')
plt.title('订单金额与订单的关系')
plt.xlabel('金额')
plt.ylabel('商品数')
plt.show()





plt.show()