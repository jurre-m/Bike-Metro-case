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

st.markdown("The third holds information on bike rental data in London. The form will be given explained later on. "
            "Source is 'https://cycling.data.tfl.gov.uk/'")


st.subheader("Challenges in the data preparation")

st.markdown("The metro and weather datasets were fairly easy to use as they were")

# mark a bulletpoint of problems (53 datasets to download) (matching rental station name to a location) (size of the datafile)

st.markdown("**The bike rental data was much more challenging:**\n"
            "- Dataframes hold information on bike rentals for only a single week. \n"
            "To get data for a year we neede to retrieve 53 datasets. \n"
            "- This made a total dataset of more than 10.000.000 rows. \n"
            "- Rental stations are identified by name. We needed to geolocate them. ")



st.subheader("From raw data to a usable dataset")

url_1 = "df_usable_case2.csv"                               # read the csv straight from the repo

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(url_1)

steps = pd.DataFrame({
    "Step": ["Raw Olympic dataset",
             "Winter games removed",
             "Merged with NOC table (left join on NOC)",
             "Rows with missing height/weight removed",
             "Only games 1968-2016 (range of the population data)",
             "Merged with population data (left join on year + country)",
             "Unique athletes per games (one athlete, several events = 1)"],
    "Rows": [70000, 58467, 58467, 58275, 39421, len(df),
             len(df.drop_duplicates(["ID", "Year"]))],      # last two are calculated live from the csv
})
steps["Change"] = steps["Rows"].diff().fillna(0).astype(int)
st.dataframe(steps, hide_index=True)



st.subheader("Choices we made")

st.markdown(
    "- **Summer games only.** Our question is about chances to participate; winter sports depend heavily on climate, "
    "which would add a second explanation we cannot separate.\n"
    "- **Left join with the NOC table** kept every row (58.467 before and after). Missing country names "
    "(Singapore, Tuvalu, Refugee team, Unknown) were filled in by hand.\n"
    "- **192 rows dropped** because height and weight could not be filled in: the sport had no known values at all. "
    "Height and weight are not used to answer our question.\n"
    "- **1968-2016 only**, because the population data starts in 1970. For each games we estimated the population "
    "by linear interpolation between the measured years; 1968 gets the 1970 value.\n"
    "- **30 rows lost in the population merge**: 24 Individual Olympic Athletes and 6 Refugee Olympic Team. "
    "They have no country, so there is no population to compare with.\n"
    "- **Athletes are counted once per games.** 9.646 rows are the same athlete in more events. That is not an error, "
    "so we did not remove them from the data, but we count unique athletes in the analysis."
)



st.subheader("Quality checks")

col1, col2 = st.columns(2)
col1.metric("Fully duplicated rows", int(df.duplicated().sum()))
col2.metric("Same athlete, more events", int(df.duplicated(["ID", "Year"]).sum()))

st.markdown("Ranges of age, height and weight. Extremes are plausible: young gymnasts and swimmers, "
            "coxswains in rowing and heavyweight lifters.")
st.dataframe(df[["Age", "Height", "Weight"]].describe().round(1))



st.subheader("The final dataset")
st.dataframe(df)
st.markdown("The notebook with all steps is also on GitHub: "
            "[Olympic_workbook.ipynb](https://github.com/JesseKnibbe/Olympic-dataset-version-1/blob/main/Olympic_workbook.ipynb)")
 
