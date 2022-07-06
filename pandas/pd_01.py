'''
Author: WangJC 781424275@qq.com
Date: 2022-07-03 17:21:51
LastEditors: WangJC 781424275@qq.com
LastEditTime: 2022-07-06 19:24:51
FilePath: \pandas\pd_01.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import numpy as np

s = pd.Series([1,2,3,5,6])
print(s)
#! 创建pandas 两种方式  1数组 2键值对
#! pandas 类型 1Series 2DataFrame 3CSV文件

# DataFrame DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
# DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
#? pandas.DataFrame( data, index, columns, dtype, copy)
dates = pd.date_range('20220703',periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d']) 
print(df)

df2 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df2)

df3 = pd.DataFrame({'a':'132','b':'31312312','c':np.array([3]*4,dtype='int32')})
print(df3)

print(df3.index)  # 行
print(df3.columns)   #列
print(df3.values)  # 值
print(df3.describe())  # 方差 均值等
print(df3.T)  # 翻转
print(df3.sort_index(axis=1,ascending=False))  # 名称排列
print(df3.sort_values(by='a'))   # 值排列

datas = pd.date_range('20220701',periods=6)
df = pd.DataFrame(np.random.randn(6,3),index=datas,columns=['a','b','c'])
print(df)
df1 = pd.DataFrame(np.arange(12).reshape(4,3),index=['a','b','c','d'],columns=['王','建','成'])
print(df1)
print(df1.sort_index(axis=0,ascending=False),'\n')
print(df1.sort_index(axis=1,ascending=False),'\n')
print(df1.T,'\n')
print(df1.describe())

# Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型
#? pandas.Series( data, index, dtype, name, copy)
ss = pd.Series({'a':'1', 'b':'2', 'c':'3'})
print(ss)

# CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。
# CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。
csv = pd.read_csv()


