# MedJustice Overview

This document provides an overview of the MedJustice project.

## 🔍 Purpose

To track insulin and contraceptive prices across countries (e.g., USA vs Japan/India), assess the impact of Medicaid cuts (OBBBA), and support undocumented communities with generic drug access and social cost prediction.

## 📁 Folder Structure

```
MedJustice/
├── data/                 # Drug price and prediction data (.csv/.json)
├── notebooks/            # Jupyter analysis notebooks
├── src/models/           # Public Python models (drug tracking, cost estimation)
├── flutter_app/          # Flutter UI prototype
├── overview.md           # Project overview (this file)
└── README.md             # Intro and license
```

## 🔗 Key Modules

- `drug_price_tracker.py`: Load and retrieve drug prices by country
- `plot_price_comparison.py`: Visual comparison of drug prices
- `demo_cost_prediction.ipynb`: Cost prediction demo using Hispanic and African American datasets
- `result_screen.dart`: Display prediction results from JSON
