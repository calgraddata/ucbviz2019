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
from ucbviz2019.graphs.degree_view_helpers import generate_fee_stack_plot, \
    generate_tuition_stack_plot, plot_projection_by_program_html
from ucbviz2019.graphs.analysis import ucb_finances_vs_tuitions_html, \
    total_cost_of_attendance_violin, all_programs_linegraph
from ucbviz2019.graphs.degree_view_helpers import make_degree_info_card, \
    get_program_stats

external_scripts = [
    "https://code.jquery.com/jquery-3.4.1.min.js"
]

app = dash.Dash(__name__, external_scripts=external_scripts)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "UC Berkeley Graduate Data Visualization Contest"

app_container = html.Div(id="core-app-container",
                         className="container has-margin-top-70")
app_container_margined = html.Div(app_container, className="has-margin-20")
location = dcc.Location(id="core-url", refresh=True)

external_stylesheets = html.Link(
    href="https://fonts.googleapis.com/css?family=Cardo&display=swap",
    rel="stylesheet",
    className="is-hidden",
)

nav_container = html.Div(id="core-nav-container")

app.layout = html.Div(
    [
        external_stylesheets,
        location,
        nav_container,
        app_container_margined
    ],
    className="section"
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


@app.callback(
    Output("core-nav-container", "children"), [Input("core-url", "pathname")]
)
def update_nav_bar_highlight(path):
    return vc.nav_html(path)


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
    Output("analysis-in-state-min-stat-cs", "value"),
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


@app.callback(
    Output("analysis-ucb-finances-container", "children"),
    [Input("analysis-ucb-finances-dropdown", "value")]
)
def update_ucb_finances_vs_tuitions_plot(value):
    return ucb_finances_vs_tuitions_html(value)


@app.callback(
    Output("analysis-tacv-container", "children"),
    [Input("analysis-tacv-dropdown", "value")]
)
def update_tacv_plot(value):
    return total_cost_of_attendance_violin(value)


@app.callback(
    Output("analysis-cpi-container", "children"),
    [Input("analysis-cpi-dropdown", "value")]
)
def update_cpi_plot(value):
    return all_programs_linegraph(value)


################################################################################
# By graph type view page
################################################################################
@app.callback(
    Output("bulk-graph-display", "children"),
    [Input("bulk-graph-dropdown", "value")]
)
def update_bulk_graph_display(dropdown_value):
    return select_bulk_graphs_html(all_provided_data, dropdown_value)


################################################################################
# By degree
################################################################################

@app.callback(
    Output("degree-card-container", "children"),
    [Input("degree-program-dropdown", "value")]
)
def update_degree_card(program):
    return make_degree_info_card(program)


@app.callback(
    Output("degree-card-stats", "children"),
    [Input("degree-card-slider", "value")],
    [State("degree-program-dropdown", "value")]
)
def update_degree_card(year, program):
    return get_program_stats(program, year)


@app.callback(
    Output("degree-fees-plot", "children"),
    [Input("degree-program-dropdown", "value")]
)
def make_fees_plot(program):
    if program is None:
        return None
    return dcc.Graph(figure=generate_fee_stack_plot(program))


@app.callback(
    Output("degree-tuition-plot", "children"),
    [Input("degree-program-dropdown", "value")]
)
def make_tuition_plot(program):
    if program is None:
        return None
    return dcc.Graph(figure=generate_tuition_stack_plot(program))


app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="countPerDegreeStatsClientsideFunction"
    ),
    Output("degree-total-out-state-cs", "value"),
    [
        Input("core-url", "pathname"),
        Input("degree-total-in-state-cs", "id"),
        Input("degree-other-misc-fees-cs", "id"),
        Input("degree-total-out-state-cs", "id"),
        Input("degree-student-services-fee-cs", "id"),
        Input("degree-campus-fee-cs", "id"),
        Input("degree-base-tuition-cs", "id"),
        Input("degree-nrst-cs", "id"),
        Input("degree-transit-fee-cs", "id"),
        Input("degree-pdst-cs", "id"),
        Input("degree-health-insurance-fee-cs", "id"),

        Input("degree-total-in-state-hidden-ref-cs", "id"),
        Input("degree-other-misc-fees-hidden-ref-cs", "id"),
        Input("degree-total-out-state-hidden-ref-cs", "id"),
        Input("degree-student-services-fee-hidden-ref-cs", "id"),
        Input("degree-campus-fee-hidden-ref-cs", "id"),
        Input("degree-base-tuition-hidden-ref-cs", "id"),
        Input("degree-nrst-hidden-ref-cs", "id"),
        Input("degree-transit-fee-hidden-ref-cs", "id"),
        Input("degree-pdst-hidden-ref-cs", "id"),
        Input("degree-health-insurance-fee-hidden-ref-cs", "id"),
    ],
)


@app.callback(
    Output("degree-info-card-year", "children"),
    [
        Input("degree-card-slider", "value"),
    ]
)
def update_degree_card_year_from_slider(year):
    return year


@app.callback(
    Output("degree-fees-projection", "children"),
    [
        Input("degree-program-dropdown", "value"),
    ]
)
def update_predictions_plot(program):
    return plot_projection_by_program_html(program)