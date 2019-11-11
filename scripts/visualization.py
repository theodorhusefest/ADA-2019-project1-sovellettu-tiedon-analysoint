
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(); sns.set_style('whitegrid')
import folium
import json


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
        
        
def map_compare_areas(df, year, value, save = True, legend = 'NoLegend', filepath = 'geo/continents.json',):
    """
    Produces a choropleth map where darker color means higher value.
    
    params:
        df: pandas dataframe with data
        year: which year the values should be taken from
        value: parameter that decides color
        save: saves map as html file in the folder 'plots/maps'
        legend: unit of the plotted variable e.g 'Produced meat per 1000 capita'
        filepath: path to geojson file

    return:
        m: choropleth map
        
    
    """
    
    # Read json-geodata from file
    borders = json.load(open(filepath))
    
    # Initialize map
    m = folium.Map(location= (25,0), tiles='cartodbpositron' , zoom_start = 1.7, prefer_canvar=True)

    # Add boerds to map
    folium.GeoJson(borders).add_to(m)

    # Make choropleth map
    map_data = df[(df['Year'] == 1961)]
    m.choropleth(geo_data=borders, data=map_data,
             columns=['Area', value],
             key_on='feature.properties.CONTINENT',
             fill_color='BuPu', fill_opacity=0.6, line_opacity=0.2,
             legend_name='legend')
    
    if save:
        m.save('{}.html'.format(legend))
        
    return m