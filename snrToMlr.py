# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:54:39 2024

@author: grace
"""
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

def main():
    mlranalysis()

def barChartDataWithConfidenceInterval(x, handle=None, legendLabel = "Data 1", confidence_level =0.95):
    
    mean = x.mean()
    std = x.std()
    n = len(x)
    alpha = 1 - confidence_level
    t_critical = t.ppf(1 - alpha/2, df=n-1)
    # Calculate the margin of error
    margin_of_error = t_critical * (std / np.sqrt(n))
    
    if handle:
        handle.errorbar(x=1, y=mean,  yerr=margin_of_error, fmt='o', capsize=5, label=legendLabel)
       # handle.set_title(f'{confidence_level*100}% Confidence Interval Error Bar')

    else:
        fig, ax = plt.subplots()
        ax.errorbar(x=0, y=mean,  yerr=margin_of_error, fmt='o', capsize=5, label=legendLabel)
        
    plt.title(f'{confidence_level*100}% Confidence Interval Error Bar')
    plt.xlabel('Measurement')
    plt.ylabel('Value')
    plt.legend()
    return ax
    

def mlranalysis():
    
    df = pd.read_excel('.\\Statistics-gk_opto_stim_snr_mlr_11_25_24 (trial).xlsx', sheet_name='Analysis', skiprows=[ 1, 2, 3])
    dfStim = df.loc[(df['state'] > 0)]
    dfNoStim = df.loc[(df['state'] == 0)]
    # print(dfStim['speed'].mean())
    # print(dfNoStim['speed'].mean())
    dfoneS = df[df['Trial'].isin(['Trial     5', 'Trial     12', 'Trial     15', 'Trial     17', 'Trial     22', 'Trial     27', 'Trial     30'])]
    dfoneSStim = dfoneS.loc[(dfoneS['state'] > 0)]
    dfoneSNoStim = dfoneS.loc[(dfoneS['state'] == 0)]
    
    StimSpeed = dfoneSStim['speed']
    NoStimeSpeed = dfoneSNoStim['speed']
    
    h = barChartDataWithConfidenceInterval(StimSpeed,legendLabel="Stim")
    h = barChartDataWithConfidenceInterval(NoStimeSpeed,h,legendLabel="NoStim")
    plt.show()
    print('hi')
    
    
    # # Get all the speed data for statistical calculation
    
    # StimSpeedMean=StimSpeed.mean()
    # NoStimSpeedMean=NoStimeSpeed.mean()
    
    # StimSpeedStd = StimSpeed.std()
    # NoStimSpeedStd = NoStimSpeedMean.std()
    
    
    
    # print("The mean speed of the stim subset:",StimSpeedMean)
    # print("The mean speedof the NO stim subset:",NoStimSpeedMean)  
    
    
   
    # # oneSStim = dfoneS.loc[(df['state'] > 0)]
    # # oneSNoStim = dfoneS.loc[(df['state'] == 0)]
    # # StimSpeed = oneSStim['speed']
    # # NoStim = oneSNoStim['speed']
    
    # # t_stat, p_value = stats.ttest_ind(NoStim, Stim)
    # # print(f"T-statistic: {t_stat}, P-value: {p_value}")
    # categories = ['Stim', 'NoStim']


    # tmp = [StimSpeedMean,NoStimSpeedMean]
    # MLRPlot = plt.bar(categories, tmp)
    # plt.title('Speed During SNR to MLR Stim')
    # plt.xlabel('MLR Stim')
    # plt.ylabel('Speed cm/s')
    # plt.show()
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