import dash_html_components as html

from ucbviz2019.app import app

test_div = html.Div("Test layout text")

app.layout = html.Div(test_div)
