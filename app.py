import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("day.csv")

st.write("Nama: Rokhana Diyah Rusdiati")
st.write("Email: anausername@gmail.com")
st.write("ID Dicoding: anarusdiati")

# Title
st.title("Bike Sharing Analysis")

# Business questions
st.write("## Conclusions")
st.write("- Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?")
st.write("- Bagaimana tren penyewaan sepeda dari waktu ke waktu?")

# Display first few rows
st.write("### Data Overview", df.head())

# Data Wrangling
# Checking for missing values
st.write("### Missing Values", df.isnull().sum())

# Converting categorical numerical columns to more readable format
df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Cloudy', 3: 'Light Rain', 4: 'Heavy Rain'})

# Exploratory Data Analysis
st.write("### Distribution of Total Bike Rentals")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df['cnt'], bins=30, kde=True, ax=ax)
ax.set_xlabel('Total Rentals')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Seasonal Analysis
st.write("### Bike Rentals by Season")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x='season', y='cnt', data=df, ax=ax)
st.pyplot(fig)

# Trend Analysis
st.write("### Bike Rental Trends Over Time")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df['dteday'], df['cnt'], marker='o', linestyle='-', alpha=0.6)
ax.set_xlabel('Date')
ax.set_ylabel('Total Rentals')
plt.xticks(rotation=45)
st.pyplot(fig)

# Additional Insights
st.write("### Correlation Matrix of Bike Rentals and Weather Conditions")
correlation_matrix = df[['cnt', 'temp', 'hum', 'windspeed']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Conclusions
st.write("## Conclusions")
st.write("- Musim berpengaruh terhadap jumlah penyewaan sepeda. Berdasarkan analisis yang telah dilakukan, diketahui bahwa musim Fall memiliki jumlah penyewaan sepeda tertinggi daripada musim lainnya.")
st.write("- Tren jumlah penyewaan sepeda semakin meningkat dari waktu ke waktu, hal ini terlihat dari jumlah sewa harian yang semakin naik setiap harinya.")
