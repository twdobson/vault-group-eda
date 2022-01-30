from locale import normalize
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import datetime
import plotly.express as px

pd.options.display.max_rows = 500
pd.options.display.float_format = '{:.5f}'.format


df = pd.read_pickle("type_1_df.pkl")
print(df['data'].value_counts())

error_messages = df[df['data'].str.contains("error")]
print(error_messages['type'].value_counts())
#type = '0' are all of the errors
#print(error_messages)

time_diff = pd.to_datetime(error_messages["receive_time"]) - pd.to_datetime(error_messages["capture_time"]) 
print(time_diff.mean())
#now looking at date/times of errors: 0 days 05:50:56.732475082

non_error_messages = df[~df['data'].str.contains("error")]
print(non_error_messages['type'].value_counts())
#print(non_error_messages)

time_diff = pd.to_datetime(non_error_messages["receive_time"]) - pd.to_datetime(non_error_messages["capture_time"]) 
#print(time_diff.mean())
#0 days 14:32:18.494144381

#Now let's explore when the average error occurs
# error_cap_times =  pd.to_datetime(error_messages["capture_time"])
# mean_ect = error_cap_times
# print(mean_ect)



#Check 'duress', 'failed', 'locked
duress_df = df[df['data'].str.contains("DURESS")]
print(duress_df)
fig = px.scatter(duress_df, x="unit_id", y="capture_time", title='Time at which Units experience Duress')
fig.show()

locked_df = df[df['data'].str.contains("Locked")]
print(locked_df)
fig = px.scatter(locked_df, x="capture_time", y="unit_id", title='Time at which Units Locked')
fig.show()

failed_df = df[df['data'].str.contains("fail")]
print(failed_df["data"].value_counts())
fig = px.scatter(failed_df, x="capture_time", y="unit_id", title='Time at which Units Falied')
fig.show()

"""Type 2"""
df = pd.read_pickle("type_2_df.pkl")

duress_df = df[df['data'].str.contains("DURESS")]
print(duress_df)
fig = px.scatter(duress_df, x="datetime", y="facility", title='Time at which Facilities experience Duress: Type 2 Data')
fig.show()

locked_df = df[df['data'].str.contains("Locked")]
print(locked_df)
fig = px.scatter(locked_df, x="datetime", y="user", title='Time at which Units Locked: Type 2 Data')
fig.show()

failed_df = df[df['data'].str.contains("fail")]
print(failed_df["data"].value_counts())
fig = px.scatter(failed_df, x="datetime", y="user", title='Time at which Units Falied: Type 2 Data')
fig.show()












