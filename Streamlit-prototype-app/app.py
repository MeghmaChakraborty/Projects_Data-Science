import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide", page_title="Prototype Dashboard")

@st.cache_data
def load_data(path="data.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df

df = load_data("data.csv")

# Sidebar filters
st.sidebar.header("Filters")
min_date = df['date'].min()
max_date = df['date'].max()
start_date, end_date = st.sidebar.date_input("Date range", [min_date, max_date])
regions = st.sidebar.multiselect("Region", options=df['region'].unique(), default=list(df['region'].unique()))
products = st.sidebar.multiselect("Product", options=df['product'].unique(), default=list(df['product'].unique()))

# Filter data
mask = (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))
mask &= df['region'].isin(regions)
mask &= df['product'].isin(products)
df_f = df.loc[mask].copy()

# KPI metrics
total_revenue = df_f['revenue'].sum()
total_orders = df_f['orders'].sum()
total_users = df_f['users'].sum()
avg_order_value = total_revenue / total_orders if total_orders>0 else 0

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Revenue", f"${total_revenue:,.0f}")
kpi2.metric("Total Orders", f"{total_orders:,}")
kpi3.metric("Active Users", f"{total_users:,}")
kpi4.metric("Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")
# Trend chart: Revenue over time
rev_ts = df_f.groupby('date').agg(revenue=('revenue','sum')).reset_index()
rev_ts['date'] = pd.to_datetime(rev_ts['date'])
fig_rev = px.line(rev_ts, x='date', y='revenue', title="Revenue Over Time", markers=True)
st.plotly_chart(fig_rev, use_container_width=True)

# Revenue by region
col1, col2 = st.columns([2,1])
with col1:
    fig_reg = px.bar(df_f.groupby('region').agg(revenue=('revenue','sum')).reset_index(), x='region', y='revenue', title="Revenue by Region", text_auto=True)
    st.plotly_chart(fig_reg, use_container_width=True)
with col2:
    fig_prod = px.pie(df_f.groupby('product').agg(revenue=('revenue','sum')).reset_index(), names='product', values='revenue', title="Revenue by Product")
    st.plotly_chart(fig_prod, use_container_width=True)

st.markdown("---")
# Top customers table
top_customers = df_f.groupby('customer').agg(revenue=('revenue','sum'), orders=('orders','sum')).reset_index().nlargest(10, 'revenue')
st.subheader("Top 10 Customers by Revenue")
st.table(top_customers.style.format({"revenue":"${:,.2f}"}))

st.markdown("---")
# Data download
st.markdown("### Download Filtered Data")
st.download_button("Download CSV", df_f.to_csv(index=False).encode('utf-8'), file_name="filtered_data.csv", mime="text/csv")
