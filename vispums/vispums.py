# -*- coding: utf-8 -*-

# Name: Don Cruver, Nicolas Cabaluna
# Date: Jun 25, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 6 – Visualizing ACS PUMS Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib

def household_language_plot(fig, hhl):
    lang_lookup = ['English only',
                    'Spanish',
                    'Other Indo-European languages',
                    'Asian and Pacific Island languages',
                    'Other language']

    ax = fig.add_subplot(2, 2, 1)
    pie = ax.pie(hhl, startangle=-117)
    ax.legend(lang_lookup, loc='upper left', 
              bbox_to_anchor=(-0.3, 0.93), 
              fontsize='small')
    plt.title(y = 0.92, s='Household Languages', fontsize='small')

def household_income_plot(fig, hincp):
    ax = fig.add_subplot(2, 2, 2)
    x_range = np.logspace(0, 7, base=10)
    hist = ax.hist2d(x=hincp.values,
                     y=hincp.index)
    
def household_vehicle_plot(fig, veh):
    ax = fig.add_subplot(2, 2, 3)
    bar = ax.bar(veh.index, 
                 veh.WGTP / 1000, 
                 align='center', 
                 color='red')
    plt.ylabel('Thousands of Households')
    plt.xlabel('# of Vehicles')
    plt.title(y = 1.0, s='Vehicles Available in Households', fontsize='small')

fig = plt.figure(figsize=(12, 12))
df = pd.read_csv("ss13hil.csv")
household_language_plot(fig, df.groupby('HHL').aggregate({'SERIALNO' : 'count'}))
household_income_plot(fig, df.HINCP[df.HINCP.notna()])
household_vehicle_plot(fig, df.groupby('VEH').aggregate({'WGTP':'sum'}))
plt.show()