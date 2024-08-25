# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:43:44 2022

@author: xiaod
"""

#%% import data and packages

import matplotlib.pyplot as plt
from read_data_ver2 import * 
import numpy as np
from sklearn.linear_model import LinearRegression
import scipy.optimize as optimize

#%% set parameters(slip)

index_ = 8671  # the step have the maximum velocity
individuals_ =    [int(i_) for i_ in range(286,2203)] # record the grain number
x_ = np.zeros(len(individuals_))
y_ = np.zeros(len(individuals_))  # store the y of the maximum v point
vx_ =  np.zeros(len(individuals_)) # store the vx of the maximum v point
vy_ = np.zeros(len(individuals_)) # store the vx of the maximum v point
abs_vx_ = np.zeros(len(individuals_)) # store the abs_vx of the maximum v point

#%% get the x and y coodinate before and after the large drop(slip)


count_ = 0
for i_ in individuals_:
    x_[count_] = sensors_[i_].loc[index_, 'cx']
    y_[count_] = sensors_[i_].loc[index_, 'cy']
    vx_[count_] = sensors_[i_].loc[index_, 'vx']
    vy_[count_] = sensors_[i_].loc[index_, 'vy']
    abs_vx_[count_] = abs(vx_[count_])
    count_ += 1
    
#%% stastic the magnitude of velovity(slip)

n_,bins_, patches_ = plt.hist(abs_vx_, bins = 100)
centers_ = np.zeros(len(n_))
for i_ in range(len(n_)):
    centers_[i_] = (bins_[i_] + bins_[i_ + 1]) / 2

bins_large_ = np.copy(centers_)
n_large_ = n_ / (centers_[1] - centers_[0]) / len(individuals_)
n_log_ = np.log(n_ / (centers_[1] - centers_[0]))

#%% plot(slip)


model = LinearRegression(fit_intercept = True)
model.fit(centers_.reshape(-1, 1)[2:13], n_log_[2:13])
n_log_fit_ =  model.predict(centers_.reshape(-1, 1)[2:13])

plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.scatter(centers_[0:17], n_log_[0:17], c = 'none', edgecolor = 'b', linewidth = 1)
plt.plot(centers_[2:13], n_log_fit_, linestyle = '--', color = 'r')
plt.text(0.015, 10, s = 'slop = %.2f' % model.coef_[0], fontsize=15, rotation=-18)
plt.xlabel('|$\\mathbf{v}_{i}$| (m/s)', fontsize = 20)
plt.ylabel('ln(Probability density)', fontsize = 20)
plt.tick_params(labelsize = 17)
# plt.title('Large slip', fontsize = 17)
plt.text( 0.03, 12.8, 'Large slip')
plt.savefig('velocity statistic slip.svg', dpi=600, format='svg')
plt.show()


print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)


#%% set parameters(stick)

index_ = 9000  # the step have the maximum velocity
individuals_ =    [int(i_) for i_ in range(286,2203)] # record the grain number


#%% get the x and y coodinate before and after the large drop(stick)
count_ = 0
for i_ in individuals_:
    x_[count_] = sensors_[i_].loc[index_, 'cx']
    y_[count_] = sensors_[i_].loc[index_, 'cy']
    vx_[count_] = sensors_[i_].loc[index_, 'vx']
    vy_[count_] = sensors_[i_].loc[index_, 'vy']
    abs_vx_[count_] = abs(vx_[count_])
    count_ += 1
    
#%% stastic the magnitude of velovity(stick)

n_,bins_, patches_ = plt.hist(abs_vx_, bins = 100)
centers_ = np.zeros(len(n_))
for i_ in range(len(n_)):
    centers_[i_] = (bins_[i_] + bins_[i_ + 1]) / 2
bins_stick_ = np.copy(centers_)
n_stick_ = n_ / (centers_[1] - centers_[0]) / len(individuals_)
n_log_ = np.log(n_/ (centers_[1] - centers_[0]))

#%%  plot(stick)
model = LinearRegression(fit_intercept = True)
model.fit(centers_.reshape(-1, 1)[2:13], n_log_[2:13])
n_log_fit_ =  model.predict(centers_.reshape(-1, 1)[2:13])

plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.scatter(centers_[0:17], n_log_[0:17], c = 'none', edgecolor = 'b', linewidth = 1)
plt.plot(centers_[2:13], n_log_fit_, linestyle = '--', color = 'r')
plt.text(0.0015, 11, s = 'slop = %.2f' % model.coef_[0], fontsize=15, rotation=-22)
plt.xlabel('|$\\mathbf{v}_{i}$| (m/s)', fontsize = 20)
plt.ylabel('ln(Probability density)', fontsize = 20)
plt.tick_params(labelsize = 17)
# plt.title('Stick', fontsize = 17)
plt.text( 0.0035, 14.7, 'Stick')
plt.savefig('velocity statistic stick.svg', dpi=600, format='svg')
plt.show()


print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)




#%% set parameters(small slip)

index_ = 8476  # the step have the maximum velocity
individuals_ =    [int(i_) for i_ in range(286,2203)] # record the grain number
x_ = np.zeros(len(individuals_))
y_ = np.zeros(len(individuals_))  # store the y of the maximum v point
vx_ =  np.zeros(len(individuals_)) # store the vx of the maximum v point
vy_ = np.zeros(len(individuals_)) # store the vx of the maximum v point
abs_vx_ = np.zeros(len(individuals_)) # store the abs_vx of the maximum v point

#%% get the x and y coodinate before and after the large drop(small slip)


count_ = 0
for i_ in individuals_:
    x_[count_] = sensors_[i_].loc[index_, 'cx']
    y_[count_] = sensors_[i_].loc[index_, 'cy']
    vx_[count_] = sensors_[i_].loc[index_, 'vx']
    vy_[count_] = sensors_[i_].loc[index_, 'vy']
    abs_vx_[count_] = abs(vx_[count_])
    count_ += 1
    
#%% stastic the magnitude of velovity(small slip)

n_,bins_, patches_ = plt.hist(abs_vx_, bins = 100)
centers_ = np.zeros(len(n_))
for i_ in range(len(n_)):
    centers_[i_] = (bins_[i_] + bins_[i_ + 1]) / 2
bins_small_ = np.copy(centers_)
n_small_ = n_ / (centers_[1] - centers_[0]) / len(individuals_)
n_log_ = np.log(n_/ (centers_[1] - centers_[0]))

#%% plot(small slip)


model = LinearRegression(fit_intercept = True)
model.fit(centers_.reshape(-1, 1)[2:13], n_log_[2:13])
n_log_fit_ =  model.predict(centers_.reshape(-1, 1)[2:13])

plt.rc('font', family = 'Arial')
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.scatter(centers_[0:17], n_log_[0:17], c = 'none', edgecolor = 'b', linewidth = 1)
plt.plot(centers_[2:13], n_log_fit_, linestyle = '--', color = 'r')
plt.text(0.015, 9.5, s = 'slop = %.2f' % model.coef_[0], fontsize=15, rotation=-22)
plt.xlabel('|$\\mathbf{v}_{i}$| (m/s)', fontsize=18)
plt.ylabel('ln(Probability density)', fontsize=20)
plt.tick_params(labelsize = 17)
# plt.title('Small slip', fontsize = 17)
plt.text( 0.027, 12.8, 'Small slip')
plt.savefig('velocity statistic small slip.svg', dpi=600, format='svg')
plt.show()


print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)

#%% summerize

# define the exponential distribution function
def func(x_, lambda_, a0_):
    return lambda_ * np.exp(x_) + a0_

plt.axes(yscale = "log")

popt_stick_, pcov_stick_ = optimize.curve_fit(func, bins_stick_[2:17], n_stick_[2:17])
plt.plot(bins_stick_[0:17], func(bins_stick_[0:17], *popt_stick_), linestyle = '--', color = 'g', label = 'Stick, $\lambda$ = %d' % -popt_stick_[0])

popt_small_, pcov_small_ = optimize.curve_fit(func, bins_small_[2:17], n_small_[2:17])
plt.plot(bins_small_[0:17], func(bins_small_[0:17], *popt_small_), linestyle = '--', color = 'k', label = 'Small slip, $\lambda$ = %d' % -popt_small_[0])

popt_large_, pcov_large_ = optimize.curve_fit(func, bins_large_[2:40], n_large_[2:40])
plt.plot(bins_large_[0:40], func(bins_large_[0:40], *popt_large_), linestyle = '--', color = 'r', label = 'Large slip, $\lambda$ = %d' % -popt_large_[0])




plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rc('font', family = 'Arial')

plt.scatter(bins_large_[0:32], n_large_[0:32], c = 'none', edgecolor = 'r', linewidth = 1)
plt.scatter(bins_small_[0:15], n_small_[0:15], c = 'none', edgecolor = 'k', linewidth = 1)
plt.scatter(bins_stick_[0:17], n_stick_[0:17], c = 'none', edgecolor = 'g', linewidth = 1)
plt.ylim(10**(-1), 10**4)
plt.xlim(-0.005, 0.08)
plt.legend(frameon = False)
plt.tick_params(labelsize = 15)
plt.xlabel('|$\\mathbf{v}_{i}$| (m/s)', fontsize=17)
plt.ylabel('Probability density', fontsize=17)

plt.savefig('velocity statistic.svg', dpi=600, format='svg')
plt.show()