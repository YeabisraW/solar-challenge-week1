"""
Dummy plot script for demonstration purposes.

Generates a simple line plot and saves it as a PNG file in the reports folder.
"""

import matplotlib.pyplot as plt

def generate_dummy_plot():
    """
    Generates and saves a dummy plot.
    
    - X values: [1, 2, 3]
    - Y values: [4, 5, 6]
    - Saves plot to 'reports/dummy_plot.png'
    """
    x = [1, 2, 3]
    y = [4, 5, 6]

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, marker='o')
    plt.title("Dummy Plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)

    # Save the figure
    plt.savefig("reports/dummy_plot.png")
    plt.show()

if __name__ == "__main__":
    generate_dummy_plot()

