# Solar Challenge Week 1

## Project Overview
This project is part of the AI Mastery training. It implements a modular Python package for solar energy analysis with a structured approach including data handling, modeling, plotting, and testing. The aim is to provide clean, reusable code and demonstrate progress on the challenge requirements.

## Folder Structure
solar-challenge-week1/
│
├─ src/ # Python modules and scripts
│ ├─ data/ # Data handling and cleaning scripts
│ │ ├─ clean_data.py
│ │ └─ data_loader.py
│ ├─ models/ # Solar analysis models
│ │ └─ solar_model.py
│ ├─ analysis/ # Feature extraction and processing
│ │ └─ solar_features.py
│ ├─ utils/ # Utility functions and plotting
│ │ └─ plot_utils.py
│ └─ main.py # Main script to run the analysis
│
├─ data/ # Input datasets (CSV files)
├─ notebooks/ # Jupyter notebooks for EDA
├─ reports/ # Generated plots and reports
├─ tests/ # Unit tests for the modules
├─ .github/workflows/ # CI/CD workflow files
├─ requirements.txt # Python dependencies
└─ .gitignore # Ignored files

## Setup
Create a Python virtual environment and install dependencies:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py
jupyter notebook notebooks/<notebook_name>.ipynb
pytest tests/
git checkout -b feature-name
```

## CI/CD
GitHub Actions are set up for automated testing and linting.
All commits must pass tests before merging to the main branch.

## Contributing
Fork the repository.
Create a new branch: git checkout -b feature-name
Write clean, documented code and add tests.
Commit with descriptive messages.
Submit a pull request for review.
Exploratory Data Analysis (EDA) and Cross-Country Comparison

Detailed data profiling, cleaning, and analysis of solar datasets for **Benin, Sierra Leone, and Togo**.

### Data Cleaning & Profiling
- Checked for missing values and outliers using **Z-scores**.
- Cleaned datasets were exported as CSV files in the `data/` folder.

### Visual Analysis
- Time series plots of **GHI, DNI, DHI** for each country.
- Correlation heatmaps to show relationships between solar metrics.
- Scatter plots and histograms to explore distributions and trends.

### Cross-Country Comparison
- Combined cleaned datasets to compare solar metrics across countries.
- Boxplots highlight differences in **GHI, DNI, DHI** between countries.
- Scatter plots visualize relationships and variations across countries.
- ANOVA statistical tests were performed to determine if differences are significant (p < 0.05).

### Outputs
- Updated EDA notebooks are in the `notebooks/` folder.
- Generated plots are saved in the `reports/` folder for reference.

## License
MIT License

## Contact
Maintainer: Yeabisra Wubishet
GitHub: https://github.com/YeabisraW/solar-challenge-week1
Email: wubyab@gmail.com
