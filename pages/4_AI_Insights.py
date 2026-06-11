import streamlit as st
import pandas as pd

# =========================
# PAGE TITLE
# =========================

st.title("🤖 AI Insights Dashboard")

st.info("""
This page automatically discovers business insights
from Amazon E-Commerce data using descriptive analytics.
""")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("amazon_dashboard_data.csv")

df["revenue"] = df["final_price"]

# =========================
# AI INSIGHTS
# =========================

top_category = (
    df.groupby("category")["revenue"]
    .sum()
    .idxmax()
)

top_category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .max()
)

best_brand = (
    df.groupby("brand")["rating"]
    .mean()
    .idxmax()
)

best_brand_rating = (
    df.groupby("brand")["rating"]
    .mean()
    .max()
)

top_payment = (
    df["payment_method"]
    .value_counts()
    .idxmax()
)

highest_return = (
    df.groupby("category")["is_returned"]
    .mean()
    .idxmax()
)

highest_return_value = (
    df.groupby("category")["is_returned"]
    .mean()
    .max() * 100
)

# =========================
# KPI SECTION
# =========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Top Revenue Category",
        top_category
    )

with col2:
    st.metric(
        "Best Rated Brand",
        best_brand
    )

with col3:
    st.metric(
        "Top Payment Method",
        top_payment
    )

with col4:
    st.metric(
        "Highest Return Category",
        highest_return
    )

# =========================
# BUSINESS INSIGHTS
# =========================

st.markdown("---")

st.subheader("📌 Automated Business Insights")

st.success(
    f"🏆 Top Revenue Category: {top_category} "
    f"(Revenue: {top_category_revenue:,.0f})"
)

st.success(
    f"⭐ Highest Rated Brand: {best_brand} "
    f"(Average Rating: {best_brand_rating:.2f})"
)

st.success(
    f"💳 Most Used Payment Method: {top_payment}"
)

st.success(
    f"📦 Highest Return Category: {highest_return} "
    f"({highest_return_value:.2f}% Returns)"
)

# =========================
# ADDITIONAL METRICS
# =========================

st.markdown("---")

st.subheader("📊 Overall Performance Metrics")

col5, col6 = st.columns(2)

with col5:
    st.metric(
        "Average Product Rating",
        f"{df['rating'].mean():.2f}"
    )

with col6:
    st.metric(
        "Average Seller Rating",
        f"{df['seller_rating'].mean():.2f}"
    )

# =========================
# EXECUTIVE SUMMARY
# =========================

st.markdown("---")

st.subheader("📝 Executive Summary")

st.info(f"""
The analysis indicates that **{top_category}** generates the
highest revenue among all product categories.

Customer satisfaction is strongest for products from
**{best_brand}**, which achieved the highest average rating.

The most preferred payment method is **{top_payment}**,
highlighting customer payment behavior.

The category with the highest return activity is
**{highest_return}**, suggesting an area for further
quality and customer experience investigation.
""")