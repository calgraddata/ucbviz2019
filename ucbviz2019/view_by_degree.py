import dash_html_components as html
import dash_core_components as dcc
from ucbviz2019.data import get_program_options


def app_view_html():
    return [html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-3"),
        # html.Div(style={'padding': 10}),
        html.Label("Find your degree program:"),
        dcc.Dropdown(options=get_program_options(),
                     id='degree-program-dropdown',
                     value="Law (J.D., LL.M., J.S.D.)",
                     placeholder='Start typing program name or degree type (e.g. Ph.D, M.Eng., ...)'),
        html.Div(id="degree-card-container"),
        # html.Div(style={'padding': 10}),
        html.Div(id="degree-tuition-plot", children=[]),
        html.Div(id="degree-fees-plot", children=[])
    ])]


