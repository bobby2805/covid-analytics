from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_covid_data.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Title
st.title("🤖 AI-Powered COVID-19 Analytics Dashboard")

# Sidebar
st.sidebar.header("Filters")

# 📅 Date Filter
start_date = st.sidebar.date_input("Start Date", df['date'].min())
end_date = st.sidebar.date_input("End Date", df['date'].max())

# Country Filter
countries = df['location'].unique()
selected_country = st.sidebar.selectbox("Select Country", countries)

# ✅ FILTER DATA (FIRST)
country_data = df[
    (df['location'] == selected_country) &
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
]

# Sort data
country_data = country_data.sort_values('date')

# 📊 Moving Average
country_data['7_day_avg'] = country_data['new_cases'].rolling(7, min_periods=1).mean()

# ✅ KPI METRICS (TOP)
if not country_data.empty:
    latest = country_data.iloc[-1]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Cases", int(latest['total_cases']))
    col2.metric("New Cases", int(latest['new_cases']))
    col3.metric("Total Deaths", int(latest['total_deaths']))

# Show latest data
st.subheader(f"Latest Data - {selected_country}")
st.write(country_data.tail())

# 📈 Total Cases
st.subheader("📈 Total Cases Over Time")
plt.figure(figsize=(10,5))
plt.plot(country_data['date'], country_data['total_cases'])
plt.title("Total Cases Trend")
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 📉 Total Deaths
st.subheader("📉 Total Deaths Over Time")
plt.figure(figsize=(10,5))
plt.plot(country_data['date'], country_data['total_deaths'])
plt.title("Total Deaths Trend")
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 📊 Daily New Cases
st.subheader("📊 Daily New Cases")
plt.figure(figsize=(10,5))
plt.plot(country_data['date'], country_data['new_cases'])
plt.title("Daily New Cases")
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 📊 Moving Average Graph
st.subheader("📊 7-Day Moving Average (New Cases)")
plt.figure(figsize=(10,5))
plt.plot(country_data['date'], country_data['7_day_avg'])
plt.title("7-Day Average of New Cases")
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

# 🌍 Top Countries Comparison
st.subheader("🌍 Top Countries by Total Cases")
latest_data = df.sort_values('date').groupby('location').last()
top_countries = latest_data.sort_values(by='total_cases', ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(top_countries.index, top_countries['total_cases'])
plt.xticks(rotation=45)
plt.title("Top Countries by Total Cases")
plt.tight_layout()
st.pyplot(plt)

# 🤖 AI Prediction
st.subheader("🤖 Future Cases Prediction")

country_data_ml = country_data.dropna(subset=['total_cases']).copy()

if not country_data_ml.empty:
    country_data_ml['days'] = (country_data_ml['date'] - country_data_ml['date'].min()).dt.days

    X = country_data_ml[['days']]
    y = country_data_ml['total_cases']

    model = LinearRegression()
    model.fit(X, y)

    future_days = np.arange(X['days'].max(), X['days'].max() + 30).reshape(-1, 1)
    future_df = pd.DataFrame(future_days, columns=['days'])

    predictions = model.predict(future_df)

    plt.figure(figsize=(10,5))
    plt.plot(country_data_ml['date'], y, label="Actual")

    future_dates = pd.date_range(start=country_data_ml['date'].max(), periods=30)
    plt.plot(future_dates, predictions, linestyle='dashed', label="Predicted")

    plt.legend()
    plt.xticks(rotation=45)
    plt.title("Future Prediction (Next 30 Days)")
    plt.tight_layout()

    st.pyplot(plt)

# 📥 Download Button
csv = country_data.to_csv(index=False)
st.download_button(
    label="📥 Download Data",
    data=csv,
    file_name='covid_data.csv',
    mime='text/csv'
)

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit | AI Project")