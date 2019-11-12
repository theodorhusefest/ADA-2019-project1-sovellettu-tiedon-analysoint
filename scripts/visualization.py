
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(); sns.set_style('whitegrid')
import folium
import json

from bokeh.plotting import figure, output_file, output_notebook, show
from bokeh.models import ColumnDataSource
from bokeh.themes import Theme
from bokeh.io import curdoc

    
theme = Theme(filename = './bokeh_theme.yaml')
curdoc().theme = theme



def plot_compare_areas(df, y, x = 'Year', title = 'NoTitle', save_png = False):
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
    
    fig, ax = plt.subplots(figsize = (16,8))
    df_grouped = df.groupby(['Area'])
    
    for area, group in df_grouped:
        sns.lineplot(group[x], group[y], label=area, palette=('BuGn_r'))
    plt.legend()
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    
    if save_png:
        plt.savefig('./plots/{}.png'.format(title))

        
        

def bokeh_compare_areas(df, y, x = 'Year', title = 'NoTitle', save_html = False):
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
    if save_html:
        output_file('{}.html'.format(title))
    
    colors = ['#32e6a1', '#92c64c', '#c69e15', '#e56b30', '#e63262']
    output_notebook()
    
    df_grouped = df.groupby(['Area'])
    
    p  = figure(title=title, x_axis_label = x, y_axis_label = y, plot_width = 900, plot_height = 500)
    
    for (area, group), color in zip(df_grouped, colors):
        p.line(group[x], group[y], legend = area, line_color = color, line_width=3)
        
    show(p)
        
        

        
def map_compare_areas(df, year, value, save_html = True, legend = 'NoLegend', filepath = 'geo/continents.json',):
    """
    Produces a choropleth map where darker color means higher value.
    
    params:
        df: pandas dataframe with data
        year: which year the values should be taken from
        value: parameter that decides color
        save_html: saves map as html file in the folder 'plots/maps'
        legend: unit of the plotted variable e.g 'Produced meat per 1000 capita'
        filepath: path to geojson file

    return:
        m: choropleth map
    """
    
    # Read json-geodata from file
    borders = json.load(open(filepath))
    
    # Initialize map
    m = folium.Map(location= (25,0), tiles='cartodbpositron' , zoom_start = 1.7, prefer_canvar=True)

    # Add borders to map
    folium.GeoJson(borders).add_to(m)

    # Make choropleth map
    map_data = df[(df['Year'] == year)]
    m.choropleth(geo_data=borders, data=map_data,
             columns=['Area', value],
             key_on='feature.properties.CONTINENT',
             fill_color='BuPu', fill_opacity=0.6, line_opacity=0.2,
             legend_name='legend')
    
    if save_html:
        m.save('{}.html'.format(legend))
        
    return m