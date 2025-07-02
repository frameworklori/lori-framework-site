import pandas as pd

def load_drug_prices(file_path='public/data/drug_prices.csv'):
"""讀取藥品價格 CSV 檔案"""
df = pd.read_csv(file_path)
return df.set_index('country')

def get_price_by_drug(drug_name, file_path='public/data/drug_prices.csv'):
"""回傳特定藥品在各國的價格"""
df = load_drug_prices(file_path)
if drug_name not in df.columns:
raise ValueError(f"{drug_name} not found in drug price data.")
return df[drug_name].to_dict()

