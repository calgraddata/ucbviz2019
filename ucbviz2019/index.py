import dash_html_components as html

from ucbviz2019.app import app
from ucbviz2019.data import get_all_data
from ucbviz2019.graphs import get_generic_line_graph_html

test_div = html.Div("Test layout text")

# only get program/year formatted files
data = get_all_data()

line_graphs = [None] * len(list(data.keys()))

for ds_name, ds in data.items():
    info = ds["info"]
    df = ds["info"]
    tist = get_generic_line_graph_html(df)

app.layout = html.Div([test_div, tist])
