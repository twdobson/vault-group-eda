
from calendar import week
from pickletools import string1
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot 
import requests
import urllib.parse
import datetime
from numpy import save
from numpy import load


#pd.options.display.max_rows = 500
pd.set_option('display.max_rows', 500)
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
    print(string)
    string_length = len(string)
    print(string_length)
    #Populates from the top
    if string_length == 9:
        #1 lockers
        array_rep = np.zeros(shape = (9,1))
        l1 = string[4]
        array_rep[1] = 2
        array_rep[2] = 2
        array_rep[3] = 2
        array_rep[4] = 2
        array_rep[5] = 2
        array_rep[6] = 2
        array_rep[7] = 2
        array_rep[8] = 2

        if l1 == 'L':
            array_rep[0] = 1

    elif string_length == 11:
        #2 lockers
        array_rep = np.zeros(shape = (9,1))
        l1 = string[4]
        l2 = string[6]
        array_rep[2] = 2
        array_rep[3] = 2
        array_rep[4] = 2
        array_rep[5] = 2
        array_rep[6] = 2
        array_rep[7] = 2
        array_rep[8] = 2

        
        if l1 == 'L':
            array_rep[0] = 1
        if l2 == 'L':
            array_rep[1] = 1
    elif string_length == 13:
        #3 lockers
        array_rep = np.zeros(shape = (9,1))
        l1 = string[4]
        l2 = string[6]
        l3 = string[8]
        array_rep[3] = 2
        array_rep[4] = 2
        array_rep[5] = 2
        array_rep[6] = 2
        array_rep[7] = 2
        array_rep[8] = 2

        if l1 == 'L':
            array_rep[0] = 1
        if l2 == 'L':
            array_rep[1] = 1
        if l3 == 'L':
            array_rep[2] = 1
    elif string_length == 15:
        #4 lockers
        array_rep = np.zeros(shape = (9,1))
        l1 = string[4]
        l2 = string[6]
        l3 = string[8]
        l4 = string[10]
        array_rep[4] = 2
        array_rep[5] = 2
        array_rep[6] = 2
        array_rep[7] = 2
        array_rep[8] = 2

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
        array_rep = np.zeros(shape = (9,1))
        l1 = string[4]
        l2 = string[6]
        l3 = string[8]
        l4 = string[10]
        l5 = string[12]
        array_rep[5] = 2
        array_rep[6] = 2
        array_rep[7] = 2
        array_rep[8] = 2

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
    elif string_length == 19:
            #6 lockers
            array_rep = np.zeros(shape = (9,1))
            l1 = string[4]
            l2 = string[6]
            l3 = string[8]
            l4 = string[10]
            l5 = string[12]
            l6 = string[14]

            array_rep[6] = 2
            array_rep[7] = 2
            array_rep[8] = 2

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
    elif string_length == 21:
            #7 lockers
            array_rep = np.zeros(shape = (9,1))
            l1 = string[4]
            l2 = string[6]
            l3 = string[8]
            l4 = string[10]
            l5 = string[12]
            l6 = string[14]
            l7 = string[16]

            array_rep[7] = 2
            array_rep[8] = 2

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
            if l7 == 'L':
                array_rep[6] = 1
    elif string_length == 23:
            #8 lockers
            array_rep = np.zeros(shape = (9,1))
            l1 = string[4]
            l2 = string[6]
            l3 = string[8]
            l4 = string[10]
            l5 = string[12]
            l6 = string[14]
            l7 = string[16]
            l8 = string[18]

            array_rep[8] = 2

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
            if l7 == 'L':
                array_rep[6] = 1
            if l8 == 'L':
                array_rep[7] == 1
    elif string_length == 25:
            #9 lockers
            array_rep = np.zeros(shape = (9,1))
            l1 = string[4]
            l2 = string[6]
            l3 = string[8]
            l4 = string[10]
            l5 = string[12]
            l6 = string[14]
            l7 = string[16]
            l8 = string[18]
            l9 = string[20]

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
            if l7 == 'L':
                array_rep[6] = 1
            if l8 == 'L':
                array_rep[7] = 1
            if l9 == 'L':
                array_rep[8] = 1
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
    unit_array = np.zeros(shape = (9,max_cols+1))
    cumulative_array = np.zeros(shape = (9,max_cols+1))

    for row in filtered_df['data']:
        slave_no, converted_beginning, converted_end = final_convert(row)
        array_diffs = abs(converted_end - converted_beginning)
        array_diffs = np.reshape(array_diffs,(9))
        cumulative_array[:,int(slave_no)] += array_diffs

        unit_array[:,int(slave_no)] = np.reshape(converted_beginning,(9))
        unit_array[:,int(slave_no)] = np.reshape(converted_end,(9))

    fig = px.imshow(cumulative_array,text_auto=True,title=f"Graph of Unit {unit_id} over December")

    return cumulative_array,fig

def create_average_plot(unit_list,df,columns):
    average_array = np.zeros(shape=(9,columns))
    count = 0
    for unit in unit_list:
        filtered_df = df[df["unit_id"] == str(unit)]
        filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

        usage_array, _ = create_individual_plot(filtered_df,unit)

        if usage_array.shape[1] == columns:
            average_array += usage_array
            count +=1

    average_array = average_array/count
    fig = px.imshow(average_array,text_auto=True,title=f"Average Utilisation of all units with {columns} columns")
    return fig

def create_average_plot_all(unit_list,df):

    average_array1 = np.zeros(shape=(9,1))
    average_array2 = np.zeros(shape=(9,2))
    average_array3 = np.zeros(shape=(9,3))
    average_array4 = np.zeros(shape=(9,4))
    average_array5 = np.zeros(shape=(9,5))
    average_array6 = np.zeros(shape=(9,6))
    average_array7 = np.zeros(shape=(9,7))
    average_array8 = np.zeros(shape=(9,8))
    average_array9 = np.zeros(shape=(9,9))

    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0

    for unit in unit_list:
        filtered_df = df[df["unit_id"] == str(unit)]
        filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]
        usage_array, _ = create_individual_plot(filtered_df,unit)

        if usage_array.shape[1] == 1:
            average_array1 += usage_array
            count1 +=1
        elif usage_array.shape[1] == 2:
            average_array2 += usage_array
            count2 +=1        
        elif usage_array.shape[1] == 3:
            average_array3 += usage_array
            count3 +=1  
        elif usage_array.shape[1] == 4:
            average_array4 += usage_array
            count4 +=1  
        elif usage_array.shape[1] == 5:
            average_array5 += usage_array
            count5 +=1
        elif usage_array.shape[1] == 6:
            average_array6 += usage_array
            count6 +=1
        elif usage_array.shape[1] == 7:
            average_array7 += usage_array
            count7 +=1
        elif usage_array.shape[1] == 8:
            average_array8 += usage_array
            count8 +=1
        elif usage_array.shape[1] == 9:
            average_array9 += usage_array
            count9 +=1
      
    average_array1 = average_array1//count1
    average_array2 = average_array2//count2
    average_array3 = average_array3//count3
    average_array4 = average_array4//count4
    average_array5 = average_array5//count5
    average_array6 = average_array6//count6
    average_array7 = average_array7//count7
    average_array8 = average_array8//count8
    average_array9 = average_array9//count9

    save("average_array_1.npy",average_array1)
    save("average_array_2.npy",average_array2)
    save("average_array_3.npy",average_array3)
    save("average_array_4.npy",average_array4)
    save("average_array_5.npy",average_array5)
    save("average_array_6.npy",average_array6)
    save("average_array_7.npy",average_array7)
    save("average_array_8.npy",average_array8) #nan
    save("average_array_9.npy",average_array9) #nan

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




locations = pd.read_pickle("data\\processed\\sites_with_geo_coding.pickle")
print(locations)

df = pd.read_pickle("type_1_df.pkl")


filtered_df = df[df["unit_id"] == "cv730"]
filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

converted_time = pd.to_datetime(filtered_df["capture_time"])
print(converted_time)


#merge









"""
Codes:
- 0: Unlocked
- 1: Locked
- 2: Unused locker 

Slaves start from 0!

"""



