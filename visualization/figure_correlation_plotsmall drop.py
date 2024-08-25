# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:29:21 2022

@author: xiaod
"""

#%% imoort 
import pickle
import matplotlib.pyplot as plt

index_ = 8476
x_ = np.linspace(0,300,31) # set the corresponding distance

filename_ = open('pickledata/list_correlation_o_small_drop.pkl', 'rb')
list_correlation_o_ = pickle.load(filename_)
correlation_o_ = list_correlation_o_[26]
print(correlation_o_)
filename_.close()


filename_ = open('pickledata/list_correlation_s_small_drop.pkl', 'rb')
list_correlation_s_ = pickle.load(filename_)
correlation_s_ = list_correlation_s_[26]
print(correlation_s_)
filename_.close()

#%%
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, correlation_o_, marker = 'o',markerfacecolor = 'w', linewidth = 1, color = 'b')

plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r', linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{ori}$)', fontsize = 17)
plt.text(80, 0.9, 'Small slip, time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])

# plt.title('Small slip, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])
plt.savefig('correlation of orintation small drop.svg', dpi=600, format='svg', linewidth = 1)
plt.show()

#%%
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 15
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.plot(x_, correlation_s_, marker = 'o', markerfacecolor = 'w', linewidth = 1, color = 'b')

plt.ylim(-0.6,1.1)
plt.axhline(0, linestyle = '--', color = 'r',linewidth = 1)
plt.xlabel('$\\mathit{r}$ (mm)', fontsize = 17)
plt.ylabel('Correlation ($\\mathit{C}$$\\rm_{mag}$)', fontsize = 17)
plt.text(80, 0.9, 'Small slip, time = %d ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])

# plt.title('Small slip, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])
plt.savefig('correlation of speed small drop.svg', dpi=600, format='svg')
plt.show()
