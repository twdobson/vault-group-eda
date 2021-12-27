import pickle

import pandas as pd
import plotly.express as px

print('reading in data')
type_1_df = pd.read_pickle('type_1_df.pkl')
type_2_df = pd.read_pickle('type_2_df.pkl')

print(type_1_df.shape)  # 14734751 = 80%
print(type_2_df.shape)  # 3671089 = 20%
print(type_2_df[type_2_df['user'] == 'dummy'].shape)  # 3459390 # 95%

print(type_2_df[type_2_df['user'] == 'dummy'].groupby(['user', 'level', 'facility', 'data']).size())
# dummy  E      auth_login  ERROR!!!! DUMMY UNITS SHOULD NOT BE LOGGING IN!!!! There's an installation problem in the field!!!    2455201
#                           failed to log in                                                                                      1004189

type_2_df = type_2_df[type_2_df['user'] != 'dummy']

type_1_df[type_1_df.columns.drop(['capture_time', 'receive_time', 'data', 'success'])].nunique()
type_1_df['log_level'].value_counts()

samples = {}
graphs = {}
remove_values = {
    'type': [0],
}

samples_type_2 = {}
graphs_type_2 = {}

for column in ['level', 'facility']:
    column_sample = []
    for value in type_2_df[column].unique():
        print('*' * 100)
        print(value)
        print('-' * 100)
        sample = type_2_df[type_2_df[column] == value].sample(min(20, type_2_df[type_2_df[column] == value].shape[0]))
        column_sample.append(sample)
        print(sample)

    distribution = type_2_df[column].value_counts(normalize=True, dropna=False).round(4)
    fig = px.bar(
        x=distribution.index.astype(str),
        y=distribution,
        text=["{:.2%}".format(val) for val in distribution],
        title=column
    )
    fig.update_layout(
        {
            'xaxis': {'title': {'text': column}},
            'yaxis': {'title': {'text': 'proportion'}},
        }
    )

    graphs_type_2[column] = fig
    samples_type_2[column] = pd.concat(column_sample, axis=0)

for column in ['type', 'log_level', 'facility']:
    column_sample = []
    for value in type_1_df[column].unique():
        print('*' * 100)
        print(value)
        print('-' * 100)
        sample = type_1_df[type_1_df[column] == value].sample(20)
        column_sample.append(sample)
        print(sample)

    distribution = type_1_df[column].value_counts(normalize=True, dropna=False).round(4)
    fig = px.bar(
        x=distribution.index.astype(str),
        y=distribution,
        text=["{:.2%}".format(val) for val in distribution],
        title=column
    )
    fig.update_layout(
        {
            'xaxis': {'title': {'text': column}},
            'yaxis': {'title': {'text': 'proportion'}},
        }
    )

    fig.show()

    graphs[column] = fig
    samples[column] = pd.concat(column_sample, axis=0)

with open("graphs.pickle", "wb") as writer:
    pickle.dump(graphs, writer)

with open("samples.pickle", "wb") as writer:
    pickle.dump(samples, writer)

with open("graphs_type_2.pickle", "wb") as writer:
    pickle.dump(graphs_type_2, writer)

with open("samples_type_2.pickle", "wb") as writer:
    pickle.dump(samples_type_2, writer)
