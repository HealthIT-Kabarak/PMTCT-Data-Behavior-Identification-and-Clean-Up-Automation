# Script to automate the cleaning of the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

# Read in the data
df = pd.read_csv('data.csv')

# Create function to clean the data
def clean_data(df):

    # Drop the unnamed column
    df.drop('Unnamed: 0', axis=1, inplace=True)

    # Drop the duplicates   
    df.drop_duplicates(inplace=True)

    # Drop the rows with missing values
    df.dropna(inplace=True)

    return df

clean_data = clean_data(df)
