import streamlit as st
import pandas as pd

st.markdown("# Exploration ❄️")
st.sidebar.markdown("# Exploration ❄️")

st.markdown("##### The Dataset")

st.write("The data was sourced from Kaggle. ")

# Read the dataset
df = pd.read_csv('telco_clean.csv', index_col=0)

# Display the data
st.dataframe(df.head())

# Shape
st.markdown("##### Shape")
st.write(f"There were {df.shape[0]} records and  {df.shape[1]} rows in the original dataset")

# Description
st.markdown("##### Statistical Analysis of Numerical Values")
st.write(df.describe())

# Null Values
st.markdown("##### Null Values and Duplicated Values")
st.write(f"There were {df.isna().sum().sum()} records with null values and  {df.duplicated().sum()} rows with duplicates!")

# Unique Values
st.markdown("##### Unique Values")
st.write("The number of unique values per column")
unique_cols = df.nunique().sort_values()
unique_cols = pd.DataFrame({'column': unique_cols.index, 'val': unique_cols.values})
left_col, mid_col, right_col = st.columns(3)
with left_col:
    st.write(unique_cols[:7])
with mid_col:
    st.write(unique_cols[7:15])
with right_col:
    st.write(unique_cols[15:])

# Data Distribution
st.markdown("##### Target Distribution")
st.write("The target variable is `Churn` which had the following distribution")
st.write(df['Churn'].value_counts(normalize=True))

# Data Type Distribution
st.markdown("##### Column Types")
st.write(df.dtypes.value_counts())
