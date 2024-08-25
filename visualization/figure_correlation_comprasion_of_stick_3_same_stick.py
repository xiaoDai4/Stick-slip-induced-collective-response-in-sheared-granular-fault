# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:11:35 2022

@author: xiaod
"""


#%% imoort 
import pickle
import matplotlib.pyplot as plt

index1_ = 7800 #larger stiffness
index2_ = 8000 # smaller stifness
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
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, list_correlation_o_[8], marker = 'o',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index1_,'Time'] , \
         color = 'b')
plt.plot(x_, list_correlation_o_[10], marker = 's',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index2_,'Time'] , \
         color = 'g')
plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r', linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{ori}$)', fontsize = 17)

plt.legend( frameon = False, fontsize = 15) 
plt.savefig('correlation of orintation comprasion 3 similiar stifness.svg', dpi=600, format='svg')
plt.show()

#%%
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, list_correlation_s_[8], marker = 'o',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index1_,'Time'] , \
         color = 'b')
plt.plot(x_, list_correlation_s_[10], marker = 's',markerfacecolor = 'w', linewidth = 1, \
         label = 'Time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index2_,'Time'] , \
         color = 'g')
plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r',linewidth = 1)
plt.axhline(0.1, linestyle = '--', color = 'r', linewidth = 1)
plt.axhline(-0.1, linestyle = '--', color = 'r', linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{mag}$)', fontsize = 17)

plt.legend( frameon = False, fontsize = 15) 
plt.savefig('correlation of speed comprasion 3 similiar stiffness.svg ', dpi=600, format='svg')
plt.show()