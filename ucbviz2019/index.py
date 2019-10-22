import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from ucbviz2019.app import app
from ucbviz2019.bulk import select_bulk_graphs_html
from ucbviz2019.data import get_all_data

# don't load csvs more than once
all_ucb_data = get_all_data()

bulk_graph_dropdown = dcc.Dropdown(
    id="bulk_graph_dropdown",
    options=[
        {"label": "Line graphs", "value": "lines"},
        {"label": "Heatmaps", "value": "heatmaps"}
    ],
    value="lines",
)

bulk_graph_display = html.Div(id="bulk_graph_display")


logo = html.Img(src="/assets/graduate_division_logo.png", className="column")
logo_centered = html.Div(logo, className="columns is-centered ucbvc-fade-in")


app.layout = html.Div(
    [
        logo_centered,
        bulk_graph_dropdown,
        bulk_graph_display
    ],
)


@app.callback(
    Output("bulk_graph_display", "children"),
    [Input("bulk_graph_dropdown", "value")]
)
def update_bulk_graph_display(dropdown_value):
    return select_bulk_graphs_html(all_ucb_data, dropdown_value)