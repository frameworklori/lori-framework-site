# 📢 WARNING: DEMO ONLY – NOT REAL PRICES. This is mock data for demonstration purposes only.
# ❌ Not connected to real GoodRx or Medicare API.

def get_price_by_drug(drug_name, csv_path):
import pandas as pd
df = pd.read_csv(csv_path)
row = df[df['Drug'].str.lower() == drug_name.lower()]
if row.empty:
return {}
return {
"USA": row["USA"].values[0],
"Japan": row["Japan"].values[0],
"India": row["India"].values[0],
}

def get_goodrx_price(drug_name="insulin", zip_code="10001"):
# 📢 DEMO MOCK DATA – Simulated GoodRx-like prices
return [
{"Pharmacy": "CVS Pharmacy", "Price": "$25.00"},
{"Pharmacy": "Walgreens", "Price": "$29.99"},
{"Pharmacy": "Walmart", "Price": "$22.50"},
{"Pharmacy": "Rite Aid", "Price": "$30.00"}
]
