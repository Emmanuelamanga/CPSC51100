# -*- coding: utf-8 -*-
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 7 – Aggregating ACS PUMS Data

import pandas as pd
import numpy as np
from pandas import DataFrame 

def create_hincp_stats_table(df):
    '''Accepts a DataFrame of PUMS data and returns descriptive statistics for 
    household income.'''
    
    # Create lookup information from the data dictionary
    hht_dict = { 1 : 'Married couple household',
                 2 : 'Other family household:Male householder, no wife present',
                 3 : 'Other family household:Female householder, no husband present',
                 4 : 'Nonfamily household:Male householder:Living alone',
                 5 : 'Nonfamily household:Male householder:Not living alone',
                 6 : 'Nonfamily household:Female householder:Living alone',
                 7 : 'Nonfamily household:Female householder:Not living alone' }
    hht_lookup = DataFrame(hht_dict.items())
    hht_lookup.index.name = 'HHT - Household/family type'
    
    # Group and aggregate the PUMS data
    hht = df.groupby('HHT').aggregate({'HINCP':
        ['mean','std','count','min','max']})
    hht.columns = hht.columns.levels[1]
    hht.index = hht.index.astype(int)
    
    # Merge in the data dictionary values
    hht = hht.merge(hht_lookup, left_index=True, right_on=[0])
    hht.set_index(1, inplace=True)
    
    # Cleanup table values to match requirements and sort
    hht.index.name = None
    hht['min'] = hht['min'].astype(int)
    hht['max'] = hht['max'].astype(int)
    hht.sort_values(by='mean', inplace=True, ascending=False)
    return hht[['mean','std','count','min','max']]

def create_hhl_access_table(df):
    '''Accepts a DataFrame of PUMS data and returns descriptive statistics relating
    to languages spoken.'''
    
    # Create lookup information from the data dictionary    
    lang_lookup ={ 1: 'English only', 
                   2: 'Spanish', 
                   3: 'Other Indo-European languages',
                   4: 'Asian and Pacific Island languages', 
                   5:'Other language'} 
    
    access_lookup = { 1:'Yes w/ Subsrc.', 2:'Yes, wo/ Subsrc.', 3:'No'}
    # create a new variable with only the subset needed and drop the na values
    df1 = df[['HHL','ACCESS','WGTP']].dropna(subset=['WGTP','ACCESS','HHL'])
    wgtp_total = float(df1.WGTP.sum())
    # create a function that sums the values and convert to string with the % sign
    hhl_sum = lambda x: "{0:.2f}".format(round(np.sum(x)/wgtp_total* 100,2)) + '%'
    hhl_access = df1.pivot_table(['WGTP'],index='HHL',columns='ACCESS',aggfunc=hhl_sum,margins=True)
    hhl_access.index.name = 'HHL - Household language'
    # rename and column and index and return the result
    return hhl_access.rename(index=lang_lookup,columns=access_lookup)

def create_hincp_quantile_table(df):
    '''Accepts a DataFrame of PUMS data and returns quantile statistics relating
    to household income.'''
    
    # Bin the data
    desc = df.HINCP.describe(percentiles = [1/3.0, 2/3.0])
    df['bin'] = pd.cut(df.HINCP,
                       bins = [-np.Inf, desc['33.3%'], desc['66.7%'], np.Inf],
                       labels = ['low', 'medium', 'high'])
    
    # Group and aggregate
    df = df.groupby('bin').aggregate({'HINCP' : ['min', 'max', 'mean'],
                                      'WGTP' : ['sum']})
        
    # Cleanup data to match requirements
    df.columns = ['min', 'max', 'mean', 'household_count']
    df.index.name = 'HINCP'
    df['min'] = df['min'].astype(int)
    df['max'] = df['max'].astype(int)
    return df
    
def main():
    # Setup display options
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    
    # Read the csv file
    df = pd.read_csv("ss13hil.csv")
    
    # Output Table 1
    print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
    print(create_hincp_stats_table(df))
    print
    
    # Output Table 2
    print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***")    
    print(create_hhl_access_table(df))
    
    # Output Table 3
    print
    print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***")
    print(create_hincp_quantile_table(df))
    return df

if __name__ == "__main__":
    print("CPSC-51100, Summer 2018")
    print("Name: Don Cruver, Nicolas Cabaluna")
    print("PROGRAMMING ASSIGNMENT #7 \n")
    main()
