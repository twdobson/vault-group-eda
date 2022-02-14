import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import Controller
from datetime import datetime

st.title("Vault Intelligence Platform")
st.header("Helping you make Data-Driven Decisions, swiftly")

add_image = st.sidebar.image("data\\assets\\VG_Logo.jpg")
option_list = ("Individual Vault Wear & Tear Analysis","Average Vault Wear & Tear Analysis","Individual Vault Time Analysis","Compare Vault Locations Across Time")
add_selectbox = st.sidebar.selectbox("Please select a view:",option_list)

data = pd.read_pickle("type_1_df_merged.pkl")
unit_ids = data["unit_id"].unique()
locations = data["store_name"].unique()

if add_selectbox == "Individual Vault Wear & Tear Analysis":
    st.header("Individual Vault Wear & Tear Analysis")
    option = st.selectbox("Please select vault unit you'd like to explore:",list(locations))

    filtered_df = data[data["store_name"] == str(option)]
    filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

    usage_array, figure = Controller.create_individual_plot(filtered_df,option)

    st.plotly_chart(figure,sharing = "streamlit")
elif add_selectbox == "Average Vault Wear & Tear Analysis":
    st.header("Average Vault Wear & Tear Analysis")
    
    config = st.selectbox("Please select Config Below",Controller.fetch_configurations())

    average_plot, fig = Controller.fetch_average(config)
    st.plotly_chart(fig,sharing = "streamlit")
elif add_selectbox == "Individual Vault Time Analysis":

    option = st.selectbox("Please select vault unit you'd like to explore:",list(locations))
    filtered_df = data[data["store_name"] == str(option)] #filter by location

    start_range, end_range = Controller.fetch_date_range(filtered_df)
    dates = st.date_input("Please Input Date",(start_range,end_range))

    filtered_df["cap_time_converted"] = pd.to_datetime(filtered_df["capture_time"]).dt.date
    filtered_df = filtered_df[(filtered_df["cap_time_converted"] >= dates[0] ) & (filtered_df["cap_time_converted"] <= dates[1])] #filter by date
    filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

    button = st.button("SEND HIM: ")

    if button:
        pie_df, whole_week = Controller.utilisation_by_week(filtered_df,option)
        pie_plot = px.pie(pie_df,names = 0,values=1)
        st.plotly_chart(pie_plot,sharing = "streamlit") # ^Stacked^ Bar chart better here?

        bar_chart = px.bar(whole_week, x = "index",y = "day_of_week")
        st.plotly_chart(bar_chart,sharing = "streamlit")
elif add_selectbox == "Compare Vault Locations Across Time":

    options = st.multiselect("Please select vault unit you'd like to explore:",list(locations))
    filtered_df = data[data["store_name"].isin(options)] #filter by location

    start_range, end_range = Controller.fetch_date_range(filtered_df)
    dates = st.date_input("Please Input Date",(start_range,end_range))

    filtered_df["cap_time_converted"] = pd.to_datetime(filtered_df["capture_time"]).dt.date
    filtered_df = filtered_df[(filtered_df["cap_time_converted"] >= dates[0] ) & (filtered_df["cap_time_converted"] <= dates[1])] #filter by date
    filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

    button = st.button("SEND HIM: ")

    if button:
        pie_df = Controller.compare_stores(filtered_df,options)
        pie_plot = px.pie(pie_df,names = "Store",values="Count")
        st.plotly_chart(pie_plot,sharing = "streamlit") # ^Stacked^ Bar chart better here?
