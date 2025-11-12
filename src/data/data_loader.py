"""
Data loading utilities.
"""

import pandas as pd

def load_data(filepath):
    """
    Load CSV data into a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return pd.DataFrame()
"""Handles data loading."""
