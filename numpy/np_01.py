'''
Author: WangJC 781424275@qq.com
Date: 2022-07-06 20:15:22
LastEditors: WangJC 781424275@qq.com
LastEditTime: 2022-07-06 20:28:58
FilePath: \numpy\np_01.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AEnp

'''
import numpy as np

# 创建一个数组
#? 1 array[[array_obj]] 
l1 = np.array([[1,2,3],[3,2,4]])
print(l1,'\n')

#? 2 zeros((shape_like))    ones((shape_like))
l2 = np.zeros((3,3))
print(l2,'\n')

l2 = np.ones((3,3))
print(l2,'\n')

#? 3 arange().reshape(shape_like)
l3 = np.arange(12).reshape(3,4) 
print(l3,'\n')

l3 = np.arange(2,18,2,dtype=np.int32)
print(l3,'\n')

