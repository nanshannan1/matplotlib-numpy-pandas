import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re

# 用于解决中文乱码问题
plt.rcParams["font.sans-serif"] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./nlp/labeledTrainData.tsv', sep='\t', escapechar='\\')
# print('记录数:{}'.format(len(df)))
# df.head()
# print(df['review'], '原始数据')
# print(df['review'][1], '原始数据')
# 使用beautifulSoup清洗数据，将数据中的html标签清除
# 1.创建beautifulSoup的对象
# df_01 = df['review'][1]
# print(df_01)
# df_02 = BeautifulSoup(df_01, 'html.parser')
# # df_03 = [s.extract() for s in df_02('script')]
# # 使用beautifulSoup获取文本
# print(df_02.get_text())
# # 将数据中的标点符号去掉
# df_03 = df_02.get_text()
# df_04 = df_03.replace(',', '').replace(".", "").replace('"', "")
# print(df_04)
#
# # 将文字转换为小写
# str_01 = df_04.lower().split(' ')
# print(str_01)


# 定义函数用来清洗数据
def clean_text(text):
    # 获取文本
    text = BeautifulSoup(text, "html.parser").get_text()
    # 去除文本中的特殊字符
    text = re.sub(r'[^a-zA-Z]', '', text)
    # 文字转换为小写的词
    # words = text.lower().split(' ')
    # return ' '.join(words)
    words = text.lower()
    return words


# 使用apply方法，使用上步的函数重新处理加载数据
df['clean_review'] = df.review.apply(clean_text)
print(df.head(1)['clean_review'])