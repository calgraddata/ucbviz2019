import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from ucbviz2019.app import app
from ucbviz2019.constants import all_ucb_data

test_div = html.Div("Test layout text")

bulk_graph_dropdown = dcc.Dropdown(
    id="bulk_graph_dropdown",
    options=[
        {"label": "Line graphs"},
        {"label": "Heatmaps"}
    ]
)

bulk_graph_display = html.Div(id="bulk_graph_display")


app.layout = html.Div([test_div] + line_graphs, className="section")


@app.callback(
    Output

)