import pandas as pd


pd.options.display.max_rows = 500
pd.options.display.max_columns = 5100
pd.options.display.width = 2000
pd.options.display.max_colwidth = 1000


log_data = []
print('reading in raw data')
with open('raw_logs.log', 'r') as read:
    for line in read:
        evaluation = eval(line.replace('true', 'True'))
        log_data.append(evaluation)

for l in range(100):
    print(log_data[l])

print('getting keys for data')
keys = [l.keys() for l in log_data]
keys_s = pd.Series(keys)
log_keys = keys_s.value_counts()


print('creating type 1 dataframes')
type_1_data = [l for l in log_data if 'success' in l.keys()]
type_1_df = pd.DataFrame(type_1_data)
type_1_df.to_pickle('./type_1_df.pkl')

print('creating type 2 dataframes')
type_2_data = [l for l in log_data if 'datetime' in l.keys()]
type_2_df = pd.DataFrame(type_2_data)
type_2_df.to_pickle('./type_2_df.pkl')
