# -*- coding: utf-8 -*-

# Name: Don Cruver, Nicolas Cabaluna
# Date: Jun 25, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 6 – Visualizing ACS PUMS Data

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def household_language_plot(fig, hhl):
    lang_lookup = ['English only',
                    'Spanish',
                    'Other Indo-European languages',
                    'Asian and Pacific Island languages',
                    'Other language']  
             
    ax1 = fig.add_subplot(2, 2, 1)
    pie = ax1.pie(hhl, startangle=-117)
    ax1.legend(lang_lookup, loc='upper left', bbox_to_anchor=(-0.3, 0.93), fontsize='small')
    plt.title(y = 0.92, s='Household Languages', fontsize='small')

def household_income_plot(fig, hincp):
    ax1 = fig.add_subplot(2, 2, 2)
    hist = ax1.hist2d(x=pd.cut(hincp.HINCP, np.logspace(start=1, stop=7)),
                      y=hincp.HINCP, bins='auto') 

fig = plt.figure(figsize=(12, 12))
df = pd.read_csv("ss13hil.csv")
household_language_plot(fig, df.groupby('HHL').aggregate({'SERIALNO' : 'count'}))
household_income_plot(fig, df)
print(df)