import dash

import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State, ClientsideFunction

from ucbviz2019.graphs.bulk import select_bulk_graphs_html
from ucbviz2019 import all_provided_data
import ucbviz2019.view_common as vc
import ucbviz2019.view_by_degree as vbd
import ucbviz2019.view_by_analysis as vba
import ucbviz2019.view_by_about as vbabout
import ucbviz2019.view_by_graph_type as vbt
from ucbviz2019.graphs.fees_stacked_bar import generate_fee_stack_plot, generate_tuition_stack_plot

external_scripts = [
    "https://code.jquery.com/jquery-3.4.1.min.js"
]

app = dash.Dash(__name__, external_scripts=external_scripts)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "UC Berkeley Graduate Data Visualization Contest"


app_container = html.Div(id="core-app-container", className="container has-margin-top-70")
location = dcc.Location(id="core-url", refresh=False)


app.layout = html.Div(
    [
        location,
        vc.nav_html(),
        app_container
    ],
    className="container"
)


################################################################################
# Common app callbacks
################################################################################
@app.callback(
    Output("core-app-container", "children"), [Input("core-url", "pathname")]
)
def display_app_html(path):
    """
    Updates which app is shown.
    """
    if str(path).strip() in ["/", "/by_degree"] or not path:
        return vbd.app_view_html()
    elif path == "/by_analysis":
        return vba.app_view_html()
    elif path == "/by_about":
        return vbabout.app_view_html()
    elif path == "/by_graph_type":
        return vbt.app_view_html()
    else:
        return vc.common_404_html()


# Animates the burger menu expansion on contraction of page
app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="animateBurgerOnClickClientsideFunction",
    ),
    Output("core-burger-trigger-cs", "value"),
    [
        Input("core-navbar-menu", "id"),
        Input("core-burger-trigger-cs", "n_clicks"),
    ],
)


################################################################################
# By analysis page
################################################################################
# Counts up each stat
app.clientside_callback(
    ClientsideFunction(
        namespace="clientside", function_name="countStatsClientsideFunction"
    ),
    Output("analysis-in-state-max-stat-cs", "children"),
    [
        Input("core-url", "pathname"),
        Input("analysis-stats-year-slider", "id"),
        Input("analysis-in-state-max-stat-cs", "id"),
        Input("analysis-out-state-max-stat-cs", "id"),
        Input("analysis-in-state-min-stat-cs", "id"),
        Input("analysis-out-state-min-stat-cs", "id"),
        Input("analysis-in-state-max-stat-hidden-ref-cs", "id"),
        Input("analysis-out-state-max-stat-hidden-ref-cs", "id"),
        Input("analysis-in-state-min-stat-hidden-ref-cs", "id"),
        Input("analysis-out-state-min-stat-hidden-ref-cs", "id"),
    ],
)

@app.callback(
    Output("analysis-stats-container", "children"),
    [
        Input("analysis-stats-year-slider", "value"),
    ]
)
def update_stats_by_year_dropdown(slider_value):
    return vba.stats_html(slider_value)

################################################################################
# By graph type view page
################################################################################
@app.callback(
    Output("bulk-graph-display", "children"),
    [Input("bulk-graph-dropdown", "value")]
)
def update_bulk_graph_display(dropdown_value):
    return select_bulk_graphs_html(all_provided_data, dropdown_value)


@app.callback(
    Output("degree_fees_plot", "children"),
    [Input("degree_program_dropdown", "value")]
)
def make_fees_plot(program):
    if program is None:
        return None
    return dcc.Graph(figure=generate_fee_stack_plot(program))

@app.callback(
    Output("degree_tuition_plot", "children"),
    [Input("degree_program_dropdown", "value")]
)
def make_fees_plot(program):
    if program is None:
        return None
    return dcc.Graph(figure=generate_tuition_stack_plot(program))