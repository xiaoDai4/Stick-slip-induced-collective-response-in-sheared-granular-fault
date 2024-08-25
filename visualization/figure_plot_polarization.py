# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:30:57 2022

@author: xiaod
"""
#%% read data
import pickle
import matplotlib.pyplot as plt

filename_ = open('list_phi_.pkl', 'rb')
list_phi_ = pickle.load(filename_)
print(list_phi_)
filename_.close()


#%% plot
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         list_phi_,\
         linewidth = 1, color = 'b')
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Polarization ($\\Phi$)', fontsize = 17)
plt.ylim([0, 0.9])
plt.xlim([10000, 14000])
y_tick_ = np.arange(0, 1, 0.1)
plt.yticks(y_tick_)
plt.savefig('polarization.svg', dpi=600, format='svg')
plt.show()


