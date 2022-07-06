'''
Author: WangJC 781424275@qq.com
Date: 2022-07-03 17:52:39
LastEditors: WangJC 781424275@qq.com
LastEditTime: 2022-07-06 19:34:30
FilePath: \pandas\pd_02.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import numpy as np

datas = pd.date_range('20220703',periods=7)
df = pd.DataFrame(np.arange(21).reshape(7,3),index=datas,columns=['a','e','f'])
print(df)

#? 选择 切片
print(df['a'],df.a)
print(df[0:3],df['2022-07-03':'2022-07-04'])


#?  loc  ****标签****所在位置[row_label,col_label]
print(df.loc['2022-07-03'])

print(df.loc[:,'a'])
print(df.loc['2022-07-04',['a','e']],'\n')

#? iloc 看****索引****位置 [row_label,col_label]
print(df.iloc[1,1],'\n')
print(df.iloc[2:3,:3])
print(df.iloc[[0,2,3],1:3],'\n')

#? ix 混合选择  
#! 报错，已弃用

# bool -> index 
print('**********')
print(df[df.a > 12])

