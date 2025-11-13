"""
solar_features.py
-----------------
This module provides utility functions to extract key solar energy features
from cleaned CSV datasets such as GHI, DNI, and DHI.
"""

import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """Load a cleaned CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path, parse_dates=["Timestamp"])

def compute_daily_features(df: pd.DataFrame) -> pd.DataFrame:
    """Compute daily mean and peak solar radiation values."""
    df["Date"] = df["Timestamp"].dt.date
    daily = df.groupby("Date").agg({
        "GHI": ["mean", "max"],
        "DNI": ["mean", "max"],
        "DHI": ["mean", "max"]
    })
    daily.columns = ["_".join(col).strip() for col in daily.columns.values]
    return daily.reset_index()

def save_features(daily_df: pd.DataFrame, output_file: str):
    """Save the computed daily features to a CSV file."""
    daily_df.to_csv(output_file, index=False)
    print(f"✅ Saved daily features to {output_file}")

if __name__ == "__main__":
    input_file = "data/benin-malanville.csv"
    output_file = "data/benin_daily_features.csv"

    df = load_data(input_file)
    daily_features = compute_daily_features(df)
    save_features(daily_features, output_file)
