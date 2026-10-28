import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the pages
introduction = st.Page("page_1.py", title="Introduction", icon="🎈")
data_preparation = st.Page("page_2.py", title="Data Preparation", icon="❄️")
distance = st.Page("page_3.py", title="Distance from Metro", icon="🎉")
weather = st.Page("page_4.py", title="Weather vs Rental", icon="🏁") 
conclusion = st.Page("page_5.py", title="Conclusion", icon="🏁")

# Set up navigation
pg = st.navigation([introduction, data_preparation, distance, weather, conclusion])

# Run the selected page
pg.run()

# Koppeling voor metrodataset
## https://dlo.mijnhva.nl/content/enforced/764257-FT-6100DASC23-T--ALG-2627/metrogebruik_londen_2022.csv?isCourseFile=true&ou=764257

# Koppeling voor weerdataset:
## https://dlo.mijnhva.nl/content/enforced/764257-FT-6100DASC23-T--ALG-2627/weather_london.csv?isCourseFile=true&ou=764257
