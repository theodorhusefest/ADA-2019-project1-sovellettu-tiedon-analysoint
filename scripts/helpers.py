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


def normalize_on_population(df1, population):
    """
    Adds an extra column to dataframe 'Norm Value' which is value of df1 divided by population in that area
    """
    
    # Join meat and population dataframes
    df = df1.merge(population, on = ['Area','Year'])

    # Rename the columns
    new_names = {'Unit_x': 'Unit', 'Value_x': 'Value', 'Value_y': 'Population', 'Unit_y': 'Population Unit'}
    df.rename(columns = new_names, inplace = True)

    # Add a new column with value per population
    df['Norm Value'] = df['Value']/(df['Population']* 1000)
    
    df = df.drop(['Population Unit', 'Area Code' ,'Area Code_y', 'Area Code_x'], axis = 1, errors='ignore')
    
    return df


def center_around_average(df, columns):
    """
    Substracts the mean of each column in params from the same column
    """
    df1 = df.copy(deep=True)
    for col in columns:
        df1[col] -= np.mean(df1[col])
        
    return df1, df.mean()


def percentage_growth(df1, df2, columns):
    """
    Calulates how much of each row contribues to total growth
    """
    df = df1.copy(deep= True)
    for col in columns:
        diff = df1[col]-df2[col]
        df[col] = diff/diff.sum()

    return df
    


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

    
def merge_crops_and_meats(meat, crops):
    """
    Merges crops and meat and adds a extra column Total Production = Crops + Meats
    Keeps only Meats, Total and Crops, Total
    """
    
    food_cont = meat.merge(crops, on= ['Area', 'Year'])
    
    # Remove all useless columns
    food_cont = food_cont.drop(['Element Code_x', 'Element_x', 'Item Code',
                    'Flag_x', 'Flag_y' ,'Element Code_y', 
                    'Unit_y', 'Element_y', 'Population_y'], axis = 1, errors = 'ignore')
    
    new_names = {'Unit_x': 'Unit', 'Value_x': 'Meat', 
                 'Value_y': 'Crops', 'Norm Value_x': 'Norm Meat', 'Norm Value_y': 'Norm Crops', 'Item_y': 'Crops Item', 
                 'Item_x': 'Meat Item', 'Population_x': 'Population'}

    food_cont = food_cont.rename(columns = new_names)
    # Only keeps totals
    food_total = food_cont[(food_cont['Meat Item'] == 'Meat, Total') & (food_cont['Crops Item'] == 'Crops, Total')]

    # Add extra column
    food_total['Total Production'] = (food_total['Meat'] +  food_total['Crops'])
    food_total['Norm Total Production'] = (food_total['Meat'] +  food_total['Crops'])/(food_total['Population']*1000)
    
    return food_total
