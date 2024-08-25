# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:53:04 2022

@author: xiaod
"""

import pickle


#%% save list_correlation_o_
filename_ = open('list_correlation_o_.pkl', 'wb')
pickle.dump(list_correlation_o_, filename_)
filename_.close()


#%% read
filename_ = open('list_correlation_o_20220708.pkl', 'rb')
list_correlation_o_ = pickle.load(filename_)
print(list_correlation_o_)
filename_.close()

#%% save list_correlation_s_
filename_ = open('list_correlation_s_.pkl', 'wb')
pickle.dump(list_correlation_s_, filename_)
filename_.close()

#%% read
filename_ = open('list_correlation_s_20220708.pkl', 'rb')
list_correlation_s_ = pickle.load(filename_)
print(list_correlation_s_)
filename_.close()

#%%
#%%
#%%

#%% list_vmx_bottom_
filename_ = open('list_vmx_bottom_all.pkl', 'wb')
pickle.dump(list_vmx_bottom_, filename_)
filename_.close()


#%% list_vmy_bottom_
filename_ = open('list_vmy_bottom_all.pkl', 'wb')
pickle.dump(list_vmy_bottom_, filename_)
filename_.close()


#%% list_vmx_top_
filename_ = open('list_vmx_top_all.pkl', 'wb')
pickle.dump(list_vmx_top_, filename_)
filename_.close()


#%% list_vmy_top_
filename_ = open('list_vmy_top_all.pkl', 'wb')
pickle.dump(list_vmy_top_, filename_)
filename_.close()


#%% list_vm_grain_
filename_ = open('list_vm_grain_all.pkl', 'wb')
pickle.dump(list_vm_grain_, filename_)
filename_.close()


#%% list_vmx_grain_
filename_ = open('list_vmx_grain_all.pkl', 'wb')
pickle.dump(list_vmx_grain_, filename_)
filename_.close()


#%% list_vmy_grain_
filename_ = open('list_vmy_grain_all.pkl', 'wb')
pickle.dump(list_vmy_grain_, filename_)
filename_.close()


#%% list_phi_
filename_ = open('list_phi_.pkl', 'wb')
pickle.dump(list_phi_, filename_)
filename_.close()

#%% list_cmx_bottom_
filename_ = open('list_cmx_bottom_.pkl', 'wb')
pickle.dump(list_cmx_bottom_, filename_)
filename_.close()

#%% list_cmy_bottom_
filename_ = open('list_cmy_bottom_.pkl', 'wb')
pickle.dump(list_cmy_bottom_, filename_)
filename_.close()

#%% list_cmx_top_
filename_ = open('list_cmx_top_.pkl', 'wb')
pickle.dump(list_cmx_top_, filename_)
filename_.close()



#%% list_cmy_top_
filename_ = open('list_cmy_top_.pkl', 'wb')
pickle.dump(list_cmy_top_, filename_)
filename_.close()






