# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:13:55 2022

@author: xiaod
"""

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
index_ = int(7609)       # select the time moment
index1_ = int(7559)    # strat step
index2_ = int(7659)     # end step



initial_ = int(5e3)      # the initial step of the plate motion data

# friction


# plate velocity
 

plt.rc('font', family = 'Arial')

plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom', color = 'g')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
plt.tick_params(labelsize = 15)    
plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.ylim([-0.03, 0.03])
plt.xlim([10540, 10640])
plt.savefig('plate velocity large drop supplement 1.svg', dpi=600, format='svg')
plt.show()

#%% select the point in stick, large slip(main shock) and small slip.

# parameters
index_ = int(8671)       # select the time moment
index1_ = int(8651)    # strat step
index2_ = int(8751)     # end step



initial_ = int(5e3)      # the initial step of the plate motion data

# friction


# plate velocity
 

plt.rc('font', family = 'Arial')

plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom', color = 'g')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
plt.tick_params(labelsize = 15)    
plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.ylim([-0.015, 0.015])
plt.xlim([11630, 11730])
plt.xticks([11630, 11650, 11670, 11690, 11710, 11730])
plt.savefig('plate velocity large drop supplement 2.svg', dpi=600, format='svg')
plt.show()

#%% select the point in stick, large slip(main shock) and small slip.

# parameters
index_ = int(10857)       # select the time moment
index1_ = int(10807)    # strat step
index2_ = int(10907)     # end step



initial_ = int(5e3)      # the initial step of the plate motion data

# friction


# plate velocity
 

plt.rc('font', family = 'Arial')

plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom', color = 'g')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
plt.tick_params(labelsize = 15)    
plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.ylim([-0.015, 0.020])
plt.xlim([13785, 13885])
plt.xticks([13785, 13805, 13825, 13845, 13865, 13885])
plt.savefig('plate velocity large drop supplement 3.svg', dpi=600, format='svg')
plt.show()

#%% select the point in stick, large slip(main shock) and small slip.

# parameters
index_ = int(11887)       # select the time moment
index1_ = int(11857)    # strat step
index2_ = int(11957)     # end step



initial_ = int(5e3)      # the initial step of the plate motion data

# friction


# plate velocity
 

plt.rc('font', family = 'Arial')

plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom', color = 'g')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
plt.tick_params(labelsize = 15)    
plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.xlim([14834, 14934])
plt.xticks([14834, 14854, 14874, 14894, 14914, 14934])
plt.savefig('plate velocity large drop supplement 4.svg', dpi=600, format='svg')
plt.show()

#%% select the point in stick, large slip(main shock) and small slip.

# parameters
index_ = int(15351)       # select the time moment
index1_ = int(15301)    # strat step
index2_ = int(15401)     # end step



initial_ = int(5e3)      # the initial step of the plate motion data

# friction


# plate velocity
 

plt.rc('font', family = 'Arial')

plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom', color = 'g')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
plt.tick_params(labelsize = 15)      
plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.ylim([-0.015, 0.015])
plt.xlim([18274, 18374])
plt.xticks([18274, 18294, 18314, 18334, 18354, 18374])
plt.savefig('plate velocity large drop supplement 5.svg', dpi=600, format='svg')
plt.show()