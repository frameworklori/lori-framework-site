# Climate Resilience & Impact Matrix (RIM) – Scoring Logic

## Evaluation Dimensions
1. Productivity Loss (%)
2. Food Yield Reduction (%)
3. Water Stress Index (0–1)
4. Adaptation Capacity Index (0–1)

## Region Resilience Score (RRS)
```plaintext
RRS = (1 - ProductivityLoss%) × (1 - WaterStress) × AdaptationCapacity

Classification
RRS > 0.75: High resilience

RRS 0.50–0.75: Moderate resilience

RRS < 0.50: High vulnerability



Data Sources
FAO, IPCC, World Bank, local census and meteorological data


---

### 📄 `LORI-ECJ-UFI/ECJ_Index_Metadata.md`

```markdown
# Environmental Climate Justice (ECJ) Index – Metadata Tags

## Primary Ethical Factors
- Access Equity: Water, food, shade, shelter
- Historical Harm Compensation
- Indigenous Sovereignty
- Generational Burden Score (GBS)

## Usage
Each case tagged with:
- [ ] Climate Impact Type (e.g., Heatwave, Drought)
- [ ] Community Vulnerability Score (0–100)
- [ ] Reparative Priority: High / Medium / Low

## Data Fields
- Region Code
- Marginalized Group Type
- Impact Severity
- Reparative Action Score





