import dash_html_components as html

from ucbviz2019.app import app
from ucbviz2019.data import get_all_data
from ucbviz2019.graphs import get_generic_line_graph_html

test_div = html.Div("Test layout text")

# only get program/year formatted files
data = get_all_data()

line_graphs = []

for ds_name, ds in data.items():
    info = ds["info"]
    df = ds["df"]

    if ds_name != "pdst_cpi":
        lg = get_generic_line_graph_html(df)
        lg_label = html.Div(ds_name, className="is-size-4")
        lg_info = html.Div(info, className="is-size-7")
        lg_container = html.Div([lg_label, lg_info, lg], className="container")
        line_graphs.append(lg_container)

app.layout = html.Div([test_div] + line_graphs, className="section")
