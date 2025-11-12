"""
Script to load, clean, and export datasets.
"""

import pandas as pd

def clean_dataset(input_path, output_path):
    """
    Load CSV, clean missing values, and save cleaned CSV.

    Args:
        input_path (str): Path to raw CSV.
        output_path (str): Path to save cleaned CSV.
    """
    df = pd.read_csv(input_path)
    df_clean = df.fillna(df.mean())
    df_clean.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_dataset("../data/your_file.csv", "../data/cleaned_data.csv")

