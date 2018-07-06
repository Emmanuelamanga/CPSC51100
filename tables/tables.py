# -*- coding: utf-8 -*-
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 7 – Aggregating ACS PUMS Data

import pandas as pd
from pandas import DataFrame 

def create_hincp_stats_table(df):
    hht_dict = { 1 : 'Married couple household',
                 2 : 'Other family household:Male householder, no wife present',
                 3 : 'Other family household:Female householder, no husband present',
                 4 : 'Nonfamily household:Male householder:Living alone',
                 5 : 'Nonfamily household:Male householder:Not living alone',
                 6 : 'Nonfamily household:Female householder:Living alone',
                 7 : 'Nonfamily household:Female householder:Not living alone' }
    
    hht_lookup = DataFrame(hht_dict.items())
    hht_lookup.index.name = 'HHT - Household/family type'
    hht = df.groupby('HHT').aggregate({'HINCP':
        ['mean','std','count','min','max']})
    hht.columns = hht.columns.levels[1]
    hht.index = hht.index.astype(int)
    hht = hht.merge(hht_lookup, left_index=True, right_index = True)
    hht.set_index(1, inplace=True)
    hht.index.name = None
    hht.sort_values('mean')
    return hht

def create_hhl_access_table(df):
    lang_lookup = ['English only',
                   'Spanish',
                   'Other Indo-European languages',
                   'Asian and Pacific Island languages',
                   'Other language']
    wgtp_total = df.WGTP.fillna(0).sum()
    hhl_access = df.groupby(['HHL','ACCESS']).aggregate({})
    return

def create_hincp_quantile_table(df):
    return

def main():
    # Read the csv file
    df = pd.read_csv("ss13hil.csv")
    print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
    print(create_hincp_stats_table(df))

    print("*** Table 2 - HHL vs. ACCESS - Frequency Table ***")    
    print(create_hhl_access_table(df))
    
    print("*** Table 3 - Quantile Analysis of HINCP - Household income (past 12 months) ***")
    print(create_hincp_quantile_table(df))
    return df

if __name__ == "__main__":
    print("CPSC-51100, Summer 2018")
    print("Name: Don Cruver, Nicolas Cabaluna")
    print("PROGRAMMING ASSIGNMENT #7 \n")
    main()
