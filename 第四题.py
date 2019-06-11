import numpy
import matplotlib.pyplot as plt
import pandas as pd

# 解决使用matplotlib绘图的中文乱码问题
plt.rcParams["font.sans-serif"] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# 导入数据并查看
data = pd.read_csv("./datasets/US_Baby_Names_right.csv")
print(data.head(5))
# 删除[Unnamed: 0]和[Id]列两种方法
# 方法一
# inplace = False 不删除源数据
# data_02 = data.drop(labels=['Unnamed: 0', 'Id'], inplace=False, axis=1)
# print(data_02.head(5))
# 方法二
# del data['Unnamed: 0']
# print(data)

# 判断几何中男孩名字女孩名字谁多
# w_sum = data.groupby("Gender").count()
# print(w_sum)
# value_counts()根据值统计数据
Gender_data = data['Gender'].value_counts()
print(Gender_data)
# 按照[Name]列将数据集进行分组并求和
names = data.groupby('Name').sum()
print(names.head(5))

# 以列[Count]的值对DataFrame降序排序，并查看
a = names.sort_values('Count', ascending=False).head(5)
print(a)

# 统计数据集中名字的个数(不含重复项，至少使用两种方法)
# 去除重复项
data03 = data.drop_duplicates(['Name']).count()
print(data03)

# 出现次数最少的名字共有几个
c = len(names[names.Count == names.Count.min()])
print(c)

