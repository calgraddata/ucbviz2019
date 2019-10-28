import dash_html_components as html
import dash_core_components as dcc

from ucbviz2019 import all_provided_data
from ucbviz2019.view_common import common_info_box_html

ist = all_provided_data["total_in_state"]["df"]  # total in state tuition
ost = all_provided_data["total_out_state"]["df"]  # total out state tuition

def app_view_html():

    stats_header = html.Div("Attendance Cost Extremes by Year", className="is-size-3 has-text-weight-bold")
    stats_year_dropdown = dcc.Slider(
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
    stats = common_info_box_html(elements=[stats_header, stats_container, stats_year_dropdown])

    ucb_finances_header = html.Div("Attendance Cost and UC Operating Expenses")
    ucb_finances = ucb_finances_vs_tuitions_html()
    ucbf = common_info_box_html(elements=[ucb_finances_header, ucb_finances])


    layout = html.Div(
        [
            stats,
            ucbf
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
        dcc.Markdown(f"Highest Attendance Cost ({slider_value}): ***{max_ist_program}***", className="ucbvc-clicker-red"),
        "max",
        max_ist,
        max_ost,
        "ucbvc-clicker-red"
    )

    if min_ist_program=="Other Programs":
        min_ist_program = "Non-professional Programs"

    min_html = tuition_stat_counters_html(
        dcc.Markdown(f"Lowest Attendance Cost ({slider_value}): ***{min_ist_program}***", className="ucbvc-clicker-green"),
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


common_stat_style = "has-margin-right-10 has-margin-left-10 has-text-centered has-text-weight-bold"



import plotly.graph_objects as go

def ucb_finances_vs_tuitions_html():

    years = list(range(1998, 2018))
    min_ist = []
    min_ist_program = []
    max_ist = []
    max_ist_program = []
    min_ost = []
    min_ost_program = []
    max_ost = []
    max_ost_program = []
    for year in years:
        y = str(year)
        max_ist.append(ist[y].max())
        max_ist_program.append(ist[y].idxmax())
        min_ist.append(ist[y].min())
        min_ist_program.append(ist[y].idxmin())
        max_ost.append(ost[y].max())
        max_ost_program.append(ost[y].idxmax())
        min_ost.append(ost[y].min())
        min_ost_program.append(ost[y].idxmin())

    data = []
    data.append(
        {"x": years, "y": max_ist, "name": "Max In State Expenses", "hovertext": max_ist_program, "title": "TEST",
         "mode": "lines+markers", "marker": {"size": 15}, "opacity": 0.3, "color": "blue"})
    data.append(
        {"x": years, "y": min_ist, "hovertext": min_ist_program, "name": "Min In State Expenses",
         "mode": "lines+markers", "marker": {"size": 15}, "opacity": 0.3, "color": "turqouise"})
    data.append(
        {"x": years, "y": max_ost, "hovertext": max_ost_program, "name": "Max Out of State Expenses",
         "mode": "lines+markers", "marker": {"size": 15}, "opacity": 0.3})
    data.append(
        {"x": years, "y": min_ost, "hovertext": min_ost_program, "name": "Min Out of State Expenses",
         "mode": "lines+markers", "marker": {"size": 15}, "opacity": 0.3})

    layout = {
        "clickmode": "event+select",
        "hovermode": "x+y",
        "xaxis": {"title": "Year"},
        "yaxis": {"title": "Dollars"}
    }

    plot = dcc.Graph(
        figure={"data": data, "layout": layout}
    )
    return plot
