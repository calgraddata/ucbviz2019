import dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from ucbviz2019.graphs.bulk import select_bulk_graphs_html
from ucbviz2019.data import get_all_data
from ucbviz2019.view_common import nav_html

app = dash.Dash(__name__)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "UC Berkeley Graduate Data Visualization Contest"

# don't load csvs more than once
all_ucb_data = get_all_data()

bulk_graph_dropdown = dcc.Dropdown(
    id="bulk_graph_dropdown",
    options=[
        {"label": "Line graphs", "value": "lines"},
        {"label": "Heatmaps", "value": "heatmaps"},
        {"label": "Violin plots", "value": "violins"}
    ],
    value="lines",
)

bulk_graph_display = html.Div(id="bulk_graph_display")
bulk_graph_display_loader = dcc.Loading(
# 'graph', 'cube', 'circle', 'dot', 'default'
    type="cube",
    children=bulk_graph_display,
    className="ucbvc-fade-in"
)
bulk_graph_display_container = html.Div(
    bulk_graph_display_loader,
    className="ucbvc-fade-in has-margin-top-30"
)


title = html.Div("UC Berkeley Graduate Division Visualization", className="is-size-2-desktop has-text-centered column")
title_centered = html.Div(title, className="columns is-centered ucbvc-fade-in")
nav = nav_html()


app.layout = html.Div(
    [
        nav_html(),
        title_centered,
        bulk_graph_dropdown,
        bulk_graph_display_container
    ],
    className="container"
)


@app.callback(
    Output("bulk_graph_display", "children"),
    [Input("bulk_graph_dropdown", "value")]
)
def update_bulk_graph_display(dropdown_value):
    return select_bulk_graphs_html(all_ucb_data, dropdown_value)



@app.callback(
    Output("core-app-container", "children"), [Input("core-url", "pathname")]
)
def display_app_html(path):
    """
    Updates which app is shown.

    Args:
        path (str): The path the browser is currently showing. For example,
            "/search".

    Returns:
        (dash_html_components.Div): The app being shown, or a 404.
    """
    if str(path).strip() in ["/", "/search"] or not path:
        return sv.app_view_html()
    elif path == "/degrees":
        return av.app_view_html()
    elif path == "/analysis":
        return bv.app_view_html()
    elif path == "/":
        return jv.app_view_html()
    else:
        return common_404_html()