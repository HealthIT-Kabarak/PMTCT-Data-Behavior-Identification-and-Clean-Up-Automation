# Script to automate the cleaning of the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

# Using a function to clean the data
def clean_data(df):
    # Dropping the columns that are not needed
    df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Unnamed: 0.1.1', 'Unnamed: 9'], axis=1, inplace=True)
    # Dropping the rows that are not needed
    df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], inplace=True)
    # Dropping the rows that have no values
    df.dropna(how='all', inplace=True)
    
    # Renaming the columns
    df.rename(columns={'Unnamed: 1': 'Country', 'Unnamed: 2': 'Year', 'Unnamed: 3': 'Status', 'Unnamed: 4': 'Life expectancy', 'Unnamed: 5': 'Adult Mortality', 'Unnamed: 6': 'Infant deaths', 
    'Unnamed: 7': 'Alcohol', 'Unnamed: 8': 'Percentage expenditure'}, inplace=True)

    
    # Changing the data type of the columns
    df['Year'] = df['Year'].astype('int')

    return df
    df = clean_data(df)