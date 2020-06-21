# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:59:11 2020

@author: PHH2KOR
"""

import mdfreader
import pandas as pd

#Loading dat file

yop = mdfreader.Mdf('EM59_Cold_MIDC_Veh6/23012020_Cold_ET_Veh6_EM59.dat') #This is the dat file
yop.resample(0.1) #resampling the data to 0.1s
channel_list = list(yop.keys()) 

df = pd.DataFrame(columns=channel_list) #pandas dataframe to store dat file content
for channel in channel_list:
    values = yop.get_channel_data(channel) #to load entire dat file , an expensive operation
    df[channel] = values


channel_list_filter = ['Epm_nEng', 'InjCtl_qSetUnBal', 'CEngDsT_t',
                'InjCrv_qPiI1Des_mp', 'InjCrv_phiMI1Des', 'InjCrv_tiPiI1Des',
                 'RailP_pFlt','AFS_mAirPerCyl', 'EnvP_p']

df_filter = pd.DataFrame(columns=channel_list_filter) #pandas dataframe to store dat file content
for channel in channel_list_filter:
    values = yop.get_channel_data(channel) #to load selected channels from dat file, an inexpensive operation
    df_filter[channel] = values

df_filter.to_csv('filedat.csv')

#loading ascii file
df_ascii = pd.read_csv('EM59_Cold_MIDC_Veh6/1i_200123_007a.asc', encoding='mbcs', sep=' ', low_memory=False)
df_ascii.to_csv('fileascii.csv')
