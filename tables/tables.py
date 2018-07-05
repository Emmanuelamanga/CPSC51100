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
    
    hht_lookup = DataFrame(hht_dict.items(), columns=['key','desc'])
    
    hht = df.groupby('HHT').aggregate(
            {'HINCP':['mean','std','count','min','max']})
    hht.columns = hht.columns.levels[1]
    hht.index = hht.index.astype(int)
    return hht.merge(hht_lookup, left_index=True, right_on='key')

def create_hhl_access_table(df):
    return

def create_hincp_quantile_table(df):
    return

def main():
    # Read the csv file
    df = pd.read_csv("ss13hil.csv")
    print("*** Table 1 - Descriptive Statistics of HINCP, grouped by HHT ***")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(create_hincp_stats_table(df))
        
    #print(create_hhl_access_table(df))
    #print(create_hincp_quantile_table(df))
    return df

if __name__ == "__main__":
    print("CPSC-51100, Summer 2018")
    print("Name: Don Cruver, Nicolas Cabaluna")
    print("PROGRAMMING ASSIGNMENT #7 \n")
    main()
