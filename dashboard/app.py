import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Solar Challenge Week 1 Dashboard")
st.write("Interactive dashboard for solar data insights (placeholder data).")

# --- Sidebar for country selection ---
country = st.sidebar.selectbox("Select a Country", ["Benin", "Sierra Leone", "Togo"])

st.write(f"Showing data for: {country}")

# --- Generate example data ---
dates = pd.date_range(start="2025-01-01", periods=30)
ghi = np.random.uniform(100, 800, size=len(dates))
dni = np.random.uniform(50, 700, size=len(dates))
dhi = np.random.uniform(20, 400, size=len(dates))

df = pd.DataFrame({
    "Date": dates,
    "GHI": ghi,
    "DNI": dni,
    "DHI": dhi
})

# --- Show dataframe ---
st.dataframe(df.head())

# --- Time series plot ---
st.subheader("Time Series of Solar Features")
fig, ax = plt.subplots(figsize=(10,4))
ax.plot(df["Date"], df["GHI"], label="GHI")
ax.plot(df["Date"], df["DNI"], label="DNI")
ax.plot(df["Date"], df["DHI"], label="DHI")
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.legend()
st.pyplot(fig)

# --- Histogram ---
st.subheader("Distribution of Solar Features")
fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.hist(df["GHI"], bins=10, alpha=0.5, label="GHI")
ax2.hist(df["DNI"], bins=10, alpha=0.5, label="DNI")
ax2.hist(df["DHI"], bins=10, alpha=0.5, label="DHI")
ax2.set_xlabel("Value")
ax2.set_ylabel("Frequency")
ax2.legend()
st.pyplot(fig2)
