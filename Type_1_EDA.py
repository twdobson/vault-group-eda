
from calendar import week
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot 
import requests
import urllib.parse
import datetime

#pd.options.display.max_rows = 500
pd.set_option('display.max_rows', 50)
pd.set_option("expand_frame_repr", True)
pd.options.display.float_format = '{:.5f}'.format
pd.set_option("max_colwidth", None)


def num_cols(df):
    max_cols = 0
    for row in df['data']:
        slave_number = int(row[22])
        if slave_number > max_cols:
            max_cols = slave_number
    return max_cols

def convert_string(string):
    string_length = len(string)
    #Populates from the top
    if string_length == 11:
        #2 lockers
        array_rep = np.zeros(shape = (6,1))
        l1 = string[4]
        l2 = string[6]
        array_rep[2] = 2
        array_rep[3] = 2
        array_rep[4] = 2
        array_rep[5] = 2
        if l1 == 'L':
            array_rep[0] = 1
        if l2 == 'L':
            array_rep[1] = 1
    elif string_length == 13:
        #3 lockers
        array_rep = np.zeros(shape = (6,1))
        l1 = string[4]
        l2 = string[6]
        l3 = string[8]
        array_rep[3] = 2
        array_rep[4] = 2
        array_rep[5] = 2

        if l1 == 'L':
            array_rep[0] = 1
        if l2 == 'L':
            array_rep[1] = 1
        if l3 == 'L':
            array_rep[2] = 1
    elif string_length == 15:
        #4 lockers
        array_rep = np.zeros(shape = (6,1))
        l1 = string[4]
        l2 = string[6]
        l3 = string[8]
        l4 = string[10]
        array_rep[4] = 2
        array_rep[5] = 2

        if l1 == 'L':
            array_rep[0] = 1
        if l2 == 'L':
            array_rep[1] = 1
        if l3 == 'L':
            array_rep[2] = 1
        if l4 == 'L':
            array_rep[3] = 1
    elif string_length == 17:
        #5 lockers
        array_rep = np.zeros(shape = (6,1))
        l1 = string[4]
        l2 = string[6]
        l3 = string[8]
        l4 = string[10]
        l5 = string[12]
        array_rep[5] = 2
        if l1 == 'L':
            array_rep[0] = 1
        if l2 == 'L':
            array_rep[1] = 1
        if l3 == 'L':
            array_rep[2] = 1
        if l4 == 'L':
            array_rep[3] = 1
        if l5 == 'L':
            array_rep[4] = 1
    if string_length == 19:
            #6 lockers
            array_rep = np.zeros(shape = (6,1))
            l1 = string[4]
            l2 = string[6]
            l3 = string[8]
            l4 = string[10]
            l5 = string[12]
            l6 = string[14]
            if l1 == 'L':
                array_rep[0] = 1
            if l2 == 'L':
                array_rep[1] = 1
            if l3 == 'L':
                array_rep[2] = 1
            if l4 == 'L':
                array_rep[3] = 1
            if l5 == 'L':
                array_rep[4] = 1
            if l6 == 'L':
                array_rep[5] = 1
    return array_rep

def final_convert(row):
    slave_number = row[22] #starts at zero
    
    start_index_1 = row.find('S')
    end_index_1 = row.find('E')
    
    begin_state = row[start_index_1-1:end_index_1+2]
    end_state = row[end_index_1+4:]

    start_index_2 = end_state.find('S')
    end_index_2 = end_state.find('E')
    end_state = end_state[start_index_2-1:end_index_2+2]

    converted_begin_state = convert_string(begin_state)
    converted_end_state = convert_string(end_state)

    return slave_number, converted_begin_state,converted_end_state

def create_individual_plot(filtered_df,unit_id):
    max_cols = int(num_cols(filtered_df))
    unit_array = np.zeros(shape = (6,max_cols+1))
    cumulative_array = np.zeros(shape = (6,max_cols+1))

    for row in filtered_df['data']:
        slave_no, converted_beginning, converted_end = final_convert(row)
        array_diffs = abs(converted_end - converted_beginning)
        array_diffs = np.reshape(array_diffs,(6))
        cumulative_array[:,int(slave_no)] += array_diffs

        unit_array[:,int(slave_no)] = np.reshape(converted_beginning,(6))
        unit_array[:,int(slave_no)] = np.reshape(converted_end,(6))

    fig = px.imshow(cumulative_array,text_auto=True,title=f"Graph of Unit {unit_id} over December")

    return cumulative_array,fig

def create_average_plot(unit_list,df,columns):
    average_array = np.zeros(shape=(6,columns))
    count = 0
    for unit in unit_list:
        filtered_df = df[df["unit_id"] == str(unit)]
        filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]
        try:
            usage_array, _ = create_individual_plot(filtered_df,unit)
            if usage_array.shape[1] == columns:
                average_array += usage_array
                count +=1
        except:
            print("Error")
    average_array = average_array/count
    fig = px.imshow(average_array,text_auto=True,title=f"Average Utilisation of all units with {columns} columns")
    return fig

def utilisation_by_week(filtered_df, unit):
    converted_time = pd.to_datetime(filtered_df["capture_time"])
    filtered_df["day_of_week"] = converted_time.dt.dayofweek #gives only the index(0-monday,6-sunday)
    
    weekend_df = filtered_df[filtered_df["day_of_week"] >= 5]
    weekend_array, weekend_fig = create_individual_plot(weekend_df,unit)
    weekend_sum = np.sum(weekend_array)
    
    week_df = filtered_df[filtered_df["day_of_week"] < 5]
    week_array, week_fig = create_individual_plot(week_df,unit)
    week_sum = np.sum(week_array)
    
    #pie_df = pd.DataFrame(data = {"Week Utilisation":[int(week_sum)],"Weekend Utilisation":[int(weekend_sum)]})
    pie_df = pd.DataFrame(data = [["Weekly Utilisation",week_sum],["Weekend Utilisation",weekend_sum]])
    
    return pie_df

locations = pd.read_csv("Site Store Addresses.csv")#Unit 1
locations.rename({'Unit 1': 'unit_id'}, axis=1, inplace=True)
print(locations.dtypes)

data_df = pd.read_pickle("type_1_df.pkl")
data_df["success"] = data_df["success"].astype(object)
data_df["type"] = data_df["type"].astype(object)
print(data_df.dtypes)

# filtered_df = data_df[data_df["unit_id"] == "cv730"]
# filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

#converted_time = pd.to_datetime(filtered_df["capture_time"])
#print(converted_time)

data_df.join(locations,on = "unit_id",how = "left")
print(data_df.columns)























# def get_location():
#     GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

#     params = {
#         'address': 'Cresta Mall, Gauteng',
#         'sensor': 'false',
#         'region': 'South Africa'
#     }
#     # Do the request and get the response data
#     req = requests.get(GOOGLE_MAPS_API_URL, params=params)
#     res = req.json()
#     # Use the first result
#     print(res)
#     result = res['results'][0]
#     geodata = dict()
#     geodata['lat'] = result['geometry']['location']['lat']
#     geodata['lng'] = result['geometry']['location']['lng']
#     geodata['address'] = result['formatted_address']

#     print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))


# get_location()



"""Codes:
- 0: Unlocked
- 1: Locked
- 2: Unused locker 

Slaves start from 0!

11085630    2021-12-10T16:06:54.6Z  Locker state on slave 1 changed from [S]-U-L-L-U-L-L-[E] to [S]-L-L-L-L-L-L-[E]
11085940   2021-12-10T16:07:26.31Z      Locker state on slave 0 changed from [S]-L-U-L-L-L-[E] to [S]-L-L-L-L-L-[E]
12592533  2021-12-12T11:00:46.251Z              Locker state on slave 4 changed from [S]-U-L-U-[E] to [S]-L-L-U-[E]
12592544  2021-12-12T11:00:46.601Z  Locker state on slave 2 changed from [S]-U-L-L-L-L-L-[E] to [S]-L-L-L-L-L-L-[E]
12656031  2021-12-12T12:31:48.461Z              Locker state on slave 4 changed from [S]-L-L-U-[E] to [S]-L-L-L-[E]
12656545  2021-12-12T12:31:54.032Z  Locker state on slave 1 changed from [S]-L-L-L-L-U-L-[E] to [S]-L-L-L-L-L-L-[E]
13830844  2021-12-13T15:55:06.937Z  Locker state on slave 1 changed from [S]-L-L-L-U-L-L-[E] to [S]-L-L-L-L-L-L-[E]

"""



#Will focus on 'Capture Time' - assuming this is the local (on-device) time the event occurred
#Assume all lockers start out as unlocked first
