import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page and Side Bar title
st.markdown("# Analysis ❄️")
st.sidebar.markdown("# Visualisations ❄️")

# Read the dataset
df = pd.read_csv('telco_clean.csv', index_col=0)

# Style
sns.set_theme(style='whitegrid')

# The Filters
tenure_list = list(sorted(df['tenure_group'].unique()))
tenure_list.append('All')
tenure_group = st.sidebar.selectbox('Tenure Group Filter:', tenure_list, index=4)

# Filtered Data
if tenure_group == 'All':
    filtered_df = df
else:
    filtered_df = df[df['tenure_group'] == tenure_group]
    st.write(f'Tenure group focus: `{tenure_group}` months')

# KPI cards

st.write("***Key Performance Indicators***")
kpi_cols1, kpi_cols2, kpi_cols3  = st.columns(3)
with kpi_cols1:
    st.metric('Churn Rate', f" {filtered_df['Churn'].mean():.2%} ")
with kpi_cols2:
    st.metric("Avg Tenure", f"{filtered_df['tenure'].mean():.1f} months")
with kpi_cols3:
    st.metric("Total Charges", f"$ {filtered_df['TotalCharges'].mean():,.2f} ")

# Contract
st.write("### Contract")
contract_cols1, contract_cols2  = st.columns(2)

with contract_cols1: 
    st.write("***Contract Type v Churn***")
    fig1, ax = plt.subplots()
    sns.barplot(data=filtered_df, x='Contract', y='Churn', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax)
    st.pyplot(fig1)

with contract_cols2:
    st.write("***Contract Type v Montly Charges***")
    fig2, ax2 = plt.subplots()
    sns.barplot(data=filtered_df, x='Contract', y='MonthlyCharges', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax2)
    st.pyplot(fig2)

st.write("*Key observations:*\n\n * Contract types really play a key factor in the churn rate.\n\n * Associated, they have the highest monthly charges on average. ")

# Gender
st.write("### Gender")
gender_cols1, gender_cols2  = st.columns(2)

with gender_cols1:
    st.write("***Gender v Churn***")
    fig3, ax3 = plt.subplots()
    sns.barplot(data=filtered_df, x='gender', y='Churn', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax3)
    st.pyplot(fig3)

with gender_cols2:
    st.write("***Gender v Monthly Charges***")
    fig4, ax4 = plt.subplots()
    sns.barplot(data=filtered_df, x='gender', y='MonthlyCharges', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax4)
    st.pyplot(fig4)

st.write("*Key observations:*\n\n * The churn rate is not significantly between Female and Male Customers. ")

# Internet Distribution
st.write("### Internet Service Distribution")

internet_cols1, internet_cols2  = st.columns(2)
with internet_cols1:
    st.write("***Internet Service v Churn***")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, x='InternetService', y='Churn', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax)
    st.pyplot(fig)

with internet_cols2:
    st.write("***Internet Service v Monthly Charge***")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, x='InternetService', y='MonthlyCharges', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax)
    st.pyplot(fig)

st.write("*Key observations:*\n\n * Although Fiber Optic reflects a large percentage of users in the dataset, it has the largest churn rate \n\n * Fiber Optic users experience the highest monthly charge as well ")


# Payment Method
st.write("### Payment Method")
tenure_cols1, tenure_cols2  = st.columns(2)
with tenure_cols1:
    st.write("***Payment Method v Churn***")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, y='PaymentMethod', x='Churn', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax)
    st.pyplot(fig)

with tenure_cols2:
    st.write("***Payment Method v Monthly Charge***")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, y='PaymentMethod', x='MonthlyCharges', 
        estimator=lambda x: sum(x)/len(x), 
        ax=ax)
    st.pyplot(fig)

st.write("*Key observations:*\n\n * Electronic check customers seem to have a terrible experience using our services reflected by the exorbitant churn rate ")

st.markdown("# 📌 Business Recommendations")
st.write("""
- **Contract Strategy:** Offer incentives for long-term contracts to reduce churn.
- **Fiber Optic Users:** Investigate service quality and pricing—highest churn and charges.
- **Electronic Check Users:** Simplify payment experience or offer alternatives.
""")
