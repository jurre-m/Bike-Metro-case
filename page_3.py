import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Metro data analysis")

st.markdown("Our hypothesis: **bike rental stations close to metro stations get more traffic** ")

## url_1 = "df_usable_case2.csv"                               # read the csv straight from the repo, no web address needed

## @st.cache_data
## def load_data(url):
##    return pd.read_csv(url)

## df = load_data(url_1)

