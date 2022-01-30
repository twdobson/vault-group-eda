import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pickle
import dash_table
from PIL import Image
import numpy as np


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

with open("graphs.pickle", "rb") as reader:
    graphs = pickle.load(reader)

with open("samples.pickle", "rb") as reader:
    samples = pickle.load(reader)

with open("graphs_type_2.pickle", "rb") as reader:
    graphs_type_2 = pickle.load(reader)

with open("samples_type_2.pickle", "rb") as reader:
    samples_type_2 = pickle.load(reader)

_type_1_duressed_unit_data = pd.read_pickle('type_1_duressed_unit_data.pkl')


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Vault Group Data", className="display-4"),
        html.Img(id='logo-image',src='logo.png'),
        html.Hr(),
        html.P("Please select a section below:", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Tim's Notes", href="/", active="exact"),
                dbc.NavLink("Table Data", href="/page-1", active="exact"),
                dbc.NavLink("Graphs", href="/page-2", active="exact"),
                dbc.NavLink("Duress Units: An exploration", href = "/page-3",active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)


app.layout = html.Div([
                dcc.Location(id="url"),
                sidebar,
                content
        ])

# @app.callback(
#     Output("logo-image","children"),
#     Input("image-input","value")
# )
# def output_image(input):
#     img = np.array(Image.open(f"{input}"))
#     fig = px.imshow(img, color_continuous_scale="gray")
#     fig.update_layout(coloraxis_showscale=False)
#     fig.update_xaxes(showticklabels=False)
#     fig.update_yaxes(showticklabels=False)
#     return dcc.Graph(figure=fig)


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                # html.H1('Notes & Findings',
                #         style={'textAlign':'center'}),
                        dcc.Markdown(open('Notes.md').read())
                ]
    elif pathname == "/page-1":
        return [
                # html.H1('Data Tables',
                #         style={'textAlign':'center'}),
                dbc.Row(dbc.Col(html.H1('Data samples per categorical variable'))),
                html.Hr(),
                dbc.Row([dbc.Col(dcc.Dropdown(id='dropdown-select-a-category',
                                    placeholder='Select category to filter on',
                                    options=[
                                    {'label': key, 'value': key}
                                    for key
                                    in samples.keys()],
                                    value=None,
                                    style={'width': 500})),

                dbc.Col(dcc.Dropdown(id='dropdown-select-a-value-within-category', 
                                     placeholder='Select Value within category',
                                     value = None,
                                     multi = True,   
                                     style={"width": 500}))]),
                html.Br(),                     
                dbc.Row(dbc.Col(dash_table.DataTable(
                                            id='datatable-samples',
                                            style_cell={'textAlign': 'left','width':'auto'},
                                                )))
                ]
    elif pathname == "/page-2":
        return [
                #html.H1('Graphs of Key Variables', style={'textAlign':'center'}),
                dbc.Row(dbc.Col(html.H1("Categorical Variable Distributions"))),
                html.Hr(),
                dbc.Row(dbc.Col([dcc.Graph(figure=graphs.get(column)) for column in graphs]))
                ]
    elif pathname == "/page-3":
        return [
                html.H1('Time series of duressed unit logs', style={'textAlign':'center'}),
                html.Hr(),
                html.Label(
            [
                html.Label(
                    id='label-select-a-duress-unit',
                    children=["Select a unit (All units have had duress detected)"]),
                dcc.Dropdown(
                    id='dropdown-select-a-duress-unit',
                    value=None,
                    style={'width': 300},
                    options=[
                        {'label': unique_value, 'value': unique_value}
                        for unique_value
                        in set(_type_1_duressed_unit_data['unit_id'])
                            ]),
            ]
                            ),
        dcc.Graph(
            id='graph-time-series-duress-units')
                ]
    
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
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


if __name__ == "__main__":
    app.run_server(debug=True)

# dbc.Row(dbc.Col(html.Br())),
#         dbc.Row(dbc.Col(html.H3("-"*196))),
#         dbc.Row(dbc.Col(html.H3('Data samples per categorical variable'))),
#         dbc.Row([dbc.Col(dcc.Dropdown(id='dropdown-select-a-category',
#                                     placeholder='Select category to filter on',
#                                     options=[
#                                     {'label': key, 'value': key}
#                                     for key
#                                     in samples.keys()],
#                                     value=None,
#                                     style={'width': 500})),

#                 dbc.Col(dcc.Dropdown(id='dropdown-select-a-value-within-category', 
#                                      placeholder='Select Value within category',
#                                      value = None,
#                                      multi = True,   
#                                      style={"width": 500}))]),
#         dbc.Row(dbc.Col(html.Br())),
#         dbc.Row(dbc.Col(dash_table.DataTable(
#                 id='datatable-samples',
#                 style_cell={'textAlign': 'left','width':'auto'},
#             ))),
#         dbc.Row(dbc.Col(html.Br())),
#         dbc.Row(dbc.Col(html.H3("-"*196))),
#         dbc.Row(dbc.Col(html.H1("Categorical Variable Distributions"))),
#         dbc.Row(dbc.Col([dcc.Graph(figure=graphs.get(column)) for column in graphs],
#     ))
# ])