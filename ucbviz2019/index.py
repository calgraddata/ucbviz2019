import os

import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import send_from_directory

from ucbviz2019.app import app

bulma = html.Link(rel='stylesheet', href='/static/css/bulma.css')
bulma_helper = html.Link(rel='stylesheet', href='/static/css/bulma-helpers.css')
# stylesheets = [bulma, bulma_helper]
custom_css = html.Link(rel='stylesheet', href='/static/css/custom.css')
stylesheets = [bulma, bulma_helper, custom_css]
stylesheet_div = html.Div(stylesheets, className="container is-hidden")


test = html.Div("Test text")
app.layout = html.Div(test)