# Solar Challenge Week 1

## Project Overview

This project is part of the AI Mastery training. It implements a modular Python package for solar energy analysis with a structured approach including data handling, modeling, plotting, and testing. The aim is to provide clean, reusable code and demonstrate progress on the challenge requirements.

---

## Folder Structure

```
solar-challenge-week1/
│
├─ src/                 # Python modules and scripts
│  ├─ data/             # Data handling and cleaning scripts
│  │   ├─ clean_data.py
│  │   └─ data_loader.py
│  ├─ models/           # Solar analysis models
│  │   └─ solar_model.py
│  ├─ analysis/         # Feature extraction and processing
│  │   └─ solar_features.py
│  ├─ utils/            # Utility functions and plotting
│  │   └─ plot_utils.py
│  └─ main.py           # Main script to run the analysis
│
├─ data/                # Input datasets (CSV files)
├─ notebooks/           # Jupyter notebooks for EDA
├─ reports/             # Generated plots and reports
├─ tests/               # Unit tests for the modules
├─ .github/workflows/   # CI/CD workflow files
├─ requirements.txt     # Python dependencies
└─ .gitignore           # Ignored files
```

---

## Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the main analysis

```bash
python src/main.py
```

This runs the full pipeline: loads data, cleans it, performs analysis, and saves plots and results in the `reports/` folder.

### Run Jupyter notebooks

```bash
jupyter notebook notebooks/<notebook_name>.ipynb
```

### Run tests

```bash
pytest tests/
```

---

## CI/CD

* GitHub Actions are set up for automated testing and linting.
* All commits must pass tests before merging to the main branch.

---

## Contributing

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature-name
```

3. Write clean, documented code and add tests.
4. Commit with descriptive messages.
5. Submit a pull request for review.

---

## License

MIT License

---

## Contact

* Maintainer: Yeabisra Wubishet
* GitHub: https://github.com/YeabisraW/solar-challenge-week1
* Email: wubyab@gmail.com
