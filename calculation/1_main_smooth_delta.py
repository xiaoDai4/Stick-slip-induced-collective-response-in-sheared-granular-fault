# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:42:56 2022

@author: xiaod
"""
"""
note for sensor data

0 - 285 sensor on the palte 
0, 2, 4, ... for bottom plate
1, 3, 5, ... for top plate  

286 -2202 sensor on the grain
"""
#%% 
# set work directory
import os
os.chdir('D:\\fault_sensor_data\\python_file')

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from read_data_ver2 import *  # notice the version of readdata
#%% 

#%%calculate_distance
def calculate_distance(individuals_, sensors_,index_):
    """
    individuals_: a list, store the sensor number we consider
    
    sensors_: store the information of sensors
    
    return distance_: 3 cloumns 0 grain1 1 grain2 2 distance 
    
    """
    #
    n_ = len(individuals_)
    # initial array to store distance
    # 3 cloumns 0 grain1 1 grain2 2 distance 
    distance_ = np.zeros([int(n_*(n_-1)/2),3])
    count_ = 0
    
    # loop to calculate distance
    for i_ in range(n_):
        for j_ in range(i_+1, n_):
            distance_[count_][0] = individuals_[i_]         
            distance_[count_][1] = individuals_[j_]   
            distance_[count_][2] = math.sqrt((sensors_[individuals_[i_]].loc[index_,'cx']-sensors_[individuals_[j_] ].loc[index_,'cx'])**2 \
            + (sensors_[individuals_[i_] ].loc[index_,'cy']-sensors_[individuals_[j_] ].loc[index_,'cy'])**2)
            count_ = count_ + 1
    return distance_
# individuals_ = [int(i_) for i_ in range(286,2203)] 
# distance_ = calculate_distance(individuals_, sensors_, 0)
#%%

#%% smooth delta
def smooth_delta(r_,a_):
    return 1/(a_ * math.sqrt(math.pi)) * math.exp(-r_**2 / a_**2)

# test_x_ = np.linspace(-200, 200,1000)
# test_y_ = np.zeros(1000)
# for i_ in range(1000):
#     test_y_[i_] = smooth_delta(test_x_[i_] ,10) 
    
# plt.plot(test_x_,test_y_)



#%%







#%% decentralization_v data
def decentralization_v(individuals_, sensors_, index_):
    """
    return df_: index represent the sensor_ numbers
    d_v in df_: decentralized v
    d_vx in df_: decentralized vx
    d_vy in df_: decentralized vy
    """
    # initial df'
    df_ = pd.DataFrame(columns = ['d_vx', 'd_vy', 'd_v'], index = individuals_)    
    # extract data
    for i_ in individuals_:
       df_.loc[i_,'vx']  = sensors_[i_].loc[index_,'vx']
       df_.loc[i_,'vy']  = sensors_[i_].loc[index_,'vy']
       # calculate module of v
       df_.loc[i_,'v'] = math.sqrt((sensors_[i_].loc[index_,'vx']) ** 2 + (sensors_[i_].loc[index_,'vy']) ** 2)
    # decentralize data
    mean_vx_ = df_['vx'].mean()
    mean_vy_ = df_['vy'].mean()
    mean_v_ = df_['v'].mean()
    df_['d_vx']  = df_['vx'] - mean_vx_
    df_['d_vy']  = df_['vy'] - mean_vy_
    df_['d_v']  = df_['v'] - mean_v_
    return df_

# sensors_dv_ = decentralization_v(individuals_, sensors_, 0)

#%% decentralization_vx data
def decentralization_vx(individuals_, sensors_, index_):
    """
    return df_: index represent the sensor_ numbers
    d_vx in df_: decentralized vx
    d_abs_vx in df_: decentralized vx
    """
    # initial df'
    df_ = pd.DataFrame(columns = ['d_vx', 'd_abs_vx'], index = individuals_)    
    # extract data
    for i_ in individuals_:
       df_.loc[i_,'vx']  = sensors_[i_].loc[index_,'vx']
       df_.loc[i_,'abs_vx']  = abs(sensors_[i_].loc[index_,'vx'])
       
    # decentralize data
    mean_vx_ = df_['vx'].mean()
    mean_abs_vx_ = df_['abs_vx'].mean()
    df_['d_vx']  = df_['vx'] - mean_vx_
    df_['d_abs_vx']  = df_['abs_vx'] - mean_abs_vx_
    return df_
# sensors_dvx_ = decentralization_vx(individuals_, sensors_, 0)

#%% decentralization_vy data
def decentralization_vy(individuals_, sensors_, index_):
    """
    return df_: index represent the sensor_ numbers
    d_vy in df_: decentralized vy
    d_abs_vy in df_: decentralized vy
    """
    # initial df'
    df_ = pd.DataFrame(columns = ['d_vy', 'd_abs_vy'], index = individuals_)    
    # extract data
    for i_ in individuals_:
       df_.loc[i_,'vy']  = sensors_[i_].loc[index_,'vy']
       df_.loc[i_,'abs_vy']  = abs(sensors_[i_].loc[index_,'vy'])
       
    # decentralize data
    mean_vy_ = df_['vy'].mean()
    mean_abs_vy_ = df_['abs_vy'].mean()
    df_['d_vy']  = df_['vy'] - mean_vy_
    df_['d_abs_vy']  = df_['abs_vy'] - mean_abs_vy_
    return df_
# sensors_dvy_ = decentralization_vy(individuals_, sensors_, 0)



#%%    calculate_correlation_v 
def calculate_correlation_v(individuals_, distance_, sensors_dv_, a_, interval_median_):
    """    
    a_: the parameter in smooth delta
    
    return correlation_o_: record the correlation of orientation in each interval
    return correlation_s_: record the correlation of magnitude in each interval
    """
    print('velocity:')    
    sum_uu_ = 0
    sum_s_ = 0
    sum_n_ = 0
    # calculate c0
    # mutual part
    for i_ in range(distance_.shape[0]):
        sum_uu_ = sum_uu_ + ( sensors_dv_.loc[int(distance_[i_, 0]), 'd_vx'] * sensors_dv_.loc[int(distance_[i_, 1]), 'd_vx'] + \
            sensors_dv_.loc[int(distance_[i_, 0]), 'd_vy'] * sensors_dv_.loc[int(distance_[i_, 1]), 'd_vy']) *  \
            smooth_delta(distance_[i_,2],a_)
        sum_s_ = sum_s_ + sensors_dv_.loc[int(distance_[i_, 0]), 'd_v'] * sensors_dv_.loc[int(distance_[i_, 1]), 'd_v']* \
            smooth_delta(distance_[i_,2],a_)
        sum_n_ = sum_n_ + smooth_delta(distance_[i_,2],a_)
    # self part
    for i_ in individuals_:
        sum_uu_ = sum_uu_ + (sensors_dv_.loc[i_, 'd_vx'] ** 2 + sensors_dv_.loc[i_, 'd_vy'] ** 2) * smooth_delta(0,a_)
        sum_s_ = sum_s_ + (sensors_dv_.loc[i_, 'd_v'] ** 2) * smooth_delta(0,a_)
        sum_n_ = sum_n_ + smooth_delta(0,a_)
    c_o0_ = sum_uu_ / sum_n_
    c_s0_ = sum_s_ / sum_n_
   
    # initial correlation_
    correlation_o_ = np.zeros(len(interval_median_))
    correlation_s_ = np.zeros(len(interval_median_))
    correlation_o_[0] = 1
    correlation_s_[0] = 1
    # print(correlation_o_)
    # print(correlation_s_)
    # # calculate
    count_ = 1
    for r_ in interval_median_[1:]: 
        print(r_)
        sum_uu_ = 0
        sum_s_ = 0
        sum_n_ = 0
        # mutual part
        for i_ in range(distance_.shape[0]):
            sum_uu_ = sum_uu_ + ( sensors_dv_.loc[int(distance_[i_, 0]), 'd_vx'] * sensors_dv_.loc[int(distance_[i_, 1]), 'd_vx'] + \
                sensors_dv_.loc[int(distance_[i_, 0]), 'd_vy'] * sensors_dv_.loc[int(distance_[i_, 1]), 'd_vy']) *  \
                smooth_delta(distance_[i_,2] - r_,a_)
            sum_s_ = sum_s_ + sensors_dv_.loc[int(distance_[i_, 0]), 'd_v'] * sensors_dv_.loc[int(distance_[i_, 1]), 'd_v']* \
                smooth_delta(distance_[i_,2] - r_,a_)
            sum_n_ = sum_n_ + smooth_delta(distance_[i_,2] - r_,a_)
        # self part
        for i_ in individuals_:
            sum_uu_ = sum_uu_ + (sensors_dv_.loc[i_, 'd_vx'] ** 2 + sensors_dv_.loc[i_, 'd_vy'] ** 2) * smooth_delta(0 - r_, a_)
            sum_s_ = sum_s_ + (sensors_dv_.loc[i_, 'd_v'] ** 2) * smooth_delta(0 - r_,a_)
            sum_n_ = sum_n_ + smooth_delta(0 - r_,a_)
        # print(sum_n_)
        correlation_o_[count_] = sum_uu_ / sum_n_ / c_o0_
        correlation_s_[count_] = sum_s_ / sum_n_ / c_s0_
        count_ += 1
    return correlation_o_, correlation_s_
    
# x_ = np.linspace(0,200,80)
# correlation_o_, correlation_s_ = calculate_correlation_v(individuals_, distance_, sensors_dv_,  5, x_)           

#%%
def calculate_correlation_vx(individuals_, distance_, sensors_dvx_, a_, interval_median_):
    """    
    a_: the parameter in smooth delta
    
    return correlation_o_: record the correlation of orientation in each interval
    return correlation_s_: record the correlation of magnitude in each interval
    """
    print('velocity x:')    
    sum_vx_ = 0
    sum_abs_vx_ = 0
    sum_n_ = 0
    # calculate c0
    # mutual part
    for i_ in range(distance_.shape[0]):
        sum_vx_ = sum_vx_ +  sensors_dvx_.loc[int(distance_[i_, 0]), 'd_vx'] * sensors_dvx_.loc[int(distance_[i_, 1]), 'd_vx'] *  \
            smooth_delta(distance_[i_,2],a_)
        sum_abs_vx_ = sum_abs_vx_ + sensors_dvx_.loc[int(distance_[i_, 0]), 'd_abs_vx'] * sensors_dvx_.loc[int(distance_[i_, 1]), 'd_abs_vx']* \
            smooth_delta(distance_[i_,2],a_)
        sum_n_ = sum_n_ + smooth_delta(distance_[i_,2],a_)
    # self part
    for i_ in individuals_:
        sum_vx_ = sum_vx_ + (sensors_dvx_.loc[i_, 'd_vx'] ** 2) * smooth_delta(0,a_)
        sum_abs_vx_ = sum_abs_vx_ + (sensors_dvx_.loc[i_, 'd_abs_vx'] ** 2) * smooth_delta(0,a_)
        sum_n_ = sum_n_ + smooth_delta(0,a_)
    c_vx0_ = sum_vx_ / sum_n_
    c_abs_vx0_ = sum_abs_vx_ / sum_n_
   
    # initial correlation_
    correlation_vx_ = np.zeros(len(interval_median_))
    correlation_abs_vx_ = np.zeros(len(interval_median_))
    correlation_vx_[0] = 1
    correlation_abs_vx_[0] = 1
    # print(correlation_o_)
    # print(correlation_s_)
    # # calculate
    count_ = 1
    for r_ in interval_median_[1:]: 
        print(r_)
        sum_vx_ = 0
        sum_abs_vx_ = 0
        sum_n_ = 0
        # mutual part
        for i_ in range(distance_.shape[0]):
            sum_vx_ = sum_vx_ +  sensors_dvx_.loc[int(distance_[i_, 0]), 'd_vx'] * sensors_dvx_.loc[int(distance_[i_, 1]), 'd_vx']  *  \
                smooth_delta(distance_[i_,2] - r_,a_)
            sum_abs_vx_ = sum_abs_vx_ + sensors_dvx_.loc[int(distance_[i_, 0]), 'd_abs_vx'] * sensors_dvx_.loc[int(distance_[i_, 1]), 'd_abs_vx']* \
                smooth_delta(distance_[i_,2] - r_,a_)
            sum_n_ = sum_n_ + smooth_delta(distance_[i_,2] - r_,a_)
        # self part
        for i_ in individuals_:
            sum_vx_ = sum_vx_ + (sensors_dvx_.loc[i_, 'd_vx'] ** 2 ) * smooth_delta(0 - r_, a_)
            sum_abs_vx_ = sum_abs_vx_ + (sensors_dvx_.loc[i_, 'd_abs_vx'] ** 2) * smooth_delta(0 - r_,a_)
            sum_n_ = sum_n_ + smooth_delta(0 - r_,a_)
        # print(sum_n_)
        correlation_vx_[count_] = sum_vx_ / sum_n_ / c_vx0_
        correlation_abs_vx_[count_] = sum_abs_vx_ / sum_n_ / c_abs_vx0_
        count_ += 1
    return correlation_vx_, correlation_abs_vx_
    
# x_ = np.linspace(0,200,21)
# correlation_vx_, correlation_abs_vx_ = calculate_correlation_vx(individuals_, distance_, sensors_dvx_,  10, x_)           




#%%    
#%%
def calculate_correlation_vy(individuals_, distance_, sensors_dvy_, a_, interval_median_):
    """    
    a_: the parameter in smooth delta
    
    return correlation_o_: record the correlation of orientation in each interval
    return correlation_s_: record the correlation of magnitude in each interval
    """
    print('velocity y:')    
    sum_vy_ = 0
    sum_abs_vy_ = 0
    sum_n_ = 0
    # calculate c0
    # mutual part
    for i_ in range(distance_.shape[0]):
        sum_vy_ = sum_vy_ +  sensors_dvy_.loc[int(distance_[i_, 0]), 'd_vy'] * sensors_dvy_.loc[int(distance_[i_, 1]), 'd_vy'] *  \
            smooth_delta(distance_[i_,2],a_)
        sum_abs_vy_ = sum_abs_vy_ + sensors_dvy_.loc[int(distance_[i_, 0]), 'd_abs_vy'] * sensors_dvy_.loc[int(distance_[i_, 1]), 'd_abs_vy']* \
            smooth_delta(distance_[i_,2],a_)
        sum_n_ = sum_n_ + smooth_delta(distance_[i_,2],a_)
    # self part
    for i_ in individuals_:
        sum_vy_ = sum_vy_ + (sensors_dvy_.loc[i_, 'd_vy'] ** 2) * smooth_delta(0,a_)
        sum_abs_vy_ = sum_abs_vy_ + (sensors_dvy_.loc[i_, 'd_abs_vy'] ** 2) * smooth_delta(0,a_)
        sum_n_ = sum_n_ + smooth_delta(0,a_)
    c_vy0_ = sum_vy_ / sum_n_
    c_abs_vy0_ = sum_abs_vy_ / sum_n_
   
    # initial correlation_
    correlation_vy_ = np.zeros(len(interval_median_))
    correlation_abs_vy_ = np.zeros(len(interval_median_))
    correlation_vy_[0] = 1
    correlation_abs_vy_[0] = 1
    # print(correlation_o_)
    # print(correlation_s_)
    # # calculate
    count_ = 1
    for r_ in interval_median_[1:]: 
        print(r_)
        sum_vy_ = 0
        sum_abs_vy_ = 0
        sum_n_ = 0
        # mutual part
        for i_ in range(distance_.shape[0]):
            sum_vy_ = sum_vy_ +  sensors_dvy_.loc[int(distance_[i_, 0]), 'd_vy'] * sensors_dvy_.loc[int(distance_[i_, 1]), 'd_vy']  *  \
                smooth_delta(distance_[i_,2] - r_,a_)
            sum_abs_vy_ = sum_abs_vy_ + sensors_dvy_.loc[int(distance_[i_, 0]), 'd_abs_vy'] * sensors_dvy_.loc[int(distance_[i_, 1]), 'd_abs_vy']* \
                smooth_delta(distance_[i_,2] - r_,a_)
            sum_n_ = sum_n_ + smooth_delta(distance_[i_,2] - r_,a_)
        # self part
        for i_ in individuals_:
            sum_vy_ = sum_vy_ + (sensors_dvy_.loc[i_, 'd_vy'] ** 2 ) * smooth_delta(0 - r_, a_)
            sum_abs_vy_ = sum_abs_vy_ + (sensors_dvy_.loc[i_, 'd_abs_vy'] ** 2) * smooth_delta(0 - r_,a_)
            sum_n_ = sum_n_ + smooth_delta(0 - r_,a_)
        # print(sum_n_)
        correlation_vy_[count_] = sum_vy_ / sum_n_ / c_vy0_
        correlation_abs_vy_[count_] = sum_abs_vy_ / sum_n_ / c_abs_vy0_
        count_ += 1
    return correlation_vy_, correlation_abs_vy_
    
# x_ = np.linspace(0,200,21)
# correlation_vy_, correlation_abs_vy_ = calculate_correlation_vy(individuals_, distance_, sensors_dvy_,  10, x_)        


#%%



#%% main
#%% one step v
individuals_ = [int(i_) for i_ in range(286,2203)] 
distance_ = calculate_distance(individuals_, sensors_, 8671)
sensors_dv_ = decentralization_v(individuals_, sensors_, 8671)
x_ = np.linspace(0,300,31)
correlation_o_, correlation_s_ = calculate_correlation_v(individuals_, distance_, sensors_dv_,  10, x_)           

#%% one step vx
individuals_ = [int(i_) for i_ in range(286,2203)] 
distance_ = calculate_distance(individuals_, sensors_, 14700)
sensors_dvx_ = decentralization_vx(individuals_, sensors_, 14700)
x_ = np.linspace(0,200,20)
correlation_vx_, correlation_abs_vx_ = calculate_correlation_vx(individuals_, distance_, sensors_dvx_,  5, x_)           

#%% one step vy
individuals_ = [int(i_) for i_ in range(286,2203)] 
distance_ = calculate_distance(individuals_, sensors_, 14700)
sensors_dvy_ = decentralization_vy(individuals_, sensors_, 14700)
x_ = np.linspace(0,200,20)
correlation_vy_, correlation_abs_vy_ = calculate_correlation_vy(individuals_, distance_, sensors_dvy_,  5, x_)           


#%% a period v
individuals_ = [int(i_) for i_ in range(286,2203)] 
x_ = np.linspace(0,300,31)
initial_index_ = 8450
stop_index_ = 8500
step_ =  1
a_ = 10 # smooth delta's parameter
index_ = initial_index_ # the current index in cycle
list_correlation_o_ = [] # store corelation in each step
list_correlation_s_ = []
while index_ <= stop_index_:
    # calculation
    distance_ = calculate_distance(individuals_, sensors_, index_)
    sensors_dv_ = decentralization_v(individuals_, sensors_, index_)
    correlation_o_, correlation_s_ = calculate_correlation_v(individuals_, distance_, sensors_dv_,  a_, x_) 
    # store data
    list_correlation_o_.append(correlation_o_)
    list_correlation_s_.append(correlation_s_)
    # update index_
    print('index step = %f' % index_)
    index_ += step_
print('calculation done')
#%%

#%% a period vx
individuals_ = [int(i_) for i_ in range(286,2203)] 
x_ = np.linspace(0,200,20)
initial_index_ = 10000
stop_index_ = 13000
step_ =  100
a_ = 10 # smooth delta's parameter
index_ = initial_index_ # the current index in cycle
list_correlation_vx_ = [] # store corelation in each step
list_correlation_abs_vx_ = []
while index_ <= stop_index_:
    # calculation
    distance_ = calculate_distance(individuals_, sensors_, index_)
    sensors_dvx_ = decentralization_vx(individuals_, sensors_, index_)
    correlation_vx_, correlation_abs_vx_ = calculate_correlation_vx(individuals_, distance_, sensors_dvx_,  a_, x_) 
    # store data
    list_correlation_vx_.append(correlation_vx_)
    list_correlation_abs_vx_.append(correlation_abs_vx_)
    # update index_
    print('index step = %f' % index_)
    index_ += step_
print('calculation done')

#%%

#%% a period vy
individuals_ = [int(i_) for i_ in range(286,2203)] 
x_ = np.linspace(0,200,20)
initial_index_ = 10000
stop_index_ = 13000
step_ =  100
a_ = 10 # smooth delta's parameter
index_ = initial_index_ # the current index in cycle
list_correlation_vy_ = [] # store corelation in each step
list_correlation_abs_vy_ = []
while index_ <= stop_index_:
    # calculation
    distance_ = calculate_distance(individuals_, sensors_, index_)
    sensors_dvy_ = decentralization_vy(individuals_, sensors_, index_)
    correlation_vy_, correlation_abs_vy_ = calculate_correlation_vy(individuals_, distance_, sensors_dvy_,  a_, x_) 
    # store data
    list_correlation_vy_.append(correlation_vy_)
    list_correlation_abs_vy_.append(correlation_abs_vy_)
    # update index_
    print('index step = %f' % index_)
    index_ += step_
print('calculation done')

