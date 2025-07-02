
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.models.drug_price_tracker import get_price_by_drug
from src.models.plot_price_comparison import plot_price_comparison

st.title("💊 MedJustice: Drug Price & ER Cost Prediction Demo")

# 藥物價格比較
st.header("1. Drug Price Tracker")
drug_name = st.selectbox("Select a drug", ["Insulin", "Birth Control", "Generic Antibiotics"])
drug_prices = get_price_by_drug(drug_name, "public/data/drug_prices.csv")
st.write(f"Prices for {drug_name}:")
st.dataframe(drug_prices)

# 顯示價格比較圖
st.pyplot(plot_price_comparison(drug_name, "public/data/drug_prices.csv"))

# ER成本預測
st.header("2. Emergency Cost Prediction (Hispanic Group)")

# 載入資料並建模
data = pd.read_csv("public/data/sample_input.csv")
subset = data[(data['ethnicity'] == 'Hispanic') & (data['category'] == 'Emergency')]
X = subset[['income', 'population', 'medicaid_access', 'undocumented_status', 'fertility_rate']]
y = subset['social_costs']

from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(X, y)
pred = model.predict(X)

# 顯示圖表
fig, ax = plt.subplots()
ax.plot(pred)
ax.set_title("ER Cost Prediction (Hispanic)")
ax.set_ylabel("Cost (USD)")
st.pyplot(fig)
