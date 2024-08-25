# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:43:37 2022

@author: xiaod
"""
#%% read data
import pickle
import matplotlib.pyplot as plt

filename_ = open('list_vmx_bottom_.pkl', 'rb')
list_vmx_bottom_ = pickle.load(filename_)
print(list_vmx_bottom_)
filename_.close()

filename_ = open('list_vmx_top_.pkl', 'rb')
list_vmx_top_ = pickle.load(filename_)
print(list_vmx_top_)
filename_.close()

filename_ = open('list_cmx_bottom_.pkl', 'rb')
list_cmx_bottom_ = pickle.load(filename_)
print(list_cmx_bottom_)
filename_.close()

filename_ = open('list_cmx_top_.pkl', 'rb')
list_cmx_top_ = pickle.load(filename_)
print(list_cmx_top_)
filename_.close()



#%% plot velocity

plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_vmx_top_,\
         linewidth = 1, label = 'Top', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_vmx_bottom_,\
         linewidth = 1, label = 'Bottom', color = 'g')

plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.ylim([-0.03, 0.03])
plt.xlim([10000, 14000])

plt.savefig('plate velocity.svg', dpi=600, format='svg')
plt.show()

#%% plot coodinate

plt.rc('font', family = 'Arial')

# initial 
base_t_ = list_cmx_top_[0]
base_b_ = list_cmx_bottom_[0]
v_load_ = 5e-4  
cx_load_point_ = []
cx_fixed_ = []
for i_ in range(len(list_cmx_top_)):
    list_cmx_top_[i_] = list_cmx_top_[i_] - base_t_
    list_cmx_bottom_[i_] = list_cmx_bottom_[i_] - base_b_
    cx_load_point_.append(v_load_ * i_)
    cx_fixed_.append(0)
# plot
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_cmx_top_,\
         linewidth = 1, label = 'Top plate')  


plt.plot(ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_cmx_bottom_,\
         linewidth = 1, label = 'Bottom plate')    
    
plt.plot(ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         cx_load_point_,\
         linewidth = 1, label = 'Load point', linestyle = '--')

plt.plot(ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         cx_fixed_,\
         linewidth = 1, label = 'Fixed', linestyle = '--')
    
plt.legend( frameon = False, fontsize = 15)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Average plate coordinate (mm)', fontsize = 17)


plt.savefig('plate coordinate.svg', dpi=600, format='svg')
plt.show()



