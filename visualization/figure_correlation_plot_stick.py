# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 13:59:51 2022

@author: xiaod
"""
#%% imoort 
import pickle
import matplotlib.pyplot as plt

index_ = 7900
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
plt.plot(x_, list_correlation_o_[9], marker = 'o',markerfacecolor = 'w', linewidth = 1, color = 'b')

plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r', linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{ori}$)', fontsize = 17)
plt.text(80, 0.9, 'Stick, time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])
# plt.title('Stick, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])
plt.savefig('correlation of orintation.svg', dpi=600, format='svg', linewidth = 1)
plt.show()

#%%
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, list_correlation_s_[9], marker = 'o', markerfacecolor = 'w', linewidth = 1, color = 'b')

plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r',linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{mag}$)', fontsize = 17)
plt.text(80, 0.9, 'Stick, time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])
# plt.title('Stick, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])
plt.savefig('correlation of speed.svg', dpi=600, format='svg')
plt.show()

