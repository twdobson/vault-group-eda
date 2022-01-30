from email import header
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

import Type_1_EDA

st.title("Vault Intelligence Platform")
st.header("Helping you make Data-Driven Decisions, swiftly")

add_image = st.sidebar.image("VG_Logo.jpg")
option_list = ("Individual Vault Wear & Tear Analysis","Average Vault Wear & Tear Analysis","Vault Week/end Analysis")
add_selectbox = st.sidebar.selectbox("Please select a view:",option_list)

data = pd.read_pickle("type_1_df.pkl")
unit_ids = data["unit_id"].unique()

if add_selectbox == "Individual Vault Wear & Tear Analysis":
    st.header("Individual Vault Wear & Tear Analysis")
    option = st.selectbox("Please select vault unit you'd like to explore:",list(unit_ids))

    filtered_df = data[data["unit_id"] == str(option)]
    filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

    usage_array, figure = Type_1_EDA.create_individual_plot(filtered_df,option)

    st.plotly_chart(figure,sharing = "streamlit")
elif add_selectbox == "Average Vault Wear & Tear Analysis":
    st.header("Average Vault Wear & Tear Analysis")
    cols = st.selectbox("Please select Vault Columns you'd like to investigate:",[5,4,3])

    plot = Type_1_EDA.create_average_plot(unit_ids,data,cols)
    st.plotly_chart(plot,sharing = "streamlit")

elif add_selectbox == "Vault Week/end Analysis":
    option = st.selectbox("Please select vault unit you'd like to explore:",list(unit_ids))

    filtered_df = data[data["unit_id"] == str(option)]
    filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

    pie_df = Type_1_EDA.utilisation_by_week(filtered_df,option)

    pie_plot = px.pie(pie_df,names = 0,values=1)
    st.plotly_chart(pie_plot,sharing = "streamlit")
    