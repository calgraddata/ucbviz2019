import dash_html_components as html
import dash_core_components as dcc
from ucbviz2019.data import get_program_options


def app_view_html():
    return [html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-3"),
        html.Div(id="degree_card_container"),
        # html.Div(style={'padding': 10}),
        html.Label("Find your degree program:"),
        dcc.Dropdown(options=get_program_options(),
                     id='degree_program_dropdown',
                     value="Law (J.D., LL.M., J.S.D.)",
                     placeholder='Start typing program name or degree type (e.g. Ph.D, M.Eng., ...)'),
        html.Div(style={'padding': 10}),
        html.Div(id="degree_tuition_plot", children=[]),
        html.Div(id="degree_fees_plot", children=[])
    ])]


