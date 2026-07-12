# Telco Customer Churn Analysis

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An exploratory data analysis and machine-learning project for understanding and predicting customer churn in a telecommunications setting. The project combines customer demographics, account details, service subscriptions, and billing information to identify churn patterns and establish a baseline predictive workflow.

## Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Business Objectives](#business-objectives)
- [Dataset Overview](#dataset-overview)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Model Performance](#model-performance)
- [Business Insights](#business-insights)
- [Dashboard](#dashboard)
- [Installation](#installation)
- [Usage](#usage)
- [Repository Roadmap](#repository-roadmap)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Overview

Customer churn directly affects recurring revenue and acquisition costs. This repository examines historical telecom customer data to explore which customer, service, contract, and billing characteristics are associated with churn. It also trains baseline classification models that can support customer-retention prioritization.

The primary analysis is implemented in [`notebooks/TelcoChurn.ipynb`](notebooks/TelcoChurn.ipynb). A companion project report is available at [`reports/Telco_Churn_Report.pdf`](reports/Telco_Churn_Report.pdf).

## Business Problem

Telecom providers need to identify customers who are likely to discontinue their service before they leave. Without a structured churn-analysis process, retention teams may apply interventions too broadly, too late, or to customers with low churn risk.

This project frames churn as a binary classification problem: use available customer information to estimate whether a customer will churn, while exploring the patterns that can inform retention strategy.

## Business Objectives

- Explore the distribution of customer churn and its relationship with key customer attributes.
- Examine churn across contract types, tenure, gender, monthly charges, and service characteristics.
- Prepare a reproducible baseline dataset for supervised learning.
- Train and compare baseline churn-classification models.
- Provide a foundation for retention-oriented dashboards and decision support.

## Dataset Overview

The raw dataset is stored in [`data/raw/Telco-Customer-Churn.csv`](data/raw/Telco-Customer-Churn.csv). It contains **7,042 customer records** and **21 columns**, including the target variable `Churn`.

| Category | Example fields |
| --- | --- |
| Customer profile | `gender`, `SeniorCitizen`, `Partner`, `Dependents` |
| Account details | `tenure`, `Contract`, `PaperlessBilling`, `PaymentMethod` |
| Services | `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `TechSupport`, streaming services |
| Billing | `MonthlyCharges`, `TotalCharges` |
| Identifier and target | `customerID`, `Churn` |

During preprocessing, the notebook removes `customerID`, converts `TotalCharges` to numeric values, and imputes invalid or blank values with the median before encoding categorical features.

## Project Architecture

```text
Raw customer data
      |
      v
Data validation and preprocessing
      |
      +--> Exploratory data analysis and visualizations
      |
      v
Feature matrix and churn target
      |
      v
Train/test split and feature scaling
      |
      v
Baseline models (Logistic Regression, Random Forest)
      |
      +--> Evaluation visualizations
      |
      +--> Interactive exploratory dashboard charts
```

## Project Structure

```text
telco-churn-analysis/
├── data/
│   └── raw/
│       └── Telco-Customer-Churn.csv    # Source dataset
├── notebooks/
│   └── TelcoChurn.ipynb                # EDA, modeling, and dashboard exploration
├── reports/
│   └── Telco_Churn_Report.pdf          # Project report
├── src/
│   ├── data/                           # Data-related modules
│   ├── features/                       # Feature-engineering modules
│   ├── models/                         # Modeling modules
│   ├── utils/                          # Shared utilities
│   └── visualization/                  # Visualization modules
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

## Technologies Used

- **Python** for analysis and modeling
- **pandas** and **NumPy** for data manipulation
- **Matplotlib** and **Seaborn** for exploratory visualizations
- **scikit-learn** for preprocessing, model training, and evaluation
- **Plotly Express** for interactive charts
- **Jupyter Notebook** for the end-to-end analysis workflow

## Machine Learning Workflow

1. Load the raw CSV dataset.
2. Explore churn distribution and relationships between churn and selected features.
3. Remove the customer identifier and clean `TotalCharges`.
4. Encode categorical variables with `LabelEncoder`.
5. Separate the feature matrix from the `Churn` target.
6. Create an 80/20 train-test split using a fixed random state of `42`.
7. Standardize features with `StandardScaler`.
8. Train Logistic Regression and Random Forest baseline classifiers.
9. Evaluate predictions with accuracy, classification reports, and confusion matrices.
10. Compare model accuracy visually and explore selected relationships with Plotly.

## Model Performance

Model metrics are intentionally not reported here until they are recorded from a reproducible run of the notebook.

| Model | Accuracy | Precision | Recall | F1-score | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| Logistic Regression | _To be added_ | _To be added_ | _To be added_ | _To be added_ | Baseline implemented |
| Random Forest | _To be added_ | _To be added_ | _To be added_ | _To be added_ | Baseline implemented |

> Add the final evaluation metrics, test-set definition, and model-selection rationale after a reproducible experiment run.

## Business Insights

Business conclusions should be added only after validating the exploratory analysis and model outputs.

- **Churn profile:** _To be added_
- **Contract and tenure patterns:** _To be added_
- **Service and support patterns:** _To be added_
- **Billing and payment patterns:** _To be added_
- **Recommended retention actions:** _To be added_

## Dashboard

The notebook includes interactive Plotly views for churn distribution, contract type versus churn, and monthly charges versus churn.

<!-- Replace these placeholders with exported dashboard screenshots when available. -->

| Churn distribution | Contract type vs. churn |
| --- | --- |
| _Dashboard screenshot placeholder_ | _Dashboard screenshot placeholder_ |

| Monthly charges vs. churn |
| --- |
| _Dashboard screenshot placeholder_ |

## Installation

1. Clone the repository and enter the project directory:

   ```bash
   git clone <repository-url>
   cd telco-churn-analysis
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```

3. Install the analysis dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn plotly jupyter
   ```

   When dependency versions are pinned in `requirements.txt`, use:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the raw dataset is present at `data/raw/Telco-Customer-Churn.csv`.
2. Start Jupyter:

   ```bash
   jupyter notebook
   ```

3. Open `notebooks/TelcoChurn.ipynb` and run the cells in order.
4. If running locally, update the notebook's data-loading path to `../data/raw/Telco-Customer-Churn.csv` (or an appropriate path for your environment) before executing it.

## Repository Roadmap

- [x] Establish repository structure.
- [x] Add raw churn dataset.
- [x] Create notebook-based EDA and baseline modeling workflow.
- [x] Add exploratory and interactive dashboard charts.
- [ ] Record reproducible model metrics and experiment details.
- [ ] Modularize notebook logic into `src/` modules.
- [ ] Add automated tests and data-validation checks.
- [ ] Add dashboard exports and documented business recommendations.

## Future Improvements

- Use a preprocessing pipeline with appropriate categorical encoding and imputation.
- Evaluate models with churn-focused metrics such as recall, precision, F1-score, ROC-AUC, and PR-AUC.
- Address class imbalance where supported by exploratory evidence.
- Tune model hyperparameters and track experiments reproducibly.
- Add model explainability, calibration, and threshold analysis tied to retention costs.
- Develop a production-ready data pipeline and prediction interface.
- Add data versioning, tests, and continuous integration.

## License

This project is licensed under the [MIT License](LICENSE).
