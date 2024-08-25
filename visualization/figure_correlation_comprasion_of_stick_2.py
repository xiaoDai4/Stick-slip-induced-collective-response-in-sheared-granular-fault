# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:15:23 2022

@author: xiaod
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:13:49 2022

@author: xiaod
"""
#%% imoort 
import pickle
import matplotlib.pyplot as plt

index1_ = 9700 #larger stiffness
index2_ = 9000 # smaller stifness
x_ = np.linspace(0,300,31) # set the corresponding distance

filename_ = open('pickledata/list_correlation_o_20220708.pkl', 'rb')
list_correlation_o_ = pickle.load(filename_)
print(list_correlation_o_)
filename_.close()


filename_ = open('pickledata/list_correlation_s_20220708.pkl', 'rb')
list_correlation_s_ = pickle.load(filename_)
print(list_correlation_s_)
filename_.close()

#%%
plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, list_correlation_o_[27], marker = 'o',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index1_,'Time'] + ', larger effective stiffness', \
         color = 'b')
plt.plot(x_, list_correlation_o_[20], marker = 's',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index2_,'Time'] + ', smaller effective stiffness', \
         color = 'g')
plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r', linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{ori}$)', fontsize = 17)
plt.tick_params(labelsize = 15)
plt.legend( frameon = False, fontsize = 12) 
plt.savefig('correlation of orintation comprasion 2.svg', dpi=600, format='svg')
plt.show()

#%%
plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, list_correlation_s_[27], marker = 'o',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index1_,'Time'] + ', larger effective stiffness', \
         color = 'b')
plt.plot(x_, list_correlation_s_[20], marker = 's',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index2_,'Time'] + ', smaller effective stiffness', \
         color = 'g')
plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r',linewidth = 1)
plt.axhline(0.1, linestyle = '--', color = 'r', linewidth = 1)
plt.axhline(-0.1, linestyle = '--', color = 'r', linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{mag}$)', fontsize = 17)
plt.tick_params(labelsize = 15)
plt.legend( frameon = False, fontsize = 12) 
plt.savefig('correlation of speed comprasion 2.svg', dpi=600, format='svg')
plt.show()