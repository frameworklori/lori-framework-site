# MedJustice – Drug Price × Social Cost Tracker

MedJustice is a Python + Flutter prototype that tracks international drug price disparities and predicts emergency and education costs associated with Medicaid access (e.g., OBBBA cuts), undocumented immigrant status, and fertility trends.

## 🔍 Purpose

To advocate for healthcare justice by:
- Comparing U.S. vs. Japan/India drug prices (e.g., insulin, contraceptives)
- Predicting ER and K–12 education cost burdens by ethnicity
- Supporting undocumented or marginalized groups with generic drug access
- Promoting awareness of policy-driven health inequities (e.g., OBBBA)

## 📁 Project Structure
medjustice/

├── data/                 # drug_prices.csv, predicted_costs.json

├── notebooks/            # Jupyter: demo_cost_prediction.ipynb

├── src/models/           # Python: drug_price_tracker.py, cost estimator

├── flutter_app/          # Dart UI: main.dart, price/result screens

├── overview.md           # Project overview & goals

└── README.md             # This file

## 🛠 Key Features

- 📉 **Price Tracker**: U.S. vs. India/Japan drug price disparity
- 📊 **Social Cost Predictor**: ER & education spending for Hispanic & African American groups
- 📱 **Undocumented-Friendly UI**: Flutter prototype with Spanish support & no-login design

## 🔗 Sample Datasets

- [`drug_prices.csv`](./data/drug_prices.csv)
- [`predicted_costs.json`](./data/predicted_costs.json)

## 🧠 Analysis

Check [`demo_cost_prediction.ipynb`](./notebook/demo_cost_prediction.ipynb) for predictive modeling using linear regression.

## 🧩 UI Prototype (Flutter)

The Flutter UI includes:
- Home navigation
- Drug price screen
- Predicted social costs viewer (`assets/predicted_costs.json`)

## 📄 License

MIT License © MedJustice Project (Public Health Advocacy)





