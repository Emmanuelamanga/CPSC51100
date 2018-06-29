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


def household_language_plot(fig, df):
    hhl = df.groupby('HHL').aggregate({'SERIALNO' : 'count'})
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

def household_income_plot(fig, df):
    hincp = df.HINCP[df.HINCP.notna()]
    ax = fig.add_subplot(2, 2, 2)
    x_range = np.logspace(0, 7, base=10)
    hist = ax.hist2d(x=hincp.values,
                     y=hincp.index)
    
def household_vehicle_plot(fig, df):
    veh = df.groupby('VEH').aggregate({'WGTP':'sum'})
    ax = fig.add_subplot(2, 2, 3)
    bar = ax.bar(veh.index, 
                 veh.WGTP / 1000, 
                 align='center', 
                 color='red',
                 tick_label=[int(x) for x in veh.index])
    plt.ylabel('Thousands of Households')
    plt.xlabel('# of Vehicles')
    plt.title(y = 1.0, s='Vehicles Available in Households', fontsize='small')

def household_taxes_plot(fig, df):
    return

fig = plt.figure(figsize=(12, 12))
df = pd.read_csv("ss13hil.csv")
household_language_plot(fig, df)
household_income_plot(fig, df)
household_vehicle_plot(fig, df)

plt.show()