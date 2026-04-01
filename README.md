# 🦠 COVID-19 Data Analytics Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![SQL](https://img.shields.io/badge/SQL-Queries-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

---

## 📌 Overview
This project analyzes global COVID-19 data using Python (pandas), SQL, and visualization tools.  
It helps understand trends, country-wise statistics, and pandemic impact.

---

## 🎯 Objectives
- Data cleaning and preprocessing  
- Data analysis using pandas  
- SQL-based insights  
- Interactive dashboard creation  

---

## 🛠️ Tech Stack
- Python (pandas, matplotlib)  
- SQL  
- Streamlit  
- Power BI / Tableau  

---

## 📂 Project Structure
covid-analytics/
│
├── data/
│   └── covid_data.csv
├── notebooks/
│   ├── day1_loading.ipynb
│   ├── day2_analysis.ipynb
│   ├── day3_cleaning.ipynb
├── sql/
│   └── queries.sql
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 📊 Features
- Data Loading & Exploration  
- Data Cleaning & Preprocessing  
- Country-wise Analysis  
- Trend Analysis  
- SQL Queries  
- Interactive Dashboard  

---

## 📅 Workflow
Day 1: Data Loading & Exploration  
Day 2: Data Analysis  
Day 3: Data Cleaning  
Day 4: Insights  
Day 5: Dashboard  

---

## 🚀 How to Run

1. Clone repository:
git clone https://github.com/bobby2805/covid-analytics.git  
cd covid-analytics  

2. Install dependencies:
pip install -r requirements.txt  

3. Run app:
streamlit run app.py  

---

## 📌 Sample SQL Queries
SELECT location, MAX(total_cases) AS total_cases
FROM covid_data
GROUP BY location
ORDER BY total_cases DESC;

SELECT location, MAX(new_cases) AS max_new_cases
FROM covid_data
GROUP BY location
ORDER BY max_new_cases DESC;

---

## 📊 Sample Python Code
import pandas as pd

df = pd.read_csv("data/covid_data.csv")
top = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)
print(top)

---

## 📷 Dashboard Preview
- Top countries with highest COVID cases
- Daily trends of new cases and deaths
- Country-wise comparison of pandemic impact
- Data-driven insights using SQL and Python

---

## 🌐 Live Demo
https://covid-analytics-mb2mrtksv5xvckrfmqpsbv.streamlit.app

---

## 📧 Contact
Name: Pannuru Kartik Reddy  
Email: kartikreddypannuru200@gmail.com  
GitHub: https://github.com/bobby2805 

---

## ⭐ Acknowledgements
- Our World in Data  
- Kaggle  

---

## 🚀 Future Improvements
- Vaccination analysis  
- Better dashboard UI  
- Real-time data integration  
