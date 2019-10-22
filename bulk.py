"""
Functions for generating bulk (multiple) graphs for prototyping etc.
"""
import dash_html_components as html

from ucbviz2019.graphs import get_generic_line_graph_html


def generate_bulk_graphs(data, graph_function):
    graphs = []
    for ds_name, ds in data.items():
        info = ds["info"]
        df = ds["df"]

        if ds_name != "pdst_cpi":
            lg = graph_function(df)
            lg_label = html.Div(ds_name, className="is-size-4")
            lg_info = html.Div(info, className="is-size-7")
            lg_container = html.Div([lg_label, lg_info, lg], className="container")
            graphs.append(lg_container)