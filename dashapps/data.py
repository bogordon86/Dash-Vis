"""Prepare data for Plotly Dash."""
import pandas as pd
import numpy as np


def create_dataframe():
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv('2020_StormEvents_details_NOAA_20201117.csv', parse_dates=['BEGIN_DATE_TIME'])
    df['BEGIN_DATE_TIME'] = df['BEGIN_DATE_TIME'].dt.date
    df.drop(columns=['BEGIN_TIME', 'END_TIME'], inplace=True)
    #num_complaints = df['complaint_type'].value_counts()
    #to_remove = num_complaints[num_complaints <= 30].index
    #df.replace(to_remove, np.nan, inplace=True)
    return df
