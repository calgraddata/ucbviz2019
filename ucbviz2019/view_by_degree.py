import dash_html_components as html
import dash_core_components as dcc
from ucbviz2019.data import get_program_options
from ucbviz2019.view_common import wrap_in_loader_html

def app_view_html():
    # degree_card_wrapper = wrap_in_loader_html(html.Div(id="degree-card-container"))
    degree_card_wrapper = html.Div(id="degree-card-container")
    tuition_plot_wrapper = wrap_in_loader_html(html.Div(id="degree-tuition-plot", children=[]))
    fees_plot_wrapper = wrap_in_loader_html(html.Div(id="degree-fees-plot", children=[]))
    return [html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-3"),
        # html.Div(style={'padding': 10}),
        html.Label("Find your degree program:"),
        dcc.Dropdown(options=get_program_options(),
                     id='degree-program-dropdown',
                     value="Law (J.D., LL.M., J.S.D.)",
                     placeholder='Start typing program name or degree type (e.g. Ph.D, M.Eng., ...)'),
        degree_card_wrapper,
        # html.Div(style={'padding': 10}),
        tuition_plot_wrapper,
        fees_plot_wrapper
    ])]


