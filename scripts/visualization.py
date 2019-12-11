
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


        

def bokeh_compare_areas(df, y, x = 'Year', title = 'NoTitle', save_html = False):
    """    
    Produces an interactiv plot with comparison on area-level.
    Uses Bokeh, and is Save_html is active it saves directly to website-folder.
    X-axis default Years, while y-axis has to be passed
    
    params:
        df: pandas dataframe with data
        y: value to be plotted on y-axis. Must be a column in df
        x: value on x-axis. Default years
        title: chosen title on plot.
        save_html: saves a png of plot in plots, and filename is title
    """
    
    if save_html:
        output_file('./website/layouts/partials/{}.html'.format(title))
    else: 
        reset_output()
    
    # Set theme and colors to use
    theme = Theme(filename = './visual/bokeh_theme.yaml')
    curdoc().theme = theme
    colors = ['#32e6a1', '#92c64c', '#c69e15', '#e56b30', '#e63262']
    
    output_notebook()
    
    df_grouped = df.groupby(['Area'])
    
    p  = figure(title=title, x_axis_label = x, y_axis_label = y, plot_width = 900, plot_height = 500)
    
    for (area, group), color in zip(df_grouped, colors):
        p.line(group[x], group[y], legend = area, line_color = color, line_width=3)
        
    p.legend.orientation = "horizontal"
    show(p)
        
        

        
def map_compare_areas(df, year, value, save_html = True, legend = 'NoLegend', filepath = './visual/geo/continents.json',):
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
    m = folium.Map(location= (25,0), 
                   width= '95%',
                   height= '80%',
                   tiles= 'cartodbpositron', 
                   zoom_start= 1.5,)

    # Add borders to map
    folium.GeoJson(borders).add_to(m)

    # Make choropleth map
    map_data = df[(df['Year'] == year)]
    m.choropleth(geo_data=borders, data=map_data,
             columns= ['Area', value],
             key_on= 'feature.properties.CONTINENT',
             fill_color= 'BuPu', fill_opacity=0.6, line_opacity=0.2,
             legend_name= legend)
    
    if save_html:
        m.save('./website/layouts/partials/{}.html'.format(legend))
        
    return m


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