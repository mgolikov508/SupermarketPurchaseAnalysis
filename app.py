import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import os
import subprocess

st.set_page_config(
    page_title="Supermarket Analysis",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Supermarket Purchase Analysis Dashboard")
st.markdown("Interactive analysis of supermarket sales and customer behavior")

# Load data
@st.cache_data
def load_data():
    data_file = Path("supermarket_data.xlsx")
    if not data_file.exists():
        # Auto-generate data if not exists (for Streamlit Cloud)
        subprocess.run(["python", "generate_data.py"])
    df = pd.read_excel(data_file)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

categories = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

payment_methods = st.sidebar.multiselect(
    "Payment Method",
    options=df["Payment Method"].unique(),
    default=df["Payment Method"].unique()
)

customer_types = st.sidebar.multiselect(
    "Customer Type",
    options=df["Customer Type"].unique(),
    default=df["Customer Type"].unique()
)

date_range = st.sidebar.date_input(
    "Date Range",
    value=(df["Date"].min(), df["Date"].max()),
    min_value=df["Date"].min(),
    max_value=df["Date"].max()
)

# Filter data
filtered_df = df[
    (df["Category"].isin(categories)) &
    (df["Payment Method"].isin(payment_methods)) &
    (df["Customer Type"].isin(customer_types)) &
    (df["Date"] >= pd.to_datetime(date_range[0])) &
    (df["Date"] <= pd.to_datetime(date_range[1]))
]

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Purchases", len(filtered_df))
with col2:
    st.metric("Total Revenue", f"${filtered_df['Total'].sum():,.2f}")
with col3:
    st.metric("Avg Purchase", f"${filtered_df['Total'].mean():.2f}")
with col4:
    st.metric("Products Sold", filtered_df['Quantity'].sum())

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sales by Category")
    category_sales = filtered_df.groupby("Category")["Total"].sum().sort_values(ascending=False)
    fig1 = px.bar(
        x=category_sales.values,
        y=category_sales.index,
        orientation='h',
        labels={'x': 'Revenue ($)', 'y': 'Category'},
        color=category_sales.values,
        color_continuous_scale='Blues'
    )
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("💳 Payment Method Distribution")
    payment_counts = filtered_df["Payment Method"].value_counts()
    fig2 = px.pie(
        values=payment_counts.values,
        names=payment_counts.index,
        hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

# Time series
st.subheader("📈 Daily Sales Trend")
daily_sales = filtered_df.groupby("Date")["Total"].sum().reset_index()
fig3 = px.line(
    daily_sales,
    x="Date",
    y="Total",
    labels={'Total': 'Revenue ($)', 'Date': 'Date'}
)
fig3.update_traces(line_color='#636EFA')
st.plotly_chart(fig3, use_container_width=True)

# Customer analysis
col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Customer Type Analysis")
    customer_revenue = filtered_df.groupby("Customer Type")["Total"].sum()
    fig4 = px.pie(
        values=customer_revenue.values,
        names=customer_revenue.index,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig4, use_container_width=True)

with col2:
    st.subheader("🏆 Top 10 Products")
    top_products = filtered_df.groupby("Product")["Total"].sum().sort_values(ascending=False).head(10)
    fig5 = px.bar(
        x=top_products.values,
        y=top_products.index,
        orientation='h',
        labels={'x': 'Revenue ($)', 'y': 'Product'}
    )
    st.plotly_chart(fig5, use_container_width=True)

# Data table
st.subheader("📋 Purchase Details")
st.dataframe(
    filtered_df.sort_values("Date", ascending=False),
    use_container_width=True,
    hide_index=True
)

# Download button
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name="filtered_supermarket_data.csv",
    mime="text/csv"
)
