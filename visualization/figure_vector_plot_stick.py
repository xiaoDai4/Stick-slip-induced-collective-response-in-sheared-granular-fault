# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:35:20 2022

@author: xiaod
"""
# first of all, import the sensor data
import matplotlib.pyplot as plt
import numpy as np
import math

#%% set parameters
index_ = 7900

individuals_ =    [int(i_) for i_ in range(286,2203)] 




x1_ = np.zeros(len(individuals_))
x2_ = np.zeros(len(individuals_))
u_ = np.zeros(len(individuals_))
v_ = np.zeros(len(individuals_))
count_ = 0
for i_ in individuals_:
    x1_[count_] = sensors_[i_].loc[index_, 'cx'] 
    x2_[count_] = sensors_[i_].loc[index_, 'cy'] 
    u_[count_] = sensors_[i_].loc[index_, 'vx'] 
    v_[count_] = sensors_[i_].loc[index_, 'vy']
    count_ += 1
u_ = u_ - np.mean(u_)
v_ = v_ - np.mean(v_)



plt.rc('font', family = 'Arial')
fig = plt.figure(figsize=(20, 2))    
plt.quiver(x1_, x2_, u_, v_,width = 0.001, scale = 0.8)
plt.axis('off')

plt.title('Stick, time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 20)


plt.tight_layout()
plt.savefig('vector_stick.svg', dpi=600, format='svg')
plt.show()

#%% plot the full velocity

index_ = 7900

individuals_ =    [int(i_) for i_ in range(286,2203)] 
threshold_ = 0.0005  # define the value to separate the large and small value
enlarge_factor_ = 10 # define the clip value



x1_ = np.zeros(len(individuals_))
x2_ = np.zeros(len(individuals_))
u_ = np.zeros(len(individuals_))
v_ = np.zeros(len(individuals_))
count_ = 0
for i_ in individuals_:
    x1_[count_] = sensors_[i_].loc[index_, 'cx'] 
    x2_[count_] = sensors_[i_].loc[index_, 'cy'] 
    u_[count_] = sensors_[i_].loc[index_, 'vx'] 
    v_[count_] = sensors_[i_].loc[index_, 'vy']
    count_ += 1
# scale the small velocity
for i_ in range(0, u_.shape[0]):
    # print(i_)
    if math.sqrt(u_[i_]**2 + v_[i_]**2) <= threshold_:
        u_[i_] = u_[i_] * enlarge_factor_
        v_[i_] = v_[i_] * enlarge_factor_

plt.rc('font', family = 'Arial')
fig = plt.figure(figsize=(20, 2))    
plt.quiver(x1_, x2_, u_, v_,width = 0.001, scale = 0.8)
plt.axis('off')

plt.title('Stick, time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 20)


plt.tight_layout()
plt.savefig('vector_stick_full_velocity.svg', dpi=600, format='svg')
plt.show()