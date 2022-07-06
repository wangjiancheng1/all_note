'''
Author: WangJC 781424275@qq.com
Date: 2022-07-03 16:05:09
LastEditors: WangJC 781424275@qq.com
LastEditTime: 2022-07-06 20:11:29
FilePath: \RL\Q_learning.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as np
import pandas as pd
import time

np.random.seed(2)

N_STATES = 6     # 一维世界的长度
ACTIONS = ['left', 'right']    # 可能动作
EPSILON = 0.9   # 动作选择概率  存在一定几率选择其他动作
ALPHA = 0.1     # 学习比率
LAMBDA = 0.9    # 未来奖励衰减度
MAX_EPISODES =  13      # 最大玩回合数
FRESH_TIME = 0.3    # 每步花的时间


# 建立Q表
def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # q_table 初始值
        columns=actions,  # actions's name
    )
    print(table)
    return table




# 动作选择  
def choose_action(state, q_table):
    state_actions = q_table.iloc[state,:]  # 基于索引选择动作值
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  #! 当随机值大于EPSILON(0.9)值 and 该状态动作Qzhi 均为0时
        action_name = np.random.choice(ACTIONS) 
    else:
        action_name = state_actions.argmax() 
        return action_name    
#? 注1
'''
1. 函数原型:  numpy.random.uniform(low=0,high=1,size=(0)) #! 参数缺省   low 下采样阈值  high 上采样阈值  size生成大小 元组()

功能:从一个均匀分布[low,high)中随机采样,注意定义域是左闭右开,即包含low,不包含high.

参数介绍:
    
    low: 采样下界,float类型,默认值为0:
    high: 采样上界,float类型,默认值为1:
    size: 输出样本数目,为int或元组(tuple)类型,例如,size=(m,n,k), 则输出m*n*k个样本,缺省时输出1个值。

返回值:ndarray类型,其形状和参数size中描述一致。

这里顺便说下ndarray类型,表示一个N维数组对象,其有一个shape(表维度大小)和dtype(说明数组数据类型的对象),使用zeros和ones函数可以创建数据全0或全1的数组,原型:

    numpy.ones(shape,dtype=None,order='C'),
其中,shape表数组形状(m*n),dtype表类型,order表是以C还是fortran形式存放数据。

2. 类似uniform,还有以下随机数产生函数:

    a. randint: 原型:numpy.random.randint(low, high=None, size=None, dtype='l'),产生随机整数:
    b. random_integers: 原型: numpy.random.random_integers(low, high=None, size=None),在闭区间上产生随机整数:
    c. random_sample: 原型: numpy.random.random_sample(size=None),在[0.0,1.0)上随机采样:
    d. random: 原型: numpy.random.random(size=None),和random_sample一样,是random_sample的别名:
    e. rand: 原型: numpy.random.rand(d0, d1, ..., dn),产生d0 - d1 - ... - dn形状的在[0,1)上均匀分布的float型数。
    f. randn: 原型:numpy.random.randn(d0,d1,...,dn),产生d0 - d1 - ... - dn形状的标准正态分布的float型数。
'''
#? 注2
# argmax(axis=0)   #! 缺省参数  默认为0 列| 1 行 -> 返回索引数
# 返回的是最大数的索引.argmax有一个参数axis,默认是0,表示每一列的最大值的索引 axis=1表示每一行的最大值的索引

# 环境反馈
def get_env_feedback(S, A):
        # This is how agent will interact with the environment 
    if A == 'right':  # move right 
        if S == N_STATES - 2: # terminate 
            S_= 'terminal'
            R = 1 
        else:
            S_=S+ 1 
            R = 0
    else:    # move left 
        R = 0
        if S == 0:
            S_ = S # reach the wall 
        else:
            S_ = S-1 
    return S_, R


def update_env(S, episode, step_counter):
    # This is how environment be updated
    env_list = ['-']*(N_STATES-1) + ['T']  # '------T'
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                                           ', end='')
    else:
        env_list[S]='o'
        interaction =''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range (MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S, q_table)
            S_, R= get_env_feedback(S, A) # take action & get ne?
            q_predict = q_table.loc[S, A]
            if S_!= 'terminal':
                # loc基于标签
                q_target =R+ LAMBDA * q_table.loc[S_ ,:].max()
            else:
                q_target =R
                is_terminated = True
            
            q_table.iloc[S, A]+= ALPHA * (q_target - q_predict)   # update
            S = S_   # move to next state
            update_env(S, episode, step_counter+1)
            step_counter += 1
    return q_table


if __name__ == '__main__': 
    q_table = rl()
    print('\r\nQ_TABLE:\n')
    print(q_table)