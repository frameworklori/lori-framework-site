# ClimatePolicySim_InputData.md

**Module Reference**: CASE-020 × Heatwave × High-Sensitivity Industry Simulation
**Prepared by**: LORI Framework Coordination Team
**Date**: 2025-07-16
**Purpose**: Provide structured simulation input data for Grok’s dual-axis visualization and CASE-020 heatwave impact analysis.

---

## 🌍 Regions & Key Metrics

| Region | Agriculture Loss (%) | Construction Loss (%) | Food Yield ↓ (%) | Water Stress Index | RIM Score |
|--------------|----------------------|------------------------|------------------|--------------------|-----------|
| **Taiwan** | 12 | 8 | 10–15 | 0.42 | 0.71 |
| **South Asia** | 18 | 22 | 20–40 | 0.68 | 0.53 |
| **Southern US** | 9 | 15 | 5–10 | 0.36 | 0.75 |
| **Kuwait** | 25 | 30 | 45–55 | 0.91 | 0.41 |
| **Mongolia** | 5 | 3 | 2–6 | 0.33 | 0.84 |

**Note**:
- Water Stress Index: 0 = low stress, 1 = extreme stress
- RIM Score: Calculated per `ClimateResilience_ScoringLogic.md`
- Food Yield loss is projected over 5–10 year trends based on FAO and IPCC regional data

---

## 🌡️ Temperature Threshold Simulation Table

| Temperature (°C) | Avg Productivity Loss (%) | Health Risk Index | Water Stress Score |
|------------------|---------------------------|-------------------|--------------------|
| 30°C | 12% | 0.28 | 0.62 |
| 35°C | 25% | 0.47 | 0.75 |
| 40°C | 41% | 0.71 | 0.88 |

---

## 🧑‍🌾 Industry-Specific Risk Factors

| Industry | 30°C Loss | 35°C Loss | 40°C Loss | Vulnerability Index |
|----------------|-----------|-----------|-----------|----------------------|
| Agriculture | 15% | 28% | 43% | 0.82 |
| Construction | 10% | 21% | 38% | 0.74 |
| Fisheries | 8% | 16% | 27% | 0.65 |
| Livestock | 12% | 23% | 35% | 0.71 |

---

## 👥 Age-Based Sensitivity Modifiers

| Age Group | Risk Amplifier | Avg Health Downtime (days/year) |
|------------------|----------------|----------------------------------|
| 15–35 (Working) | 1.0× | 12 |
| 36–55 (Core Labor)| 1.3× | 19 |
| 56+ (Elderly) | 1.8× | 28 |

---

## 🚰 Integrated Water Use Module (CASE-020A Extension)

This input dataset now incorporates water ethics factors from **California-specific simulation (CASE-020A)** with structured data from:

- [`W5_HouseholdWaterUse.csv`](./CASE020A_DataTables/W5_HouseholdWaterUse.csv) – Home use by region, per-capita daily gallons, year-based comparison

- [`W6_IndustrialWaterUse.csv`](./CASE020A_DataTables/W6_IndustrialWaterUse.csv) – Industrial sectors such as food processing, manufacturing, oil refining

- [`W7_OilShaleExtraction.csv`](./CASE020A_DataTables/W7_OilShaleExtraction.csv) – Hydraulic fracturing & steam injection water use

- [`W8_EnergyFacilitiesUse.csv`](./CASE020A_DataTables/W8_EnergyFacilitiesUse.csv) – Thermoelectric & hydropower facility water use

- [`W9_UrbanWaterUse.csv`](./CASE020A_DataTables/W9_UrbanWaterUse.csv) – Composite urban water use data by region and density

These files support comparative modeling of human consumption, industrial pressure, fire preparedness, and reclaimed system ethics.

---

## 🏷️ Metadata Tags

- `heatwave-ethics`

- `industry-productivity-loss`

- `climate-vulnerability-model`

- `high-risk-occupation`

- `age-modifier-index`

- `RIM-score-compatible`

- `california-water-conflict`

- `urban-vs-industrial-consumption`

---

## 📩 Notes for Simulation (Grok)

- Data supports dual-axis chart (Temperature × Productivity loss).  

- Can be mapped by region or industry.  

- RIM scores enable integration with `ClimateResilience_ScoringLogic.md` for impact modeling.  

- Age-based modifiers can be layered for demographic-specific projections.  

- Water resource input extends equity & policy dimensions for CASE-020A deliberations.


**End of Document**

