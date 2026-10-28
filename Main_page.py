import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the pages
introduction = st.Page("page_1.py", title="Introduction", icon="🎈")
hypothesis = st.Page("page_2.py", title="Data Preparation", icon="❄️")
answer = st.Page("page_3.py", title="Hypothesis Testing", icon="🎉")
conclusion = st.Page("page_4.py", title="Conclusion", icon="🏁") 

# Set up navigation
pg = st.navigation([introduction, hypothesis, answer, conclusion])

# Run the selected page
pg.run()
 
