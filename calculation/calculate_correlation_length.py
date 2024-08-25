# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:10:51 2022

@author: xiaod
"""
import math
import numpy as np
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

def calculate_a_period(individuals_, x_, initial_index_, stop_index_, step_, a_):
    '''

    Parameters
    ----------
    individuals_ : list
        DESCRIPTION: the number of grains
    x_ : np array
        DESCRIPTION: the distance array
    initial_index_ : int
        DESCRIPTION: 
    stop_index_ : int
        DESCRIPTION.
    step_ : int
        DESCRIPTION.
    a_ : float
        DESCRIPTION: parameter of smooth delta

    Returns
    -------
    list_correlation_o_, 
    
    list_correlation_s_

    '''
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
    return list_correlation_o_, list_correlation_s_
    
#%% test
if __name__ == '__main__':
    individuals_ = [int(i_) for i_ in range(286,2203)] 
    x_ = np.linspace(0,300,31)
    initial_index_ = 8450
    stop_index_ = 8500
    step_ =  1
    a_ = 10 # smooth delta's parameter
    list_correlation_o_, list_correlation_s_ = calculate_a_period(individuals_, x_, initial_index_, stop_index_, step_, a_)

#%%    

def calculate_a_step(sensors_ ,individuals_, x_, index_, a_):
    '''
    

    Parameters
    ----------
    individuals_ : list
        DESCRIPTION: the number of grains
    x_ : np array
        DESCRIPTION: the distance array
    index_ : int
        DESCRIPTION.
    a_ : float
        DESCRIPTION: the parameter of smooth delta

    Returns
    -------
    correlation_o_ : TYPE
        DESCRIPTION.
    correlation_s_ : TYPE
        DESCRIPTION.

    '''
    distance_ = calculate_distance(individuals_, sensors_, index_)
    sensors_dv_ = decentralization_v(individuals_, sensors_, index_)
    correlation_o_, correlation_s_ = calculate_correlation_v(individuals_, distance_, sensors_dv_,  a_, x_)
    return correlation_o_, correlation_s_           
#%% test
individuals_ = [int(i_) for i_ in range(286,2203)] 
x_ = np.linspace(0,300,31)
a_ = 10
index_ = 8500
if __name__ == '__main__':
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    
    
    
#%% calculate correlation length
def calculate_correlation_length(correlation_, a_, cut_):
    '''
    parameters:
        correlation_: the corelation in each distance 
        a_: the interval
        cut_: the threshold

    Returns
    -------
    None.
    correlation_lengths_: a one dimensional array of correlation lengths
    
    '''
    correlation_lengths_ =  np.zeros(len(correlation_))
    # print(correlation_lengths_)
    count_ = 0
    for each_ in correlation_:
        for i_ in range(len(each_)):
            if each_[i_] <= cut_:
                record_ = i_ - 1   # record the step before reach the cut_
                r_ = (each_[record_] - cut_) / (each_[record_] - each_[i_])                
                correlation_lengths_[count_] = (record_ + r_) *a_
                break
        count_ += 1
    return correlation_lengths_

a_ = 10    
cut_ = 1/math.exp(1)
if __name__ == '__main__':
    correlation_lengths_ = calculate_correlation_length(correlation_o_small_, a_, cut_)
        
#%% calculate correlation strength
def calculate_correlation_strength(correlation_, a_):
    '''
    parameters:
        correlation_: the corelation in each distance 
        a_: the interval

    Returns
    -------
    None.
    correlation_strength_: a one dimensional array of correlation strength
    
    '''
    correlation_strengths_ =  np.zeros(len(correlation_))
    
    # print(correlation_strengths_)
    count_ = 0
    for each_ in correlation_:
        int_ = 0  # record the intergration
        for i_ in range(len(each_)):
            int_ +=abs(each_[i_])
        correlation_strengths_[count_] = int_ - 0.5 * each_[0] - 0.5*each_[len(each_) - 1]
        count_ += 1
    return correlation_strengths_
    
a_ = 10    
if __name__ == '__main__':
    correlation_strengths_ = calculate_correlation_strength(correlation_o_stick_, a_)