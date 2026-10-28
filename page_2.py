import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Data exploration and preparation")

st.subheader("We started with data from 3 different datasets")

st.markdown("The first holds information on the weather in London. It holds 8402 rows and 11 columns. "
            "Source is Brightspace")

st.markdown("The second holds information on metro data in London. It holds 470 rows and 16 columns. "
            "Source is Brightspace")

st.markdown("The third holds information on bike rental data in London. The form will be explained later on. "
            "Source is 'https://cycling.data.tfl.gov.uk/'")


st.subheader("Challenges in the data preparation")

st.markdown("The metro and weather datasets were fairly easy to use as they were")

# mark a bulletpoint of problems (53 datasets to download) (matching rental station name to a location) (size of the datafile)

st.markdown("**The bike rental data was much more challenging:**\n"
            "- Dataframes hold information on bike rentals for only a single week. \n"
            "To get data for a year we needed to retrieve and combine 53 datasets. \n"
            "- This made a total dataset of more than 10.000.000 rows. \n"
            "- Rental stations are identified by name. We needed to geolocate them. ")


st.markdown("The notebooks used to prepare the data and test the visuals in the presentation with all steps are also on GitHub: "
            "(https://github.com/jurre-m/Bike-Metro-case)")
 
