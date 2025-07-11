# ClimatePolicySim_InputData.md
## 📊 Climate Policy Simulation – Input Dataset for CASE-020

This file provides baseline data for simulating climate resource allocation trade-offs across different regions under extreme weather conditions. The focus is on labor safety, food security, and resilience modeling across high-heat and low-temperature scenarios in five selected regions.

---

### 🌍 Region Profiles & Sectoral Data

| Region | Climate Profile | Sector | Temp Threshold (°C) | Productivity Loss (%) | Labor Population | Crop Loss Rate (%) | Water Stress Score | RIM Resilience Score |
|----------------|---------------------|---------------|----------------------|------------------------|-------------------|---------------------|---------------------|-----------------------|
| Taiwan | Subtropical, humid | Agriculture | 35°C | 28% | 320,000 | 15% | 0.52 | 0.66 |
| South Asia | Monsoon, hot | Agriculture | 40°C | 35% | 7,200,000 | 40% | 0.73 | 0.48 |
| Southern U.S. | Arid-subtropical | Construction | 38°C | 30% | 1,850,000 | — | 0.47 | 0.72 |
| Kuwait | Desert, hyper-arid | Construction | 42°C | 42% | 600,000 | — | 0.91 | 0.35 |
| Mongolia | Subarctic, dry | Agriculture | -20°C (Winter) | 33% | 260,000 | 18% | 0.36 | 0.58 |

---

### 🧾 Notes:
- **Temp Threshold**: Critical temperature above (or below) which productivity loss begins.
- **Productivity Loss (%)**: Estimated output reduction under climate stress.
- **Water Stress Score**: Higher values indicate greater water scarcity pressure.
- **RIM Score**: Normalized Resilience & Impact Matrix score from 0–1 (higher is more resilient).
- Crop loss data for construction sector is not applicable (—).

---

### 🧭 Source Guidance
Data derived from preliminary synthesis of:
- ILO & FAO datasets on heat stress and labor impacts
- IPCC regional climate projections
- World Bank water security reports
- Case-specific assumptions validated by LORI Framework

---

### ✅ Prepared For:
Grok × LORI Climate Co-Governance Simulation
CASE-020: Labor Resource Ethics in Heatwave Scenarios
Linked Modules: ECJ, RIM, Jury System, GHLI
