import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# =========================
# PAGE TITLE
# =========================

st.title("🔮 Forecasting & Future Predictions")

st.info("""
This page performs revenue forecasting using the Prophet model
and provides future revenue estimates with confidence intervals.
""")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("amazon_dashboard_data.csv")

df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# =========================
# PREPARE FORECAST DATA
# =========================

forecast_df = (
    df.groupby('purchase_date')['final_price']
    .sum()
    .reset_index()
)

forecast_df.columns = ['ds', 'y']

# =========================
# KPI SECTION
# =========================

latest_revenue = forecast_df['y'].iloc[-1]

avg_revenue = forecast_df['y'].mean()

forecast_days = 90

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Forecast Horizon",
        f"{forecast_days} Days"
    )

with col2:
    st.metric(
        "Average Daily Revenue",
        f"{avg_revenue:,.0f}"
    )

with col3:
    st.metric(
        "Latest Daily Revenue",
        f"{latest_revenue:,.0f}"
    )

# =========================
# MODEL TRAINING
# =========================

st.markdown("---")

with st.spinner("Training Prophet Forecast Model..."):

    model = Prophet()

    model.fit(forecast_df)

    future = model.make_future_dataframe(
        periods=90
    )

    forecast = model.predict(future)

# =========================
# FORECAST CHART
# =========================

st.markdown("---")

st.subheader("📈 Revenue Forecast")

fig1 = model.plot(forecast)

st.pyplot(fig1)

# =========================
# FORECAST TABLE
# =========================

st.markdown("---")

st.subheader("📋 Future Revenue Predictions")

future_predictions = forecast[
    ['ds', 'yhat', 'yhat_lower', 'yhat_upper']
].tail(20)

st.dataframe(future_predictions)

# =========================
# FORECAST COMPONENTS
# =========================

st.markdown("---")

st.subheader("📊 Forecast Components")

fig2 = model.plot_components(forecast)

st.pyplot(fig2)

# =========================
# BUSINESS INTERPRETATION
# =========================

st.markdown("---")

st.subheader("📌 Forecast Insights")

future_avg = forecast['yhat'].tail(90).mean()

st.success(f"""
The forecast model predicts future revenue patterns
for the next 90 days.

The estimated average forecasted daily revenue is
approximately {future_avg:,.0f}.

The confidence interval provides uncertainty bounds,
helping decision-makers understand possible revenue variations.

This forecasting analysis supports future planning,
inventory management, and business strategy decisions.
""")
