""" Contains functions that are commonly used in project """

import pandas as pd
import numpy as np


#**************** Clean data *****************

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

    return countries, area, continents