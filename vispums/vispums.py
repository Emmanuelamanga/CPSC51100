# -*- coding: utf-8 -*-

# Name: Don Cruver, Nicolas Cabaluna
# Date: Jun 25, 2018
# Course: CPSC51100 - Statistical Programming, Lewis University
# Term: Summer 2018
# Assignment Name: Programming Assignment 6 – Visualizing ACS PUMS Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def household_language_plot(fig, df):
    '''Adds the pie-chart of household languages as specified in the assignment'''
    hhl = df.groupby('HHL').aggregate({'SERIALNO' : 'count'})
    lang_lookup = ['English only',
                   'Spanish',
                   'Other Indo-European languages',
                   'Asian and Pacific Island languages',
                   'Other language']

    ax = fig.add_subplot(2, 2, 1)
    ax.axis('equal')
    pie = ax.pie(hhl, startangle=-117)
    ax.legend(lang_lookup, loc='upper left', 
              bbox_to_anchor=(0.1, 0.93), 
              fontsize='small')
    plt.title(y = 0.91, s='Household Languages', fontsize='small')

def household_income_plot(fig, df):
    '''Adds the household-income histogram as specified in the assignment'''
    hincp = df.HINCP[df.HINCP.notna()]    
    ax = fig.add_subplot(2, 2, 2)
    bins = np.logspace(1, 7, num=110, base=10)
    hist = ax.hist(x=hincp, 
                   density=True, 
                   bins=bins, 
                   histtype='bar',
                   color='#00cc00',
                   edgeColor='black',
                   linewidth=0.6)                      
    plt.xscale('log', nonposx='clip', subsx=[1, 2, 3, 4, 5, 6, 7])
    hincp.plot.kde(ax=ax, style='--', logx=True)
    ax.grid(linestyle='--')
    plt.ylabel('Density')
    plt.xlabel('Household Income ($) - Log Scaled')
    plt.title(y = 1.0, s='Distribution of Household Income', fontsize='small')
    
def household_vehicle_plot(fig, df):
    '''Adds the household-vehicle bar chart as specified in the assignment'''
    veh = df.groupby('VEH').aggregate({'WGTP':'sum'})
    ax = fig.add_subplot(2, 2, 3)
    ax.bar(veh.index, 
           veh.WGTP / 1000, 
           align='center', 
           color='red',
           tick_label=[int(x) for x in veh.index])
    plt.ylabel('Thousands of Households')
    plt.xlabel('# of Vehicles')
    plt.title(y = 1.0, s='Vehicles Available in Households', fontsize='small')

def household_taxes_plot(fig, df):
    '''Adds the taxes vs. home size scatter plot as specified in the 
    assignment'''
    return

# Create the figure
fig = plt.figure(figsize=(20, 10))

# Read the csv file
df = pd.read_csv("ss13hil.csv")

# Add the plots to the figures
household_language_plot(fig, df)
household_income_plot(fig, df)
household_vehicle_plot(fig, df)
household_taxes_plot(fig, df)

# Export to png file
plt.savefig('pums.png')