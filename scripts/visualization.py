
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(); sns.set_style('whitegrid')
import folium
import json

from bokeh.plotting import figure, output_file, output_notebook, reset_output, show
from bokeh.models import ColumnDataSource
from bokeh.themes import Theme
from bokeh.io import curdoc



def plot_compare_areas(df, y, x = 'Year', y_label = 'Value', 
                       title = 'NoTitle', grouping = 'Area', figsize = (12,7), 
                       save_png = False, subplot = False, ax = None, outside = False):
    """
    Plots one line per Area in df. 
    X-axis default Years, while y-axis has to be passed
    
    params:
        df: pandas dataframe with data
        y: value to be plotted on y-axis. Must be a column in df
        x: value on x-axis. Default years
        title: chosen title on plot.
        save_png: saves a png of plot in plots, and filename is title
    """
    if not subplot:
        fig, ax = plt.subplots(figsize = figsize)
        
    df_grouped = df.groupby([grouping])

    for area, group in df_grouped:
        sns.lineplot(group[x], group[y], label=area, palette=('BuGn_r'))
    
    if outside:
        ax.legend(bbox_to_anchor=(1.04,1), loc="upper left")
    else:
        ax.legend()
    

    ax.set_title(title, fontsize = 14)
    ax.set_xlabel(x, fontsize = 14)
    ax.set_ylabel(y_label, fontsize = 14)
    
    if save_png:
        plt.savefig('./plots/{}.png'.format(title))




def plot_yearly(yearly_item, item, yearly_population, by = 'Area'):
    warnings.filterwarnings('ignore')
    fig, axs = plt.subplots(2, 2)
    
    yearly_population.sort_values(by = 'Year', inplace = True)
    groups = yearly_item[by].unique()
    world_year_population = yearly_population.groupby('Year').agg({'Value':'sum'}).reset_index()
    
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:pink']  
    fig.set_size_inches(15,12)

    plot_y = []
    for group in groups:
        y = yearly_item[yearly_item[by] == group].Value.values
        x = yearly_item[yearly_item[by] == group].Year.values
        
        axs[0,0].plot(x, y)
        
        if by == 'Area':
            y_n = yearly_item[yearly_item[by] == group].Value.values/(yearly_population[yearly_population[by] == group].Value.values*1000)
            axs[1,0].plot(x, y_n)

        plot_y.append(yearly_item[yearly_item[by] == cont].Value.values.tolist())

    axs[0,0].legend(groups)
    axs[0,0].set_title(item + ' production per continent')
    axs[0,0].set_xlabel('Year')
    axs[0,0].set_ylabel('Tonnes')
    axs[0,0].yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0}')) 

    axs[0,1].stackplot(x, np.vstack(plot_y), labels = groups, alpha=0.8)
    axs[0,1].legend(loc='upper left')
    axs[0,1].set_title('Total world '+ item +' production')
    axs[0,1].set_xlabel('Year')
    axs[0,1].set_ylabel('Tonnes')
    axs[0,1].yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0}'))
    
    if by == 'Area':
        
        axs[1,0].set_title(item + ' production per continent, normalized on continent population')
        axs[1,0].set_xlabel('Year')
        axs[1,0].set_ylabel('Tonnes')

        total_year_item = yearly_item.groupby('Year').agg({'Value':'sum'}).reset_index()

        axs[1,1].plot(total_year_item['Year'].values,
                total_year_item['Value'].values/(world_year_population['Value'].values*1000))
        axs[1,1].legend(['Total all continents'])
        axs[1,1].set_title('Total, normalized on population')
        axs[1,1].set_xlabel('Year')
        axs[1,1].set_ylabel('Tonnes')


def plot_crop_livestock(df1, df2, y, x = 'Year', y_label = 'Value', 
                       title1 = 'NoTitle', title2 = 'NoTitle2', figsize = (12,7), 
                       save_png = False, subplot = False, ax = None):
    """
    Plots one line per Area in df. 
    X-axis default Years, while y-axis has to be passed
    
    params:
        df: pandas dataframe with data
        y: value to be plotted on y-axis. Must be a column in df
        x: value on x-axis. Default years
        title: chosen title on plot.
        save_png: saves a png of plot in plots, and filename is title
    """
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(15,7)
    fig.subplots_adjust(wspace = 0.5)
        
    ax1.plot(df1[x], df1[y])
    ax2.plot(df2[x], df2[y])
    
    ax1.set_title(title1, fontsize = 14)
    ax1.set_xlabel(x, fontsize = 14)
    ax1.set_ylabel(y_label, fontsize = 14)
    
    ax2.set_title(title2, fontsize = 14)
    ax2.set_xlabel(x, fontsize = 14)
    ax2.set_ylabel(y_label, fontsize = 14)
    
    if save_png:
        plt.savefig('./plots/{}.png'.format(title))
        
        
        
def bar_plot(df1, df2, title, center=0):
    """
    Produces a bar plot for based on df made in question 3.
    """
    
    plt.figure(figsize = (10, 6))
    width = 0.3
    margin = 0.025
    meat_gain = 1
    
    p1 = plt.bar(df1.index, df1['Norm Meat']*meat_gain, width, color= 'b', zorder = 3)
    p2 = plt.bar(df1.index, df1['Norm Crops'], width, bottom = df1['Norm Meat']*meat_gain, color = '#eba134', zorder = 2)
    p3 = plt.bar(df2.index + width + margin, df2['Norm Meat']*meat_gain, width, color= 'b', zorder = 3)
    p4 = plt.bar(df2.index + width + margin, df2['Norm Crops'], width, bottom = df2['Norm Meat']*meat_gain,  color = '#eba134', zorder = 2)
    
    ticks = ['1961 2007 \n Africa', '1961 2007 \n Asia', 
             '1961 2007 \n Europe', '1961 2007 \n North America', 
             '1961 2007 \n Oceania', '1961 2007 \n South America']
    
    margin_y = 0.5
    step_size = 0.5
    
    xmin, xmax, ymin, ymax = plt.axis()
    ymin = -1
    plt.ylim([ymin, ymax])

    plt.xticks(df1.index + width/2, ticks, fontsize = 16)    
    plt.yticks(np.arange(ymin - margin_y, ymax + margin_y, step_size), 
               np.arange(np.around(center + ymin - margin_y, decimals = 1),
                         np.around(center + ymax + margin_y, decimals = 1), step_size), fontsize = 14)

    
    plt.ylabel('Production per person [tonnes]', fontsize = 16)
    plt.legend((p1[0], p2[0]), ('Meat Production', 'Crops Production'), fontsize = 16)
    plt.title(title, fontsize = 20)
    
    
def bar_plot_with_population(df, title):
    """
    Produces a bar plot with growth in population.
    """
    
    def autolabel(rects, pop_growth, left = False):
        for idx, rect in enumerate(rects):
            height = rect.get_height()
            if left:
                plt.text(rect.get_x() - rect.get_width()/2, height/2 - 0.01,
                        '{}%'.format(int(pop_growth[idx])),
                        ha='center', va='bottom', rotation=0)
            else:
                plt.text(rect.get_x() + rect.get_width()/2 + 0.27, height/2 - 0.01,
                        '{}%'.format(int(pop_growth[idx])),
                        ha='center', rotation=0)

    fig = plt.figure(figsize = (10, 5))
    width = 0.25
    margin = 0.025
    meat_gain = 1
    pop_gain = 1
    
    p1 = plt.bar(df.index, df['Total Production'],width, color= 'r')
    p2 = plt.bar(df.index + width + margin , df['Population'], width, bottom= 0 , color= 'g')
    
    autolabel(p1, df['Total Production']*100, left= True)
    autolabel(p2, df['Population']*100)
    
    ticks = ['Africa', 'Asia', 
             'Europe', 'North America', 
             'Oceania', 'South America']
    plt.xticks(df.index + width/2, ticks, fontsize = 14)
    
    xmin, xmax, ymin, ymax = plt.axis()
    plt.ylim([ymin-0.02,ymax])
    
    step_size = 0.1
    plt.yticks(np.arange(ymin, ymax, step_size), 
               ['{}%'.format(int(i)) for i in np.arange(ymin*100, ymax*100, step_size*100)])

    plt.legend((p1[0], p2[0]), ('Total Production Growth', 'Population Growth'), fontsize = 14)
    plt.title(title, fontsize = 16)
    
