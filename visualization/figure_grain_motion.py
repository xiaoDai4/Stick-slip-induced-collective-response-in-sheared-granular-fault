# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:34:51 2022

@author: xiaod
"""

#%% read data
import matplotlib.pyplot as plt

filename_ = open('list_vm_grain_.pkl', 'rb')
list_vm_grain_ = pickle.load(filename_)
print(list_vm_grain_)
filename_.close()

filename_ = open('list_vmx_grain_.pkl', 'rb')
list_vmx_grain_ = pickle.load(filename_)
print(list_vmx_grain_)
filename_.close()




#%% plot velocity

plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.size'] = 15
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_vm_grain_,\
         linewidth = 1, color = 'b')  




plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Average particle \nvelocity magnitude (mm/ms)', fontsize = 17)


plt.savefig('grain velocity.svg', dpi=600, format='svg')
plt.show()

#%% plot x velocity

plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_vmx_grain_,\
         linewidth = 1, color = 'b')  


plt.ylim([-0.004, 0.009])
y_tick_ = np.arange(-0.004, 0.009, 0.002)
plt.yticks(y_tick_)
  
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('$\\it{v_x}$$\\rm_{gm}$ (mm/ms)', fontsize = 17)


plt.savefig('grain x velocity.svg', dpi=600, format='svg')
plt.show()




