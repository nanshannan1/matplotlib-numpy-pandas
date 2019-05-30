# coding:utf-8

import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas as pd
import numpy as np


# 解决中文的乱码问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 使用pandas读取数据
chipo = pd.read_csv('/sjfx/cc/datasets/chipo.csv')
# print(chipo.iloc[0:10])

# item_name = chipo.ix[:, 'item_name']
# print(item_name)



item_name_01 = chipo.groupby("item_name").count()
# print(item_name_01)
item_name_02 = item_name_01.sort_values(by='Unnamed: 0', ascending=False)
# print(item_name_02['Unnamed: 0'])
item_name_03 = item_name_02['Unnamed: 0']
item_name_03 = item_name_03.head()
x = item_name_03.index
y = item_name_03.values
plt.figure(figsize=(15, 7))
plt.bar(x, y, label='商品名')
plt.title('商品购买次数排名')
plt.xlabel('商品名称')
plt.ylabel('出现的订单次数')
plt.legend(loc='upper right')
plt.show()