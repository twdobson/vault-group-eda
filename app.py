import pickle

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
from dash.dependencies import Output, Input

with open("graphs.pickle", "rb") as reader:
    graphs = pickle.load(reader)

with open("samples.pickle", "rb") as reader:
    samples = pickle.load(reader)

with open("graphs_type_2.pickle", "rb") as reader:
    graphs_type_2 = pickle.load(reader)

with open("samples_type_2.pickle", "rb") as reader:
    samples_type_2 = pickle.load(reader)

_type_1_duressed_unit_data = pd.read_pickle('type_1_duressed_unit_data.pkl')

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.H1('Vault data exploration'),
        dcc.Markdown(open('Notes.md').read()),
        html.Hr(),
        html.H2('Data type 1'),
        html.Br(),
        html.H3('Data samples per categorical variable'),
        html.Label(
            [
                html.Label(
                    id='label-select-a-categorical-variable',
                    children=["Select a category"],

                ),
                dcc.Dropdown(
                    id='dropdown-select-a-category',
                    options=[
                        {'label': key, 'value': key}
                        for key
                        in samples.keys()
                    ],
                    value=None,
                    style={'width': 300}
                ),
            ]
        ),
        html.Br(),
        html.Label(
            [
                html.Label(
                    id='label-select-a-value-within-category',
                    children=["Select a value within category"]
                ),
                dcc.Dropdown(
                    id='dropdown-select-a-value-within-category',
                    value=None,
                    multi=True,
                    style={'width': 300}
                ),
            ]
        ),
        html.Br(),
        html.Div(
            dash_table.DataTable(
                id='datatable-samples',
                style_cell={'textAlign': 'left'},
            )
        ),
        html.Hr(),
        html.H3('Categorical variable distribution'),
        *[
            dcc.Graph(figure=graphs.get(column))
            for column
            in graphs
        ],
        html.Br(),
        html.Hr(),
        html.H3('Time series of duressed unit logs'),
        html.Label(
            [
                html.Label(
                    id='label-select-a-duress-unit',
                    children=["Select a unit (All units have had duress detected)"]
                ),
                dcc.Dropdown(
                    id='dropdown-select-a-duress-unit',
                    value=None,
                    style={'width': 300},
                    options=[
                        {'label': unique_value, 'value': unique_value}
                        for unique_value
                        in set(_type_1_duressed_unit_data['unit_id'])
                    ]
                ),
            ]
        ),
        dcc.Graph(
            id='graph-time-series-duress-units'
        ),
        html.Br(),
        html.Hr(),
        # Type 2 starts
        html.H2('Data type 2'),
        html.Br(),
        html.H3('Data samples per categorical variable'),
        html.Label(
            [
                html.Label(
                    id='label-select-a-categorical-variable-type-2',
                    children=["Select a category"],

                ),
                dcc.Dropdown(
                    id='dropdown-select-a-category-type-2',
                    options=[
                        {'label': key, 'value': key}
                        for key
                        in samples_type_2.keys()
                    ],
                    value=None,
                    style={'width': 300}
                ),
            ]
        ),
        html.Br(),
        html.Label(
            [
                html.Label(
                    id='label-select-a-value-within-category-type-2',
                    children=["Select a value within category"]
                ),
                dcc.Dropdown(
                    id='dropdown-select-a-value-within-category-type-2',
                    value=None,
                    multi=True,
                    style={'width': 300}
                ),
            ]
        ),
        html.Br(),
        html.Div(
            dash_table.DataTable(
                id='datatable-samples-type-2',
                style_cell={'textAlign': 'left'},
            )
        ),
        html.Hr(),
        html.H3('Categorical variable distribution'),
        *[
            dcc.Graph(figure=graphs_type_2.get(column))
            for column
            in graphs_type_2
        ],

    ]
)


@app.callback(
    [
        Output('datatable-samples', 'data'),
        Output('datatable-samples', 'columns'),
        Output('dropdown-select-a-value-within-category', 'options')
    ],
    [
        Input('dropdown-select-a-category', 'value'),
        Input('dropdown-select-a-value-within-category', 'value')
    ]
)
def filter_samples(category, value):
    with open("samples.pickle", "rb") as reader:
        samples = pickle.load(reader)

    if not category:
        df = pd.concat([
            samples.get(key)
            for key
            in samples
        ])

        options_nested = [
            df[key].unique()
            for key
            in samples
        ]

        options = [item for sublist in options_nested for item in sublist]

        options = [
            {'label': value, 'value': value}
            for value
            in options
        ]

        return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], options
    else:
        df = samples.get(category)

        options = df[category].unique()

        options = [
            {'label': value, 'value': value}
            for value
            in options
        ]

        if value:
            df = df[df[category].isin(value)]

        return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], options


@app.callback(
    [
        Output('datatable-samples-type-2', 'data'),
        Output('datatable-samples-type-2', 'columns'),
        Output('dropdown-select-a-value-within-category-type-2', 'options')
    ],
    [
        Input('dropdown-select-a-category-type-2', 'value'),
        Input('dropdown-select-a-value-within-category-type-2', 'value')
    ]
)
def filter_samples_type_2(category, value):
    with open("samples_type_2.pickle", "rb") as reader:
        samples = pickle.load(reader)

    if not category:
        df = pd.concat([
            samples.get(key)
            for key
            in samples
        ])

        options_nested = [
            df[key].unique()
            for key
            in samples
        ]

        options = [item for sublist in options_nested for item in sublist]

        options = [
            {'label': value, 'value': value}
            for value
            in options
        ]

        return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], options
    else:
        df = samples.get(category)

        options = df[category].unique()

        options = [
            {'label': value, 'value': value}
            for value
            in options
        ]

        if value:
            df = df[df[category].isin(value)]

        return df.to_dict('records'), [{"name": i, "id": i} for i in df.columns], options


@app.callback(
    Output('graph-time-series-duress-units', 'figure'),
    Input('dropdown-select-a-duress-unit', 'value')
)
def show_duress_timeseries(unit_id):
    type_1_duressed_unit_data = pd.read_pickle('type_1_duressed_unit_data.pkl')

    unit_records = type_1_duressed_unit_data[type_1_duressed_unit_data['unit_id'] == unit_id]

    fig = px.scatter(
        unit_records,
        y="capture_time",
        x=[1] * unit_records.shape[0],
        color="facility",
        text="facility",
        hover_data=['data'],
        range_x=[1, 1]
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
