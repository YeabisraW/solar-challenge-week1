
# Solar Challenge Week 1

## Project Overview
This project is part of the AI Mastery training. It implements a modular Python package for solar energy analysis with a structured approach including data handling, modeling, plotting, and testing. The aim is to provide clean, reusable code and demonstrate progress on the challenge requirements.

## Folder Structure
- solar-challenge-week1/
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

---

## Setup

### 1. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
###Usage
#Run the main analysis
python src/main.py # This runs the full pipeline: loads data, cleans it, performs analysis, and saves plots and results in theCI/CD

#GitHub Actions are set up for automated testing and linting.

#All commits must pass tests before merging to the main branch. reports/ folder.

### This version is **complete, structured, and easy to follow** for anyone: it clearly explains setup, usage, testing, and contribution steps.  

