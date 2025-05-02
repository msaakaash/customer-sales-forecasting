import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
rfm = pd.read_csv('../data/processed/rfm_table.csv')

st.set_page_config(page_title="Customer Analytics Dashboard", layout="wide")
st.title("📊 Customer Segmentation & Churn Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Customers")
segment_filter = st.sidebar.multiselect("Select Segments", options=rfm['Segment'].unique(), default=rfm['Segment'].unique())
churn_filter = st.sidebar.selectbox("Select Churn Status", options=["All", "Churned", "Active"])

filtered_data = rfm.copy()
if segment_filter:
    filtered_data = filtered_data[filtered_data['Segment'].isin(segment_filter)]
if churn_filter == "Churned":
    filtered_data = filtered_data[filtered_data['Churn'] == 1]
elif churn_filter == "Active":
    filtered_data = filtered_data[filtered_data['Churn'] == 0]

st.markdown(f"### Showing {len(filtered_data)} Customers")

# Metric Cards
col1, col2, col3 = st.columns(3)
col1.metric("Avg Recency", round(filtered_data['Recency'].mean(), 2))
col2.metric("Avg Frequency", round(filtered_data['Frequency'].mean(), 2))
col3.metric("Avg Monetary Value", f"${round(filtered_data['Monetary'].mean(), 2)}")

# Revenue by Segment
st.markdown("#### 💸 Revenue by Segment")
rev_plot = filtered_data.groupby("Segment")["Monetary"].sum().sort_values()
fig1, ax1 = plt.subplots()
rev_plot.plot(kind='barh', ax=ax1, color='skyblue')
st.pyplot(fig1)

# Churn by Segment
st.markdown("#### Churn Rate by Segment")
churn_rate = rfm.groupby('Segment')['Churn'].mean().sort_values()
fig2, ax2 = plt.subplots()
churn_rate.plot(kind='bar', ax=ax2, color='salmon')
st.pyplot(fig2)

# Download Data
st.markdown("#### 📥 Download Filtered Data")
st.download_button("Download CSV", data=filtered_data.to_csv(index=False), file_name="filtered_customers.csv")

# Footer
st.markdown("---")
st.markdown("Say My Name.")

