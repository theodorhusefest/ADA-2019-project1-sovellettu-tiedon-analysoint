""" Contains functions that are commonly used in project """

import pandas as pd
import numpy as np



def split_fao_data(df):
    """
    Function that splits data into countries, areas and continents.
    params:
        df: fao-dataframe that includes area codes.
        
    returns:
        countries: dataframe with area-code < 500
        area: dataframe with only area-code > 500
        continents: dataframe with the 6 continents
    
    """
    
    countries = df[df['Area Code'] < 500]
    area = df[df['Area Code'] > 500]
    
    continents = ['Africa', 'Northern America', 'South America', 'Asia', 'Oceania', 'Europe']
    continents = df[df['Area'].isin(continents)]
    
    # Reset index on each of the dataframes, and drop the old indexes
    countries = countries.reset_index().drop('index', axis = 1)
    area = area.reset_index().drop('index', axis = 1)
    continents = continents.reset_index().drop('index', axis = 1)

    return countries, area, continents


def explain_df(df):
    """
    Prints a quick summary of the dataframe
    params:
        df: fao-dataframe with columns [Area, Year, Item, Element, Unit]
    """
    
    print('The data contain(s) the following: ') 
    print(f'    area(s)    : {(df.Area.unique().tolist())}')
    print(f'    years      : {(df.Year.min())} - {df.Year.max()}')
    print(f'    item(s)    : {(df.Item.unique().tolist())}')
    print(f'    elements(s): {(df.Element.unique().tolist())}')
    print(f'    unit(s)    : {(df.Unit.unique().tolist())}')
