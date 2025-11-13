"""
solar_features.py

This module provides functions to compute daily solar energy features
from cleaned solar datasets. It is designed to be imported and used
by other scripts or notebooks.
"""

import pandas as pd

def compute_daily_mean(df, column):
    """
    Compute the daily mean of a specified column in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned solar dataset with a 'Timestamp' column.
    column : str
        The name of the column to compute daily mean for (e.g., 'GHI').

    Returns
    -------
    pd.DataFrame
        DataFrame with 'Date' and daily mean of the specified column.
    
    Example
    -------
    >>> df_daily = compute_daily_mean(df, 'GHI')
    """
    df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
    daily_mean = df.groupby('Date')[column].mean().reset_index()
    daily_mean.rename(columns={column: f'{column}_daily_mean'}, inplace=True)
    return daily_mean

def compute_daily_max(df, column):
    """
    Compute the daily maximum of a specified column.

    Parameters
    ----------
    df : pd.DataFrame
        The cleaned solar dataset with a 'Timestamp' column.
    column : str
        Column name to compute daily max (e.g., 'DNI').

    Returns
    -------
    pd.DataFrame
        DataFrame with 'Date' and daily max of the specified column.
    
    Example
    -------
    >>> df_daily_max = compute_daily_max(df, 'DNI')
    """
    df['Date'] = pd.to_datetime(df['Timestamp']).dt.date
    daily_max = df.groupby('Date')[column].max().reset_index()
    daily_max.rename(columns={column: f'{column}_daily_max'}, inplace=True)
    return daily_max

def merge_daily_features(*dfs):
    """
    Merge multiple daily feature DataFrames into a single DataFrame.

    Parameters
    ----------
    *dfs : pd.DataFrame
        Multiple daily feature DataFrames (with 'Date' column).

    Returns
    -------
    pd.DataFrame
        Single DataFrame with all daily features merged on 'Date'.
    
    Example
    -------
    >>> df_merged = merge_daily_features(df_ghi, df_dni)
    """
    from functools import reduce
    df_merged = reduce(lambda left, right: pd.merge(left, right, on='Date'), dfs)
    return df_merged
