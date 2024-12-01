# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:54:39 2024

@author: grace
"""
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

def main():
    mlranalysis()

def mlranalysis():
    
    df = pd.read_excel('.\\Statistics-gk_opto_stim_snr_mlr_11_25_24 (trial).xlsx', sheet_name='Analysis', skiprows=[ 1, 2, 3])
    dfStim = df.loc[(df['state'] > 0)]
    dfNoStim = df.loc[(df['state'] == 0)]
    print(dfStim['speed'].mean())
    print(dfNoStim['speed'].mean())
    dfoneS = df[df['Trial'].isin(['Trial     5', 'Trial     12', 'Trial     15', 'Trial     17', 'Trial     22', 'Trial     27', 'Trial     30'])]
    dfoneSStim = dfoneS.loc[(dfoneS['state'] > 0)]
    dfoneSNoStim = dfoneS.loc[(dfoneS['state'] == 0)]
    stimspeed=(dfoneSStim['speed'].mean())
    nostimspeed=(dfoneSNoStim['speed'].mean())
    print(dfoneSStim['speed'].mean())
    print(dfoneSNoStim['speed'].mean())  
    oneSStim = dfoneS.loc[(df['state'] > 0)]
    oneSNoStim = dfoneS.loc[(df['state'] == 0)]
    Stim = oneSStim['speed']
    NoStim = oneSNoStim['speed']
    t_stat, p_value = stats.ttest_ind(NoStim, Stim)
    print(f"T-statistic: {t_stat}, P-value: {p_value}")
    categories = ['Stim', 'NoStim']
    values = [Stim.mean(), NoStim.mean()]
    Stimarr = np.array([Stim], dtype=object)
    NoStimarr = np.array([NoStim], dtype=object)
    values = [Stimarr, NoStimarr]
    tmp = [stimspeed,nostimspeed]
    MLRPlot = plt.bar(categories, tmp)
    plt.title('Speed During SNR to MLR Stim')
    plt.xlabel('MLR Stim')
    plt.ylabel('Speed cm/s')
    plt.show()
#mlranalysis()
def vmanalysis():
    df = pd.read_excel('C:\\Users\\grace\\OneDrive\\Documents\\tmp.xlsx', sheet_name='Analysis')
    dfVM = df[-df['Trial'].isin(['Trial     5', 'Trial     6', 'Trial     7'])]
    dfVMStim = dfVM.loc[(dfVM['state'] > 0)]
    dfVMNoStim = dfVM.loc[(dfVM['state'] == 0)]
    print(dfVMStim['speed'].mean())
    print(dfVMNoStim['speed'].mean())
    VMNoStim = dfVM.loc[(df['state'] == 0)]
    VMStim = dfVM.loc[(df['state'] > 0)]
    StimVM = VMStim['speed']
    NoStimVM = VMNoStim['speed']
    t_stat, p_value = stats.ttest_ind(NoStimVM, StimVM)
    print(f"T-statistic: {t_stat}, P-value: {p_value}")
    categories = ['StimVM', 'NoStimVM']
    values = [StimVM.mean(), NoStimVM.mean()]
    VMPlot = plt.bar(categories, values)
    plt.title('Speed During SNR to VM Stim')
    plt.xlabel('VM Stim')
    plt.ylabel('Speed cm/s')
    plt.show()
    
if __name__ == "__main__":
    main()