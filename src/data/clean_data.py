"""
clean_data.py

This script loads a CSV dataset, performs basic cleaning (fills missing values),
and saves the cleaned dataset. It is designed to be run independently of the notebook.
"""

import pandas as pd

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Fill missing values with column means."""
    return df.fillna(df.mean())

def save_data(df, output_path):
    """Save DataFrame to CSV."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    # Replace 'your_file.csv' with your CSV filename
    input_file = "../../data/benin-malanville.csv"
    output_file = "../../data/benin-cleaned_data.csv"

    data = load_data(input_file)
    print("Original data info:")
    print(data.info())
    
    cleaned = clean_data(data)
    save_data(cleaned, output_file)
