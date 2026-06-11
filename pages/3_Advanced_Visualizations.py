import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PAGE TITLE
# =========================

st.title("📊 Advanced Visualizations")

st.info("""
This page presents advanced visualization techniques
including ECDF, Violin Plot, and Correlation Heatmap
for deeper analytical insights.
""")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("amazon_dashboard_data.csv")

# Sample for faster rendering
viz_df = df.sample(2000, random_state=42)

# =========================
# VISUALIZATION KPIs
# =========================

avg_price = viz_df['final_price'].mean()

max_price = viz_df['final_price'].max()

avg_rating = viz_df['rating'].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Price",
        f"{avg_price:,.0f}"
    )

with col2:
    st.metric(
        "Maximum Price",
        f"{max_price:,.0f}"
    )

with col3:
    st.metric(
        "Average Rating",
        f"{avg_rating:.2f}"
    )

# =========================
# ECDF PLOT
# =========================

st.markdown("---")

st.subheader("📈 ECDF of Product Prices")

sorted_prices = viz_df['final_price'].sort_values()

y = [i / len(sorted_prices) for i in range(1, len(sorted_prices) + 1)]

fig1, ax1 = plt.subplots(figsize=(7,4))

ax1.plot(sorted_prices, y)

ax1.set_title("Empirical Cumulative Distribution Function")
ax1.set_xlabel("Final Price")
ax1.set_ylabel("Cumulative Probability")

st.pyplot(fig1)

# =========================
# VIOLIN PLOT
# =========================

st.markdown("---")

st.subheader("🎻 Rating Distribution by Category")

fig2, ax2 = plt.subplots(figsize=(8,4))

sns.violinplot(
    data=viz_df,
    x='category',
    y='rating',
    ax=ax2
)

ax2.set_title("Customer Rating Distribution Across Categories")

st.pyplot(fig2)

# =========================
# CORRELATION HEATMAP
# =========================

st.markdown("---")

st.subheader("🔥 Correlation Heatmap")

numeric_cols = [
    'price',
    'discount',
    'final_price',
    'rating',
    'review_count',
    'stock',
    'seller_rating',
    'shipping_time_days'
]

fig3, ax3 = plt.subplots(figsize=(8,5))

sns.heatmap(
    viz_df[numeric_cols].corr(),
    cmap='coolwarm',
    annot=True,
    ax=ax3
)

ax3.set_title("Correlation Matrix of Numerical Features")

st.pyplot(fig3)

# =========================
# INSIGHTS SECTION
# =========================

st.markdown("---")

st.subheader("📌 Visualization Insights")

st.success("""
• ECDF shows cumulative distribution of product prices.

• Violin Plot reveals rating spread across categories.

• Heatmap highlights relationships among numerical variables.

• Advanced visualizations support perception-aware analytics
and data-driven decision making.
""")