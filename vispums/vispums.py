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
    # aggregate the data
    hhl = df.groupby('HHL').aggregate({'SERIALNO' : 'count'})

    # create the pie chart
    ax = fig.add_subplot(2, 2, 1)
    ax.axis('equal')
    pie = ax.pie(hhl, startangle=-117)

    # add the legend    
    lang_lookup = ['English only',
               'Spanish',
               'Other Indo-European languages',
               'Asian and Pacific Island languages',
               'Other language']
    ax.legend(lang_lookup, loc='upper left', 
              bbox_to_anchor=(0.1, 0.93), 
              fontsize='small')
              
    # add the title
    plt.title(y = 0.91, s='Household Languages', fontsize='small')

def household_income_plot(fig, df):
    '''Adds the household-income histogram as specified in the assignment'''
    # filter out missing data
    hincp = df.HINCP[df.HINCP.notna()]

    # create the histogram    
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
    
    # add labels and title
    plt.ylabel('Density')
    plt.xlabel('Household Income ($) - Log Scaled')
    plt.title(y = 1.0, s='Distribution of Household Income', fontsize='small')
    
def household_vehicle_plot(fig, df):
    '''Adds the household-vehicle bar chart as specified in the assignment'''
    # aggregate the data
    veh = df.groupby('VEH').aggregate({'WGTP':'sum'})
    
    # create the bar chart
    ax = fig.add_subplot(2, 2, 3)
    ax.bar(veh.index, 
           veh.WGTP / 1000, 
           align='center', 
           color='red',
           tick_label=[int(x) for x in veh.index])
           
    # add labels and title
    plt.ylabel('Thousands of Households')
    plt.xlabel('# of Vehicles')
    plt.title(y = 1.0, s='Vehicles Available in Households', fontsize='small')

def household_taxes_plot(fig, df):
    '''Adds the taxes vs. home size scatter plot as specified in the 
    assignment'''
    # create the mapping between the TAXP to $ value
    mapping={1:0,2:1,3:50,63:5500,64:6000,65:7000,66:8000,67:9000,68:10000}
    for i in range(4,63):
      if(i<23):
        mapping[i] = mapping[i-1]+50
      else:
        mapping[i] = mapping[i-1]+100
        
    #replace the value of TAXP with the mapping value
    df['TAXP'].replace(mapping,inplace=True)

    # create the scatter plot
    ax = fig.add_subplot(2, 2, 4)
        
    # Create the scatterplot between TAXP and VALP with colormap MRGP and 
    # marker size set to WGTP
    plt.scatter(df['VALP'],df['TAXP'],c=df['MRGP'],s=df['WGTP'],alpha=0.25,cmap='seismic')
    
    # Set the tick marks as shown on the png file
    plt.colorbar(ticks=[0,1250,2500,3750,5000]).set_label('First Mortgage Payment (Monthly $)')
    plt.ylim(ymin=0,ymax=11000)
    plt.xlim(xmin=0,xmax=1200000)

    # add labels and title
    plt.xlabel('Taxes ($)')
    plt.ylabel('Property Value ($)')
    plt.title(y = 1.0, s='Property Taxes vs. Property Values', fontsize='small')

def main():
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

if __name__ == "__main__":
    print("CPSC-51100, Summer 2018")
    print("Name: Don Cruver, Nicolas Cabaluna")
    print("PROGRAMMING ASSIGNMENT #6 \n")
    main()