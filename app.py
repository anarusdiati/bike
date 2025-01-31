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
st.write("Dataset source: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/data?select=day.csv")
st.write("Streamlit app: https://bikeeeee.streamlit.app/")

# Title
st.title("Bike Sharing Analysis")
st.markdown("Data Analysis to understand bike lending trends based on dataset.")

# Load dataset
url = "https://raw.githubusercontent.com/lakshmi25npathi/Bike-Sharing-Dataset/master/day.csv"
data = pd.read_csv(url)

# Convert 'dteday' column to datetime format
df['dteday'] = pd.to_datetime(df['dteday'])

# Menu options
menu = st.sidebar.radio("Analysis:", ["EDA Univariate", "EDA Bivariate", "EDA Multivariate", "Data Visualization"])

# EDA Univariate
if menu == "EDA Univariate":
    st.subheader("Univariate Analysis")
    st.write("Displays the distribution of numeric variables in a dataset.")

    numerical_features = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
    
    for col in numerical_features:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(data[col], kde=True, bins=30, color="blue", ax=ax)
        ax.set_title(f"Distribusi {col}")
        st.pyplot(fig)

# EDA Bivariate
elif menu == "EDA Bivariate":
    st.subheader("Bivariate Analysis")
    st.write("Viewing the relationship between two variables in a dataset.")

    # Scatter Plot
    st.write("**Scatter Plot between Temperature and Number of Bike Borrowings**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x=data["temp"], y=data["cnt"], ax=ax)
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Bike Rentals")
    st.pyplot(fig)

    # Boxplot
    st.write("**Boxplot between Season and Number of Bike Borrowings**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=data["season"], y=data["count"], ax=ax)
    ax.set_xlabel("Season")
    ax.set_ylabel("Bike Rentals")
    st.pyplot(fig)

# EDA Multivariate
elif menu == "EDA Multivariate":
    st.subheader("Multivariate Analysis")
    st.write("Shows the relationship between multiple variables at once.")

    # Heatmap Correlation
    df_corr = data.drop(columns=['dteday'])
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data_corr.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

# Data Visualization
elif menu == "Data Visualization":
    st.subheader("Data Visualization")

    # Visualization 1: Boxplot of bike lending by day of the week
    st.write("**What are the bike lending trends based on day of the week?**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(x=df["weekday"], y=df["count"], ax=ax)
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Bike Rentals")
    st.pyplot(fig)
    st.markdown("**Insight:**Bicycle rentals are higher on weekends than on weekdays, indicating that bicycles are used more often for recreational activities..")
  
    # Visualization 2: Scatter plot of temperature vs number of bikes borrowed
    st.write("**Does temperature affect the number of bikes borrowed??**")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x=data["temp"], y=data["count"], ax=ax)
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Bike Rentals")
    st.pyplot(fig)
    st.markdown("**Insight:**Bike rentals increase with increasing temperature, but after a certain temperature, the number tends to stabilize.")

    
