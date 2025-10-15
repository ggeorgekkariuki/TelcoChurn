import streamlit as st

# Page title
analysis_page = st.Page('analysis.py', title='Visualisations')
eda_page = st.Page('eda.py', title="Data Exploration")

# Navigation
pg = st.navigation([analysis_page, eda_page])

# Run selected page
pg.run()

