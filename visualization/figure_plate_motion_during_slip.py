# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:36:10 2022

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



#%% plot velocity small drop
fig = plt.figure(figsize=(2.5, 4))
index_ = int(8476)
index1_ = int(8.45e3)
index2_ = int(8.5e3)
initial_ = int(7e3)

plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_top_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Top plate', color = 'b')  

plt.plot(ConSV_PlateTopBeadMiddle_.loc[index1_:index2_, 'Time'],  \
         list_vmx_bottom_[index1_ - initial_:index2_ - initial_+1],\
         linewidth = 1, label = 'Bottom plate', color = 'g')
    
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_top_[index_ - initial_],\
              c = 'r', marker = '*')
plt.scatter(ConSV_PlateTopBeadMiddle_.loc[index_, 'Time'],  \
            list_vmx_bottom_[index_ - initial_],\
              c = 'r', marker = '*')
# plt.title('Small slip') 
plt.text( 11432, -0.004, 'Small slip')

plt.legend( frameon = False, fontsize = 13)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.xlim([11430, 11480])
plt.ylim([-0.005, 0.005])
plt.xticks([11430, 11455, 11480])

plt.savefig('plate velocity small drop.svg', dpi=600, format='svg')
plt.show()

#%% plot velocity large drop
fig = plt.figure(figsize=(2.5, 4))
index_ = int(8671)
index1_ = int(8.65e3)
index2_ = int(8.75e3)
initial_ = int(7e3)

plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
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
              c = 'r', marker = '*', )
# plt.title('Large slip')   
plt.text( 11660, -0.015, 'Large slip')  
plt.legend( frameon = False, fontsize = 13)    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Plate velocity (m/s)', fontsize = 17)
plt.ylim([-0.020, 0.020])
plt.xlim([11630, 11730])
plt.xticks([11630, 11680, 11730])
plt.savefig('plate velocity large drop.svg', dpi=600, format='svg')
plt.show()


