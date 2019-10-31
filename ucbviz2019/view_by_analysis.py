import dash_html_components as html
import dash_core_components as dcc

from ucbviz2019 import all_provided_data
from ucbviz2019.view_common import common_info_box_html
from ucbviz2019.graphs.analysis import all_programs_linegraph

ist = all_provided_data["total_in_state"]["df"]  # total in state tuition
ost = all_provided_data["total_out_state"]["df"]  # total out state tuition


def app_view_html():
    common_header_style = "is-size-3 has-text-weight-bold"

    # total attendance cost violin
    stats_header = html.Div("Attendance Cost Extremes by Year",
                            className=common_header_style)
    stats_year_slider = dcc.Slider(
        id="analysis-stats-year-slider",
        min=1998,
        max=2018,
        value=2015,
        step=1,
        marks={k: str(k) for k in list(range(1998, 2019, 5))},
        # tooltip="Generate stats by year"
        className="has-margin-10"
    )
    stats_container = html.Div(id="analysis-stats-container")
    stats = common_info_box_html(
        elements=[stats_header, stats_container, stats_year_slider])

    # comparison of ucb finances with total cost of attendance
    ucb_finances_header = html.Div("Attendance Cost and UC Operating Expenses", className=common_header_style)
    ucb_finances = html.Div(id="analysis-ucb-finances-container", children=dcc.Graph())
    ucb_finances_dropdown = dcc.Dropdown(
        id="analysis-ucb-finances-dropdown",
        options=[
            {"value": "in-state", "label": "In state cost of attendance"},
            {"value": "out-state", "label": "Out of state cost of attendance"}
        ],
        value="out-state",
        className="has-margin-10"
    )
    ucbf = common_info_box_html(elements=[ucb_finances_header, ucb_finances_dropdown, ucb_finances])

    # total attendance cost violin
    tacv_header = html.Div("Total Attendance Cost Distribution", className=common_header_style)
    tacv_container = html.Div(id="analysis-tacv-container", children=dcc.Graph())
    tacv_dropdown = dcc.Dropdown(
        id="analysis-tacv-dropdown",
        options=[
            {"value": "in-state", "label": "In state cost of attendance"},
            {"value": "out-state", "label": "Out of state cost of attendance"}
        ],
        value="out-state",
        className="has-margin-10"
    )
    tacv = common_info_box_html(elements=[tacv_header, tacv_dropdown, tacv_container])


    amayhm_header = html.Div("Comparing Costs with the Consumer Price Index", className=common_header_style)
    amayhm_dropdown = dcc.Dropdown(
        id="analysis-amayhm-dropdown",
        options=[
            {"value": "in-state", "label": "In state cost of attendance"},
            {"value": "out-state", "label": "Out of state cost of attendance"},
            {"value": "tuition", "label": "Base Tuition"},
            {"value": "pdst", "label": 'Professional Degree Supplement'},
            {"value": "nrst", "label": 'Non-residential Supplement'},
            {"value": "registration-student-services-fee", "label": 'Registration Services Fee'},
            {"value": "campus-fee", "label": "Campus Fee"},
            {"value": "transit-fee", "label": 'Transit Fee'},
            {"value": "health-insurance-fee", "label": "Health Insurance Fee"}
        ],
        value="out-state",
        className="has-margin-10"
    )
    amayhm_container = html.Div(id="analysis-amayhm-container", children=dcc.Graph())
    amayhm = common_info_box_html(elements=[amayhm_dropdown, amayhm_container])


    layout = html.Div(
        [
            stats,
            ucbf,
            tacv,
            amayhm
        ]
    )

    return layout


def stats_html(slider_value):
    """
    Display the fee increase as a stacked bar chart.
    Args:
        slider_value (int): the year!

    Returns:

    """
    slider_value = str(slider_value)
    max_ist = ist[slider_value].max()
    max_ist_program = ist[slider_value].idxmax()
    min_ist = ist[slider_value].min()
    min_ist_program = ist[slider_value].idxmin()
    max_ost = ost[slider_value].max()
    max_ost_program = ost[slider_value].idxmax()
    min_ost = ost[slider_value].min()
    min_ost_program = ost[slider_value].idxmin()

    max_html = tuition_stat_counters_html(
        dcc.Markdown(
            f"Highest Attendance Cost ({slider_value}): ***{max_ist_program}***",
            className="ucbvc-clicker-red"),
        "max",
        max_ist,
        max_ost,
        "ucbvc-clicker-red"
    )

    if min_ist_program == "Other Programs":
        min_ist_program = "Non-professional Programs"

    min_html = tuition_stat_counters_html(
        dcc.Markdown(
            f"Lowest Attendance Cost ({slider_value}): ***{min_ist_program}***",
            className="ucbvc-clicker-green"),
        "min",
        min_ist,
        min_ost,
        "ucbvc-clicker-green"
    )
    return html.Div([max_html, min_html])


def tuition_stat_counters_html(label, code, in_state_tuition,
                               out_state_tuition, colorclass):
    """
    Args:
        label: str or html
        in_state_tuition: float
        out_state_tuition: float

    Returns:
        html

    """
    labelmap = {
        "in-state": "In state",
        "out-state": "Out of state"
    }
    common_stat_style = "has-margin-right-10 has-margin-left-10 has-text-centered has-text-weight-bold"

    stats_columns = []
    for k, tuition in {"in-state": int(in_state_tuition),
                       "out-state": int(out_state_tuition)}.items():
        stat = html.Div(
            "${:,}".format(tuition),
            id=f"analysis-{k}-{code}-stat-cs",
            className=f"is-size-4-desktop {common_stat_style} {colorclass}",
        )

        stat_static_value = html.Div(
            tuition,
            id=f"analysis-{k}-{code}-stat-hidden-ref-cs",
            className="is-hidden",
        )

        stat_descriptor = html.Div(
            f"{labelmap[k]}",
            className=f"is-size-6-desktop has-text-centered has-margin-right-10 has-margin-left-10 {colorclass}"
        )

        stat_column = html.Div(
            [stat_descriptor, stat, stat_static_value],
            className=f"flex-column is-half has-text-centered has-margin-top-10 {colorclass}",
        )
        stats_columns.append(stat_column)

    stats_columns_html = html.Div(stats_columns,
                                  className="columns is-centered")

    stat_descriptor = html.Div(
        label, className=f"is-size-4-desktop has-text-centered"
    )
    container = html.Div([stat_descriptor, stats_columns_html],
                         className="has-margin-20")
    return container