import pandas as pd
import matplotlib.pyplot as plt

def plot_price_comparison(drug_name, file_path='public/data/drug_prices.csv'):

df = pd.read_csv(file_path)
if drug_name not in df.columns:
raise ValueError(f"{drug_name} not found in file.")

df = df.set_index('country')
prices = df[drug_name]

prices.plot(kind='bar', title=f'{drug_name} Price Comparison (USD/month)', ylabel='Price ($)')
plt.tight_layout()
plt.show()


