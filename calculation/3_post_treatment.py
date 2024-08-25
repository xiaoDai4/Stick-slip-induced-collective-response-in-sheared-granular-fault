# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:41:41 2022

@author: xiaod
"""
#%% packages
import numpy as np

#%%

#%% intergral correlation 
def intergral_correlation(x_,list_correlation_):
    '''
    Parameters
    ----------
    x_: distance series
    list_correlation_: record the correlation series

    Returns
    -------
    integral_correlation_: the integral of correlation 
    
    integral_correlation_positive_: the integral of positive correlation 
    
    integral_correlation_negative_: the integral negative of correlation 
    
    '''
    interval_ = x_[1] - x_[0]
    integral_correlation_ = np.zeros(len(list_correlation_))
    integral_correlation_abs_ = np.zeros(len(list_correlation_))
    integral_correlation_positive_ = np.zeros(len(list_correlation_))
    integral_correlation_negative_ = np.zeros(len(list_correlation_))
    i_ = 0
   
    for correlation_ in list_correlation_:
        marker_ = 0 # mark if the position cross the first correlation point
        for t_ in correlation_:
            # print(marker_)
            # dismiss the first domain
            if marker_ == 0:
                # print(marker_)
                if t_ <= 0:
                    marker_ = 1
                    integral_correlation_negative_[i_] += t_
            # calculate the remain part
            elif marker_ == 1:
                # print(marker_)
                if t_ <= 0:
                    integral_correlation_negative_[i_] += t_
                if t_ >= 0:
                    integral_correlation_positive_[i_] += t_
        i_ += 1
        integral_correlation_ = integral_correlation_negative_ + integral_correlation_positive_
        integral_correlation_abs_ = integral_correlation_positive_ - integral_correlation_negative_
    return integral_correlation_ * interval_,integral_correlation_negative_ * interval_, integral_correlation_positive_ * interval_, integral_correlation_abs_ * interval_

        
      
x_ = np.linspace(0,300,31)
integral_correlation_, integral_correlation_negative_, integral_correlation_positive_, integral_correlation_abs_ = intergral_correlation(x_,list_correlation_s_) 
#%%

#%% the correlation at a certain distance 
def domain_para(x_, list_correlation_, threshold_):
    '''
    Parameters
    ----------
    x_ : 
        distance series
    list_correlation_ : 
        record the correlation series
    threshold_:
        distinguish domain
    
    Returns 
    -------
    turn_: count the turns
    tranverse_: count the tranverse
    length_: the length of the domain
    length_var_
    domain_area_:
    domain_area_var_:
    ratio_tt_: ratio of tranverse to turn 
    '''
    interval_ = x_[1] - x_[0]
    turn_ = np.zeros(len(list_correlation_))
    tranverse_ = np.zeros(len(list_correlation_))
    length_ = np.zeros(len(list_correlation_))
    length_var_ = np.zeros(len(list_correlation_))
    domain_area_ = np.zeros(len(list_correlation_))
    domain_area_var_ = np.zeros(len(list_correlation_))
    ratio_tt_ = np.zeros(len(list_correlation_))
    # turn_
    i_ = 0
    for correlation_ in list_correlation_:
        marker_ = 0
        for t_ in correlation_:
            # print(marker_)
            # dismiss the first domain
            if marker_ == 0:
                # print(marker_)
                if t_ <= 0:
                    marker_ = 1
                    old_step_ = t_ # record the old step's value 
                    trend_ = -1 # record the state of trend
            # calculate the remain part
            elif marker_ == 1:
                if trend_ == -1:
                    if t_ >= old_step_:
                        turn_[i_] += 1
                        trend_ = 1
                    old_step_ = t_                       
                elif trend_ == 1: 
                    if t_ <= old_step_:
                        turn_[i_] += 1
                        trend_ = -1
                    old_step_ = t_       
        i_ += 1
    
    # tranverse_ and domain boundary
    i_ = 0
    domain_boundary_all_ = []
    for correlation_ in list_correlation_:
        marker_ = 0
        domain_boundary_ = [] # record the domain boundary
        for t_ in correlation_:
            # print(marker_)
            # dismiss the first domain
            if marker_ == 0:
                # print(marker_)1
                if t_ <= 0:
                    marker_ = 1
                    if threshold_ >= 0:
                        threshold_ = -threshold_ # the threshold to distinguish domains
                    state_ = 1  # record the current state
                    potential_boundary_ = x_[np.where(correlation_ == t_)][0] # record the potential boundary
                    old_step_ = t_   # record the old step
                    if t_ <= threshold_:
                        tranverse_[i_] += 1
                        state_ = -1
                        threshold_ = -threshold_
                        domain_boundary_.append(potential_boundary_)
            # calculate the remain part
            elif marker_ == 1:
                if state_ == 1:
                    if t_ * old_step_ <= 0:
                        potential_boundary_ = x_[np.where(correlation_ == t_)][0]
                        # print(potential_boundary_)
                    if t_  <= threshold_:
                        tranverse_[i_] += 1
                        state_ = -1
                        threshold_ = -threshold_
                        domain_boundary_.append(potential_boundary_)
                    old_step_ = t_                       
                elif state_ == -1: 
                    if t_ * old_step_ <= 0:
                        potential_boundary_ = x_[np.where(correlation_ == t_)][0]
                        # print(potential_boundary_)
                    if t_ >= threshold_:
                        tranverse_[i_] += 1
                        state_ = 1
                        threshold_ = -threshold_
                        domain_boundary_.append(potential_boundary_)
                    old_step_ = t_
        domain_boundary_all_.append(domain_boundary_)
        i_ += 1
    
    
    # complete domain boundary 
    for i_ in range(tranverse_.shape[0]):
        if tranverse_[i_] ==  len(domain_boundary_all_[i_]):
            domain_boundary_all_[i_].append(x_[len(x_)-1])

    
    # length_
    for i_ in range(length_.shape[0]):
        length_[i_] = (domain_boundary_all_[i_][len(domain_boundary_all_[i_])-1] - \
                       domain_boundary_all_[i_][0]) / (len(domain_boundary_all_[i_])-1)
  
    # ratio_tt_ 
    for i_ in range(ratio_tt_.shape[0]):
        ratio_tt_[i_] = turn_[i_] / tranverse_[i_]
    
    # length_var_    
    for i_ in range(length_var_.shape[0]):
        lenths_ = []
        for j_ in range(len(domain_boundary_all_[i_][1:])):
            lenths_.append(domain_boundary_all_[i_][j_+1] - domain_boundary_all_[i_][j_])
        # print(lenths_)
        length_var_[i_] = np.var(lenths_)
       
    # domain_area_: record the 
    # domain_area_var_:
    for i_ in range(len(domain_boundary_all_)):
        t_index_ = [] # record the boundary position
        areas_ = [] # record the areas in one index 
        for j_ in domain_boundary_all_[i_]:
            t_index_.append(np.where(x_ == j_)[0][0])
        for k_ in range(len(t_index_) - 1):
            t_area_ = 0
            for l_ in range(int(t_index_[k_+1] - t_index_[k_])):
                t_area_ += list_correlation_[i_][t_index_[k_] + l_]
            areas_.append(abs(t_area_) * interval_)
        domain_area_[i_] = np.mean(areas_)
        domain_area_var_[i_] = np.var(areas_)
    return turn_, tranverse_, ratio_tt_, length_, length_var_, domain_area_, domain_area_var_
turn_, tranverse_, ratio_tt_, length_, length_var_, domain_area_,domain_area_var_ = domain_para(x_,list_correlation_s_, 0.1) 

#%%
#%%increasement
def increasement(x_, list_correlation_):
    '''
    
    Parameters
    ----------
    correlation_ : the processed correlation in each step

    Returns
    -------
    d_correlation_: the increasement of the proccessed correlation
    
    '''
    interval_ = x_[1] - x_[0]
    d_correlation_ = np.zeros(len(list_correlation_) - 1)
    
    for i_ in range(len(d_correlation_)):
        d_correlation_[i_] = np.sum(np.absolute( (list_correlation_[i_+1] - list_correlation_[i_]) * interval_))
    return d_correlation_
x_ = np.linspace(0,300,31)
d_correlation_ = increasement(x_, list_correlation_s_)

#%%

#%% calculate velocity on each plate
# bottom
index_ = 8300

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

#%% calculate velocity in a period
# bottom
index_ = 5000
stop_index_ = 20000
time_step_ = 1
list_vmx_bottom_ = [] # record the mean vx pf bottom
list_vmy_bottom_ = [] # record the mean vy of bottom
list_vmx_top_ = []   # record the mean vx of top
list_vmy_top_ = []    # record the mean vy of top
list_vm_grain_ = []     # record the mean v of grain
list_vmx_grain_ = []     # record the mean vx of grain
list_vmy_grain_ = []    # record the mean vy of grain

while index_ <= stop_index_:
    print(index_)
    individuals_ = [int(2*i_) for i_ in range(143)]
    # bottom
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

    # grains
    individuals_ = [int(i_) for i_ in range(286,2203)] 

    sensors_dv_ = decentralization_v(individuals_, sensors_, index_)
    
    
    
    
    list_vmx_bottom_.append(vmx_bottom_)
    list_vmy_bottom_.append(vmy_bottom_)
    list_vmx_top_.append(vmx_top_)
    list_vmy_top_.append(vmy_top_)
    list_vm_grain_.append(sensors_dv_['v'].mean())
    list_vmx_grain_.append(sensors_dv_['vx'].mean())
    list_vmy_grain_.append(sensors_dv_['vy'].mean())
    
    index_ += time_step_
#%% polarization one step
# bottom
index_ = 8300

individuals_ = [int(i_) for i_ in range(286,2203)] 

vmx_unit_ = 0
vmy_unit_ = 0
for i_ in individuals_:
    v_ = math.sqrt(sensors_[i_].loc[index_, 'vx'] ** 2 + sensors_[i_].loc[index_, 'vy'] ** 2)
    vmx_unit_ += sensors_[i_].loc[index_, 'vx'] / v_
    vmy_unit_ += sensors_[i_].loc[index_, 'vy'] / v_

    
vmx_unit_ = vmx_unit_ / len(individuals_)
vmy_unit_ = vmy_unit_ / len(individuals_)
phi_ = math.sqrt(vmx_unit_ ** 2 + vmy_unit_ ** 2)




#%% polarization a period



# bottom
index_ = 7000
stop_index_ = 11000
time_step_ = 1
list_phi_ = [] # record the mean vx pf bottom
individuals_ = [int(i_) for i_ in range(286,2203)] 

while index_ <= stop_index_:
    print(index_)
    vmx_unit_ = 0
    vmy_unit_ = 0
    for i_ in individuals_:
        v_ = math.sqrt(sensors_[i_].loc[index_, 'vx'] ** 2 + sensors_[i_].loc[index_, 'vy'] ** 2)
        vmx_unit_ += sensors_[i_].loc[index_, 'vx'] / v_
        vmy_unit_ += sensors_[i_].loc[index_, 'vy'] / v_

        
    vmx_unit_ = vmx_unit_ / len(individuals_)
    vmy_unit_ = vmy_unit_ / len(individuals_)
    phi_ = math.sqrt(vmx_unit_ ** 2 + vmy_unit_ ** 2)
    
    
    
    
    list_phi_.append(phi_)

    
    index_ += time_step_






#%% plate's coordinate in a step

# bottom
index_ = 8300

individuals_ = [int(2*i_) for i_ in range(143)]

cmx_bottom_ = 0
cmy_bottom_ = 0
for i_ in individuals_:
    cmx_bottom_ += sensors_[i_].loc[index_, 'cx']
    cmy_bottom_ += sensors_[i_].loc[index_, 'cy']   
cmx_bottom_ = cmx_bottom_ / len(individuals_)
cmy_bottom_ = cmy_bottom_ / len(individuals_)

# top
individuals_ = [int(2*i_+1) for i_ in range(143)]
cmx_top_ = 0
cmy_top_ = 0
for i_ in individuals_:
    cmx_top_ += sensors_[i_].loc[index_, 'cx']
    cmy_top_ += sensors_[i_].loc[index_, 'cy']   
cmx_top_ = cmx_top_ / len(individuals_)
cmy_top_ = cmy_top_ / len(individuals_)





#%% calculate plate's coordinate in a period
# bottom
index_ = 7000
stop_index_ = 11000
time_step_ = 1
list_cmx_bottom_ = [] # record the mean cx pf bottom
list_cmy_bottom_ = [] # record the mean cy of bottom
list_cmx_top_ = []   # record the mean cx of top
list_cmy_top_ = []    # record the mean cy of top

while index_ <= stop_index_:
    print(index_)
    individuals_ = [int(2*i_) for i_ in range(143)]
    # bottom
    cmx_bottom_ = 0
    cmy_bottom_ = 0
    for i_ in individuals_:
        cmx_bottom_ += sensors_[i_].loc[index_, 'cx']
        cmy_bottom_ += sensors_[i_].loc[index_, 'cy']   
    cmx_bottom_ = cmx_bottom_ / len(individuals_)
    cmy_bottom_ = cmy_bottom_ / len(individuals_)
    
    # top
    individuals_ = [int(2*i_+1) for i_ in range(143)]
    cmx_top_ = 0
    cmy_top_ = 0
    for i_ in individuals_:
        cmx_top_ += sensors_[i_].loc[index_, 'cx']
        cmy_top_ += sensors_[i_].loc[index_, 'cy']   
    cmx_top_ = cmx_top_ / len(individuals_)
    cmy_top_ = cmy_top_ / len(individuals_)

    
    list_cmx_bottom_.append(cmx_bottom_)
    list_cmy_bottom_.append(cmy_bottom_)
    list_cmx_top_.append(cmx_top_)
    list_cmy_top_.append(cmy_top_)

    
    index_ += time_step_

