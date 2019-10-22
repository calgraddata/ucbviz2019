import dash_html_components as html

from ucbviz2019.app import app
from ucbviz2019.graphs import get_generic_line_graph_html

test_div = html.Div("Test layout text")


line_graphs =
tist = get_generic_line_graph_html()

app.layout = html.Div([test_div, tist])
