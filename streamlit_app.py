# 📢 This app uses fake/mock data. Do not use for real medical decisions or price comparisons.

import streamlit as st
import pandas as pd
from src.models.drug_price_tracker import get_price_by_drug, get_goodrx_price
from src.models.plot_price_comparison import plot_price_comparison

st.title("💊 MedJustice: Drug Cost & Social Impact Demo")
st.markdown("**🛑 Disclaimer: This app uses mock data for demo purposes only.**")

# --- Drug Price Comparison ---
st.header("📉 Global Drug Price Comparison")

drug_name = st.selectbox("Choose a drug", ["Insulin", "Contraceptive", "Metformin"])
csv_path = "public/data/drug_prices.csv"
prices = get_price_by_drug(drug_name, csv_path)
st.write("Estimated monthly price (demo data):", prices)

st.pyplot(plot_price_comparison(drug_name, csv_path))

# --- Simulated GoodRx Prices ---
st.header("💵 U.S. Retail Prices (Simulated GoodRx)")

zip_code = st.text_input("ZIP Code", "10001")
mock_prices = get_goodrx_price(drug_name.lower(), zip_code)
st.dataframe(mock_prices)

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ for social impact. | 🚫 Demo data only – Not for real medical decisions.")

