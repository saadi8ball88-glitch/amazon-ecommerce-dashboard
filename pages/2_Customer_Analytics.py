import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# PAGE TITLE
# =========================

st.title("👥 Customer Analytics")

st.info("""
This page analyzes customer behavior, ratings,
payment preferences, and product return patterns.
""")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("amazon_dashboard_data.csv")

# =========================
# CUSTOMER KPIs
# =========================

avg_rating = df['rating'].mean()

most_used_payment = (
    df['payment_method']
    .value_counts()
    .idxmax()
)

return_rate = (
    df['is_returned']
    .mean() * 100
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Rating",
        f"{avg_rating:.2f}"
    )

with col2:
    st.metric(
        "Most Used Payment",
        most_used_payment
    )

with col3:
    st.metric(
        "Return Rate",
        f"{return_rate:.2f}%"
    )

# =========================
# RATING DISTRIBUTION
# =========================

st.markdown("---")

st.subheader("⭐ Rating Distribution")

fig1, ax1 = plt.subplots(figsize=(7,4))

df['rating'].hist(
    bins=10,
    ax=ax1
)

ax1.set_title("Customer Rating Distribution")
ax1.set_xlabel("Rating")
ax1.set_ylabel("Frequency")

st.pyplot(fig1)

# =========================
# PAYMENT METHODS
# =========================

st.markdown("---")

st.subheader("💳 Payment Method Usage")

payment_counts = df['payment_method'].value_counts()

fig2, ax2 = plt.subplots(figsize=(7,4))

payment_counts.plot(
    kind='bar',
    ax=ax2
)

ax2.set_title("Most Preferred Payment Methods")
ax2.set_xlabel("Payment Method")
ax2.set_ylabel("Number of Transactions")

st.pyplot(fig2)

# =========================
# RETURN ANALYSIS
# =========================

st.markdown("---")

st.subheader("📦 Return Analysis")

category_returns = (
    df.groupby('category')['is_returned']
    .mean() * 100
)

fig3, ax3 = plt.subplots(figsize=(7,4))

category_returns.plot(
    kind='bar',
    ax=ax3
)

ax3.set_title("Return Rate by Category")
ax3.set_xlabel("Category")
ax3.set_ylabel("Return Percentage")

st.pyplot(fig3)

# =========================
# CUSTOMER INSIGHTS
# =========================

st.markdown("---")

highest_return_category = category_returns.idxmax()

highest_return_value = category_returns.max()

st.success(
    f"📌 Category with Highest Return Rate: "
    f"{highest_return_category} "
    f"({highest_return_value:.2f}%)"
)