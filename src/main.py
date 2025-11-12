"""
Main entry point for the Solar Challenge Week 1 project.

Demonstrates usage of data loading, modeling, and plotting modules.
"""

from src.data.data_loader import load_data
from src.models.solar_model import SolarModel
from src.utils.plot_utils import plot_results

def main():
    """
    Main function to run the solar energy analysis.
    Steps:
    1. Load input data
    2. Initialize the solar model
    3. Generate predictions
    4. Plot results
    """
    # Load dummy data (replace with real CSV in future)
    data = load_data("data/sample_data.csv")

    # Initialize solar model
    model = SolarModel(panel_area=10, efficiency=0.18)

    # Generate predictions
    predictions = model.predict(data['irradiance'])

    # Plot results
    plot_results(data['time'], predictions)

if __name__ == "__main__":
    main()
"""Main entry point."""
