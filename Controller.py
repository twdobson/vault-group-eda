
import pandas as pd
import numpy as np
import plotly.express as px
import pickle

#pd.options.display.max_rows = 500
pd.set_option('display.max_rows', 500)
pd.set_option("expand_frame_repr", True)
pd.options.display.float_format = '{:.5f}'.format
pd.set_option("max_colwidth", None)

MAX_ROW_LENGTH = 9
#determine how many columns are in each vault
def num_cols(df):
    max_cols = 0
    for row in df['data']:
        slave_number = int(row[22])
        if slave_number > max_cols:
            max_cols = slave_number
    return max_cols

def max_row_calc(filtered_df):
    max_rows = 0
    for row in filtered_df["data"]:
        
        _, _, converted_end = final_convert(row)

        last_row_end = np.where(converted_end == 2)

        this_last_row = last_row_end[0][0]

        if this_last_row > max_rows:
            max_rows = this_last_row

    return max_rows

def convert_string(string):
    string_length = len(string)
    #Populates from the top
    if string_length == 9:
        #1 lockers
        array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
        array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
        array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
        array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
        array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
            array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
            array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
            array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
            array_rep = np.zeros(shape = (MAX_ROW_LENGTH,1))
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
    """
    Basis method to compute cumulative utilisation across the provided time period.
    
    """
    max_cols = int(num_cols(filtered_df))
    max_rows = max_row_calc(filtered_df)
    cumulative_array = np.zeros(shape = (max_rows,max_cols+1))

    for row in filtered_df['data']:
        slave_no, converted_beginning, converted_end = final_convert(row) #outputs 9 rows at this point
        array_diffs = abs(converted_end - converted_beginning)
        array_diffs = array_diffs[:max_rows]
        array_diffs = np.reshape(array_diffs,(max_rows))
        cumulative_array[:,int(slave_no)] += array_diffs
    fig = px.imshow(cumulative_array,text_auto=True,title=f"Graph of Unit {unit_id} over December")
    return cumulative_array,fig

def create_average_plot(unit_list,df,rows,columns):
    """Used to comput averages in real-time

        The concern here is that this script will take long time to run/inefficient. 
        Added script below to compute all at once and then fetch.
    
    """
    average_array = np.zeros(shape=(rows,columns))
    count = 0
    for unit in unit_list:
        try:
            filtered_df = df[df["unit_id"] == str(unit)]
            filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]
            usage_array, _ = create_individual_plot(filtered_df,unit)

            if usage_array.shape == (rows,columns):
                average_array += usage_array
                count +=1
        except:
            print(f"Something went wrong when scanning unit {unit}")
            pass

    average_array = average_array/count
    fig = px.imshow(average_array,text_auto=True,title=f"Average Utilisation of all units with {columns} columns and {rows} rows")
    return average_array, fig

def create_average_plot_script(unit_list, raw_df):
    """
    Batch script used to loop through a day/week/month's logs and store the average across all available configs.
    
    """
    matrix_dict = {}
    count_dict = {}
    for unit in unit_list:
        filtered_df = raw_df[raw_df["unit_id"] == str(unit)]
        filtered_df = filtered_df[filtered_df['data'].str.contains("Locker state")]

        max_cols = int(num_cols(filtered_df))
        max_rows = int(max_row_calc(filtered_df))
        shape = (max_rows,max_cols+1)
        shape = str(shape)
        cum_array, _ = create_individual_plot(filtered_df,unit)

        if shape in matrix_dict.keys():
            matrix_dict[shape] += cum_array
            count_dict[shape] += 1
        else:
            matrix_dict[shape] = cum_array
            count_dict[shape] = 1


    average_dict = {}
    for key in matrix_dict.keys():
        average_dict[key] = matrix_dict[key]/count_dict[key]

    with open("data\\processed\\ave_lookup_dict.pickle","wb") as file:
        pickle.dump(average_dict,file)

def fetch_configurations():
    """
    Used to fetch averages from above batch
    
    """
    with open("data\\processed\\ave_lookup_dict.pickle","rb") as file:
        average_dict = pickle.load(file)
    return average_dict.keys()

def fetch_average(shape):

    with open("data\\processed\\ave_lookup_dict.pickle","rb") as file:
        average_dict = pickle.load(file)

    fig = px.imshow(average_dict[shape], text_auto= True,title=f"Average Utilisation of all units with configuration: {shape}")

    return average_dict[shape], fig

def fetch_date_range(raw_df):
    raw_cap_time = raw_df["capture_time"]
    converted_time = pd.to_datetime(raw_cap_time)
    
    start_time = converted_time.min()
    end_time = converted_time.max()

    return start_time, end_time

def utilisation_by_week(filtered_df, unit):
    converted_time = pd.to_datetime(filtered_df["capture_time"])
    filtered_df["day_of_week"] = converted_time.dt.dayofweek #gives only the index(0-monday,6-sunday)

    mapping_function = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}

    weekend_df = filtered_df[filtered_df["day_of_week"] >= 5]
    weekend_array, _ = create_individual_plot(weekend_df,unit)
    weekend_sum = np.sum(weekend_array)
    weekend_df["day_of_week"] = weekend_df["day_of_week"].map(mapping_function)
    
    weekend_numbers = weekend_df["day_of_week"].value_counts()
    weekend_numbers = pd.DataFrame(weekend_numbers).reset_index()

    week_df = filtered_df[filtered_df["day_of_week"] < 5]
    week_array, _ = create_individual_plot(week_df,unit)
    week_sum = np.sum(week_array)
    week_df["day_of_week"] = week_df["day_of_week"].map(mapping_function)
    
    week_numbers = week_df["day_of_week"].value_counts()
    week_numbers = pd.DataFrame(week_numbers).reset_index()
    
    whole_df = week_numbers.append(weekend_numbers)

    pie_df = pd.DataFrame(data = [["Weekly Utilisation",week_sum],["Weekend Utilisation",weekend_sum]])
    
    return pie_df, whole_df

def compare_stores(filtered_df,options):
    final_df = pd.DataFrame(columns=["Store","Count"])
    for store in options:
        slice = filtered_df[filtered_df["store_name"] == store]
        array, _ = create_individual_plot(slice,store)
        sum = np.sum(array)
        length = len(final_df)

        final_df.loc[length] = [store,sum]

    return final_df

