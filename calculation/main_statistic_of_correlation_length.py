# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:51:02 2022

@author: xiaod
"""

#%% import packages and data
import pickle
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
os.chdir('D:\\fault_sensor_data\\python_file')
from read_data_ver2 import *  # notice the version of readdata

# read pickle data
filename_ = open('pickledata\\list_vmx_top_all.pkl', 'rb')
list_vmx_top_ = pickle.load(filename_)
filename_.close()

filename_ = open('pickledata\\list_vmx_bottom_all.pkl', 'rb')
list_vmx_bottom_ = pickle.load(filename_)
filename_.close()

#%% select the point in stick, large slip(main shock) and small slip.

# parameters
index_ = int(13.749e3)       # select the time moment
index1_ = int(13e3)    # strat step
index2_ = int(14e3)     # end step



initial_ = int(5e3)      # the initial step of the plate motion data

# friction

plt.rc('font', family = 'Arial')
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         (ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_,'fx'] - ConSV_PlateTopBeadMiddle_.loc[index1_:index2_,'fx'])/ \
         (ConSV_PlateTopBeadMiddle_.loc[index1_:index2_,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_,'fy']),\
         linewidth = 1)
plt.xlabel('Time(ms)')
plt.ylabel('Friction coefficient')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.tight_layout()
# plt.savefig('friction coefficient.svg', dpi=600, format='svg')
plt.show()

# plate velocity
 

plt.rc('font', family = 'Arial')

plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top plate')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom plate')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
    
plt.legend( frameon = False )    
plt.xlabel('Time(ms)')
plt.ylabel('Velocity(mm/ms)')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# plt.savefig('plate velocity large drop supplement 5.svg', dpi=600, format='svg')
plt.show()

#%% record the step
large_drop_main_ = [ 7609, 8671, 10857, 11887, 15351]

large_drop_fore_ = [ 7598, 7602, 10823, 10835, 10845, 15337]

large_drop_after_ = [7620, 7627, 8705, 8717, 10864, 10877, 10890, 15357]

between_shocks_ = [ 8686, 8712, 7604, 10853, 10884, 15330, 15344]

small_drop_ = [ 8476, 8774, 8517, 9426, 5180, 6636, 11227, 11333, 13190, 13749]

stick_ = [8055, 8400, 9100, 9790, 5250, 6620, 11736, 11050, 13990, 13350]

#%% calculate their correlation
individuals_ = [int(i_) for i_ in range(286,2203)] # the number of grain
x_ = np.linspace(0,300,31)  
a_ = 10
correlation_o_large_main_, correlation_s_large_main_ = [], []
correlation_o_large_fore_, correlation_s_large_fore_ = [], []
correlation_o_large_after_, correlation_s_large_after_ = [], []
correlation_o_between_shocks_, correlation_s_between_shocks_ = [], []
correlation_o_small_, correlation_s_small_ = [], []
correlation_o_stick_, correlation_s_stick_ = [], []

for index_ in  large_drop_main_:
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    correlation_o_large_main_.append(correlation_o_)
    correlation_s_large_main_.append(correlation_s_)
    print(index_)
    
for index_ in  large_drop_fore_:
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    correlation_o_large_fore_.append(correlation_o_)
    correlation_s_large_fore_.append(correlation_s_)
    print(index_)
    
for index_ in  large_drop_after_:
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    correlation_o_large_after_.append(correlation_o_)
    correlation_s_large_after_.append(correlation_s_)
    print(index_)
    
for index_ in between_shocks_:
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    correlation_o_between_shocks_.append(correlation_o_)
    correlation_s_between_shocks_.append(correlation_s_)
    print(index_)

for index_ in small_drop_:
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    correlation_o_small_.append(correlation_o_)
    correlation_s_small_.append(correlation_s_)
    print(index_)
    
for index_ in stick_:
    correlation_o_, correlation_s_ = calculate_a_step(sensors_ ,individuals_, x_, index_, a_)
    correlation_o_stick_.append(correlation_o_)
    correlation_s_stick_.append(correlation_s_)
    print(index_)
#%% save data
with open('pickledata\\correlation_of_different_stage.pkl','wb') as f_:
    pickle.dump(correlation_o_large_main_, f_)
    pickle.dump(correlation_s_large_main_, f_)
    pickle.dump(correlation_o_large_fore_, f_)
    pickle.dump(correlation_s_large_fore_, f_)
    pickle.dump(correlation_o_large_after_, f_)
    pickle.dump(correlation_s_large_after_, f_)
    pickle.dump(correlation_o_between_shocks_, f_)
    pickle.dump(correlation_s_between_shocks_, f_)
    pickle.dump(correlation_o_small_, f_)
    pickle.dump(correlation_s_small_, f_)
    pickle.dump(correlation_o_stick_, f_)
    pickle.dump(correlation_s_stick_, f_)




