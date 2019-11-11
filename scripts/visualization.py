
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(); sns.set_style('whitegrid')
import folium


def plot_compare_areas(df, y, x = 'Year', title='NoTitle', save = False):
    """
    Plots one line per Area in df. 
    X-axis default Years, while y-axis has to be passed
    params:
        df: Pandas dataframe with data
        y: value to be plotted on y-axis. Must be a column in df
        x: value on x-axis. Default years
        title: chosen title on plot.

    
    """
    fig, ax = plt.subplots(figsize = (16,8))
    df_grouped = df.groupby(['Area'])
    
    for area, group in df_grouped:
        sns.lineplot(group[x], group[y], label=area, palette=('BuGn_r'))
    plt.legend()
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    
    if save:
        plt.savefig('./plots/{}.png'.format(title))
        
        
