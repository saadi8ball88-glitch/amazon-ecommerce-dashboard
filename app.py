import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Amazon E-Commerce Dashboard")

st.write("Select a page from the sidebar.")
# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Amazon E-Commerce Analytics Dashboard",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.kpi-card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.3);
}

.kpi-title {
    font-size: 18px;
    color: #CBD5E1;
}

.kpi-value {
    font-size: 30px;
    font-weight: bold;
    color: #38BDF8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.title("🛒 Amazon E-Commerce Analytics Dashboard")

st.info("""
AI-Augmented Perception-Aware Visualization Dashboard
for Amazon E-Commerce Analytics.
""")

# =========================
# LOAD DATA
# =========================

@st.cache_data
def load_data():
    return pd.read_csv("amazon_dashboard_data.csv")

df = load_data()

# =========================
# KPI VALUES
# =========================

total_revenue = df['final_price'].sum()
total_orders = len(df)
avg_rating = df['rating'].mean()
return_rate = df['is_returned'].mean() * 100

# =========================
# KPI SECTION
# =========================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Orders</div>
        <div class="kpi-value">{total_orders:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Revenue</div>
        <div class="kpi-value">{total_revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Average Rating</div>
        <div class="kpi-value">{avg_rating:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Return Rate</div>
        <div class="kpi-value">{return_rate:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# DATASET INFO
# =========================

st.markdown("---")

st.subheader("📂 Dataset Information")

st.write("Dataset Shape:", df.shape)

# =========================
# REVENUE BY CATEGORY
# =========================

st.markdown("---")

st.subheader("📊 Revenue by Category")

category_sales = (
    df.groupby('category')['final_price']
    .sum()
    .sort_values(ascending=False)
)

fig1, ax1 = plt.subplots(figsize=(6,4))

category_sales.plot(
    kind='bar',
    ax=ax1
)

ax1.set_title("Revenue by Category")
ax1.set_xlabel("Category")
ax1.set_ylabel("Revenue")

st.pyplot(fig1)

# =========================
# MONTHLY REVENUE TREND
# =========================

df['purchase_date'] = pd.to_datetime(df['purchase_date'])

st.markdown("---")

st.subheader("📈 Monthly Revenue Trend")

monthly_revenue = (
    df.groupby(
        df['purchase_date'].dt.to_period('M')
    )['final_price']
    .sum()
)

monthly_revenue.index = monthly_revenue.index.astype(str)

fig2, ax2 = plt.subplots(figsize=(6,4))

monthly_revenue.plot(
    marker='o',
    ax=ax2
)

ax2.set_title("Monthly Revenue Trend")
ax2.set_xlabel("Month")
ax2.set_ylabel("Revenue")

plt.xticks(rotation=45)

st.pyplot(fig2)

# =========================
# CATEGORY DISTRIBUTION
# =========================

st.markdown("---")

st.subheader("📊 Category Distribution")

category_count = df['category'].value_counts()

fig3, ax3 = plt.subplots(figsize=(6,4))

category_count.plot(
    kind='bar',
    ax=ax3
)

ax3.set_title("Category Distribution")
ax3.set_xlabel("Category")
ax3.set_ylabel("Orders")

st.pyplot(fig3)

# =========================
# DATA PREVIEW
# =========================

st.markdown("---")

with st.expander("🔍 View Dataset Sample"):
    st.dataframe(df.head())