# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:20:04 2022

@author: xiaod
"""
# first of all, import the sensor data
import matplotlib.pyplot as plt
#%% 
fig = plt.figure(figsize=(12, 4))
plt.rcParams['font.size'] = 15
plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[5e3:2e4, 'Time'],  \
         (ConSV_PlateBottomBeadMiddle_.loc[5e3:2e4,'fx'] - ConSV_PlateTopBeadMiddle_.loc[5e3:2e4,'fx'])/ \
         (ConSV_PlateTopBeadMiddle_.loc[5e3:2e4,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[5e3:2e4,'fy']),\
         linewidth = 1, color = 'b')
plt.xlim([8000, 23000])
plt.ylim([0.3, 0.6])
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Friction coefficient', fontsize = 17)
plt.tight_layout()
plt.savefig('friction coefficient.svg', dpi=600, format='svg')
plt.show()


#%% show all the friction coefficient
# fig = plt.figure(figsize=(6, 2))
# plt.rcParams['font.size'] = 12
# plt.rc('font', family = 'Arial')
# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
# plt.plot(ConSV_PlateBottomBeadMiddle_.loc[0:2e4, 'Time'],  \
#          (ConSV_PlateBottomBeadMiddle_.loc[0:2e4,'fx'] - ConSV_PlateTopBeadMiddle_.loc[0:2e4,'fx'])/ \
#          (ConSV_PlateTopBeadMiddle_.loc[0:2e4,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[0:2e4,'fy']),\
#          linewidth = 1)
# plt.xlabel('Time (ms)', fontsize = 13)
# plt.ylabel('Friction coefficient', fontsize = 13)
# plt.tight_layout()
# plt.savefig('friction coefficient all.svg', dpi=600, format='svg')
# plt.show()





#%% plot the area we focus on
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4, 'Time'],  \
         (ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4,'fx'] - ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4,'fx'])/ \
         (ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4,'fy']),\
         linewidth = 1, color = 'b')
    
plt.xlabel('Time (ms)', fontsize = 17)
plt.ylabel('Friction coefficient', fontsize = 17)
plt.xlim([10000, 14000])
plt.ylim([0.35, 0.55])
plt.savefig('friction coefficient inset.svg', dpi=600, format='svg')
plt.show()

