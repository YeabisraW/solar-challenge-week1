"""
Utility plotting functions.
"""

import matplotlib.pyplot as plt

def plot_results(time, values, title="Solar Energy Output"):
    """
    Plot time series results.

    Args:
        time (list or pd.Series): Time points.
        values (list or pd.Series): Corresponding values to plot.
        title (str): Plot title.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(time, values, marker='o')
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Energy Output (W)")
    plt.grid(True)
    plt.show()
"""Utility functions."""
