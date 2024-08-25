# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:36:15 2022

@author: xiaod
"""


# first of all, import the sensor data
import matplotlib.pyplot as plt
import math

#%% set parameters
index_ = 8671


#%% plot the friction coefficient with index


plt.plot(ConSV_PlateBottomBeadMiddle_.index[int(7e3):int(1.1e4+1)],  \
         (ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4,'fx'] - ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4,'fx'])/ \
         (ConSV_PlateTopBeadMiddle_.loc[7e3:1.1e4,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[7e3:1.1e4,'fy']),\
         linewidth = 1)
plt.scatter(ConSV_PlateBottomBeadMiddle_.index[index_],  \
         (ConSV_PlateBottomBeadMiddle_.loc[index_,'fx'] - ConSV_PlateTopBeadMiddle_.loc[index_,'fx'])/ \
         (ConSV_PlateTopBeadMiddle_.loc[index_,'fy'] - ConSV_PlateBottomBeadMiddle_.loc[index_,'fy']) \
             , c = 'r', marker = '*')
plt.title(ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'])

#%% scatter plot of vx(max min is plate motion)

# calculate velocity on each plate
# bottom


individuals_ = [int(2*i_) for i_ in range(143)]

vmx_bottom_ = 0
vmy_bottom_ = 0
for i_ in individuals_:
    vmx_bottom_ += sensors_[i_].loc[index_, 'vx']
    vmy_bottom_ += sensors_[i_].loc[index_, 'vy']   
vmx_bottom_ = vmx_bottom_ / len(individuals_)
vmy_bottom_ = vmy_bottom_ / len(individuals_)

# top
individuals_ = [int(2*i_+1) for i_ in range(143)]
vmx_top_ = 0
vmy_top_ = 0
for i_ in individuals_:
    vmx_top_ += sensors_[i_].loc[index_, 'vx']
    vmy_top_ += sensors_[i_].loc[index_, 'vy']   
vmx_top_ = vmx_top_ / len(individuals_)
vmy_top_ = vmy_top_ / len(individuals_)


# plot
individuals_ =    [int(i_) for i_ in range(286,2203)] 

c_name_ = 'vx'


x1_ = np.zeros(len(individuals_))
x2_ = np.zeros(len(individuals_))
c_ = np.zeros(len(individuals_))
count_ = 0
for i_ in individuals_:
    x1_[count_] = sensors_[i_].loc[index_, 'cx']
    x2_[count_] = sensors_[i_].loc[index_, 'cy']
    c_[count_] = sensors_[i_].loc[index_, c_name_]
    count_ += 1
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 17
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
fig = plt.figure(figsize=(20, 2))
plt.scatter(x1_ - 70,x2_ - 252,c = c_, s = 10, cmap = 'seismic', vmin = vmx_bottom_, vmax = vmx_top_ )
cb = plt.colorbar()
cb. set_label(label = '$\\mathit{v}_{xi}$ (m/s)', fontsize = 17)
# plt.title('Large slip, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 23)
plt.xlabel('$\\mathit{x}$ (mm, large slip, time = %d ms)' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 20)
plt.ylabel('$\\mathit{y}$ (mm)', fontsize =20)
plt.savefig('scatter plot of vx large slip(max min is plate motion).svg', dpi=600, format='svg')
plt.show()


#%% scatter plot of vx(extended range)

# calculate velocity on each plate
# bottom


individuals_ = [int(2*i_) for i_ in range(143)]

vmx_bottom_ = 0
vmy_bottom_ = 0
for i_ in individuals_:
    vmx_bottom_ += sensors_[i_].loc[index_, 'vx']
    vmy_bottom_ += sensors_[i_].loc[index_, 'vy']   
vmx_bottom_ = vmx_bottom_ / len(individuals_)
vmy_bottom_ = vmy_bottom_ / len(individuals_)

# top
individuals_ = [int(2*i_+1) for i_ in range(143)]
vmx_top_ = 0
vmy_top_ = 0
for i_ in individuals_:
    vmx_top_ += sensors_[i_].loc[index_, 'vx']
    vmy_top_ += sensors_[i_].loc[index_, 'vy']   
vmx_top_ = vmx_top_ / len(individuals_)
vmy_top_ = vmy_top_ / len(individuals_)


# plot
individuals_ =    [int(i_) for i_ in range(286,2203)] 

c_name_ = 'vx'


x1_ = np.zeros(len(individuals_))
x2_ = np.zeros(len(individuals_))
c_ = np.zeros(len(individuals_))
count_ = 0
for i_ in individuals_:
    x1_[count_] = sensors_[i_].loc[index_, 'cx']
    x2_[count_] = sensors_[i_].loc[index_, 'cy']
    c_[count_] = sensors_[i_].loc[index_, c_name_]
    count_ += 1
plt.rc('font', family = 'Arial')
plt.rcParams['font.size'] = 17
fig = plt.figure(figsize=(20, 2))
plt.scatter(x1_ - 70, x2_ - 252,c = c_, s = 10, cmap = 'seismic', vmin = vmx_bottom_ - 3*(vmx_top_ - vmx_bottom_ ), vmax = vmx_top_ + 3*(vmx_top_ - vmx_bottom_ ) )
cb = plt.colorbar()
cb. set_label(label = '$\\mathit{v}_{xi}$ (m/s)', fontsize = 17)
# plt.title('Large slip, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 23)
plt.xlabel('$\\mathit{x}$ (mm, large slip, time = %d ms)' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 20)

plt.ylabel('$\\mathit{y}$ (mm)', fontsize = 20)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.savefig('scatter plot of vx large slip(extend range).svg', dpi=600, format='svg')
plt.show()


#%% scatter plot of v

# calculate velocity on each plate
# bottom


individuals_ = [int(2*i_) for i_ in range(143)]

vmx_bottom_ = 0
vmy_bottom_ = 0
for i_ in individuals_:
    vmx_bottom_ += sensors_[i_].loc[index_, 'vx']
    vmy_bottom_ += sensors_[i_].loc[index_, 'vy']   
vmx_bottom_ = vmx_bottom_ / len(individuals_)
vmy_bottom_ = vmy_bottom_ / len(individuals_)

# top
individuals_ = [int(2*i_+1) for i_ in range(143)]
vmx_top_ = 0
vmy_top_ = 0
for i_ in individuals_:
    vmx_top_ += sensors_[i_].loc[index_, 'vx']
    vmy_top_ += sensors_[i_].loc[index_, 'vy']   
vmx_top_ = vmx_top_ / len(individuals_)
vmy_top_ = vmy_top_ / len(individuals_)


# plot
individuals_ =    [int(i_) for i_ in range(286,2203)] 

c_name_ = 'v'


x1_ = np.zeros(len(individuals_))
x2_ = np.zeros(len(individuals_))
c_ = np.zeros(len(individuals_))
count_ = 0
for i_ in individuals_:
    x1_[count_] = sensors_[i_].loc[index_, 'cx']
    x2_[count_] = sensors_[i_].loc[index_, 'cy']
    c_[count_] = math.sqrt((sensors_[i_].loc[index_, 'vx'] ** 2) + (sensors_[i_].loc[index_, 'vy'] ** 2))
    count_ += 1
plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.size'] = 17
fig = plt.figure(figsize=(20, 2))
plt.scatter(x1_ - 70, x2_ - 252,c = c_, s = 10, cmap = 'seismic',  vmin = 0, vmax = 0.001)
cb = plt.colorbar()
cb. set_label(label = '|$\\mathbf{v}_{i}$| (m/s)', fontsize = 17)
# plt.title('Large slip, time = %.2f ms ' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 23)
plt.xlabel('$\\mathit{x}$ (mm, large slip, time = %d ms)' % ConSV_PlateBottomBeadMiddle_.loc[index_,'Time'], fontsize = 20)
plt.ylabel('$\\mathit{y}$ (mm)', fontsize = 20)
plt.savefig('scatter plot of v large slip.svg', dpi=600, format='svg')
plt.show()