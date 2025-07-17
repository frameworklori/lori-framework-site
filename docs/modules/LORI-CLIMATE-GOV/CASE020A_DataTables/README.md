# CASE020A_DataTables – California Water Ethics & Fire Risk Dataset (W1–W9)

This folder contains nine structured CSV/Markdown files representing the core water use, conflict, and infrastructure variables for LORI Framework CASE-020A: California Water Ethics × Fire Risk Analysis.

## 📊 File Index (W1–W9)

| File Name | Title | Scope | Status |
|------------------------|----------------------------------------------|--------------------------------------------|---------------|
| W1_StructuralScarcity | Structural Groundwater Scarcity | Central Valley, South Coast | ✅ Generated |
| W2_AgriVsTribal | Agricultural vs Tribal Water Allocation | San Joaquin, Kern, Sacramento | ✅ Generated |
| W3_FireConflict | Fire Emergency Water Conflict Zones | Butte, Tule River, San Joaquin | ✅ Generated |
| W4_ReclaimedSystems | Recycled Water Infrastructure Access | LA, SF, Central Valley, Tribal | ✅ Generated |
| W5_HouseholdWaterUse | Per Capita & Annual Household Use | SF Bay, South Coast, Sacramento | ✅ Generated |
| W6_IndustrialWaterUse | Industrial Water Use by Sector | Food, Refining, Cement, Lithium | ✅ Generated |
| W7_OilShaleExtraction | Water Use in Fracking & Oil Fields | Kern, Belridge, Lost Hills | ✅ Generated |
| W8_EnergyFacilitiesUse | Water Use in Energy Production (Thermo/Hydro)| Southern CA, Delta, Hoover region | ⏳ Pending |
| W9_UrbanWaterUse | Urban Public Water Use Efficiency | SF, LA, Sacramento | ⏳ Pending |

> 📌 *Files W8 and W9 will be finalized once updated data from USGS / DWR 2025 is retrieved.*

---

## 🛠️ Source and Validation

- **Primary Sources**:
- California Department of Water Resources (DWR)
- USGS California Water Science Center
- CalFire, CalGEM, DOGGR, LADWP, SFPUC
- Tribal community reports (Tule River, 2025)

- **Data Range**: 2010–2023 (most estimates), with 2024–2025 projections flagged
- **Validation Pending**: Official 2025 UWMPs, SGMA reports, and CalGEM datasets will be required to confirm and calibrate most values

---

## ⚠️ Data Risk Advisory

- Many entries are **estimate-based**, not full empirical datasets
- Fracking, tribal, and wildfire-related data may **underreport structural inequities**
- Conflicts noted are contextual and not universally verified
- All CSV/MD tables include "Source_Year" and "Notes" fields to aid post-validation

---

## 🔗 Cross-Module Interoperability

- 🔍 Use with:
- `LORI-ECJ-UFI/ECJ_Index_Metadata.md` – Environmental Justice weighting
- `LORI-RIM/ClimateResilience_ScoringLogic.md` – Resilience & infrastructure impact
- `LORI-JURY-CASES/CASE020A_CaliforniaWaterEthics.md` – Ethical simulation file
- `ClimateGov_Modules.md` – For integration map and governance modules

- 📂 Related CASEs:
- `CASE-020B` – Tribal Water Sovereignty
- `CASE-021` – Indigenous Water Ethics (West)
- `CASE-022` – Climate Justice × Infrastructure Delay

---

## ✅ Maintainer Notes

- Last updated: **2025-07-17**
- Maintainer: **LORI Framework Dispatch**
- Contact: `dispatch@lori-framework.eth` (fictional placeholder)
