import dash_html_components as html

from ucbviz2019.app import app
from ucbviz2019.data import get_all_filenames
from ucbviz2019.graphs import get_generic_line_graph_html

test_div = html.Div("Test layout text")

# only get program/year formatted files
fnames = get_all_filenames(include_cpi=False)
line_graphs = [None] * len(fnames)
for i, f in enumerate(fnames):
    tist = get_generic_line_graph_html(fname)

app.layout = html.Div([test_div, tist])
