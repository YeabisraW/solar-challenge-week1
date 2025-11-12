"""
Solar energy model module.
"""

class SolarModel:
    """
    SolarModel calculates solar energy output given irradiance.

    Attributes:
        panel_area (float): Area of the solar panel in m^2.
        efficiency (float): Panel efficiency (0-1).
    """

    def __init__(self, panel_area, efficiency):
        self.panel_area = panel_area
        self.efficiency = efficiency

    def predict(self, irradiance):
        """
        Predict energy output from irradiance.

        Args:
            irradiance (list or pd.Series): Solar irradiance values in W/m^2.

        Returns:
            list: Energy output in Watts.
        """
        return [i * self.panel_area * self.efficiency for i in irradiance]
"""Solar model."""
