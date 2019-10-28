import dash_html_components as html
import dash_core_components as dcc

from ucbviz2019 import all_provided_data

ist = all_provided_data["total_in_state"]["df"]  # total in state tuition
ost = all_provided_data["total_out_state"]["df"]  # total out state tuition

def app_view_html():
    year_dropdown = dcc.Slider(
        id="analysis-stats-year-slider",
        value=2018,
        marks={k: str(k) for k in list(range(1998, 2019))},
        # tooltip="Generate stats by year"
    )

    stats_container = html.Div(id="analysis-stats-container")

    layout = html.Div(
        [
            year_dropdown,
            stats_container,
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
    print(f"SLIDER VALUE IS {slider_value}")
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
        f"Highest Tuition: {max_ist_program}",
        "max",
        max_ist,
        max_ost,
    )

    min_html = tuition_stat_counters_html(
        f"Highest Tuition: {min_ist_program}",
        "min",
        min_ist,
        min_ost,
    )
    return html.Div([max_html, min_html])


def tuition_stat_counters_html(label, code, in_state_tuition,
                               out_state_tuition):
    """
    Args:
        label: str
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
            "${:,}".format(in_state_tuition),
            id=f"analysis-{k}-{code}-stat-cs",
            className=f"is-size-4-desktop {common_stat_style}",
        )

        stat_static_value = html.Div(
            tuition,
            id=f"analysis-{k}-{code}-stat-hidden-ref-cs",
            className="is-hidden",
        )

        stat_descriptor = html.Div(
            f"{labelmap[k]}",
            className=f"is-size-6-desktop has-text-centered has-margin-right-10 has-margin-left-10"
        )

        stat_column = html.Div(
            [stat_descriptor, stat, stat_static_value],
            className="flex-column is-half has-text-centered has-margin-top-10",
        )
        stats_columns.append(stat_column)

    stats_columns_html = html.Div(stats_columns,
                                  className="columns is-centered")

    stat_descriptor = html.Div(
        f"{label}", className=f"is-size-4-desktop has-text-centered"
    )
    container = html.Div([stat_descriptor, stats_columns_html],
                         className="has-margin-20")
    return container


common_stat_style = "has-margin-right-10 has-margin-left-10 has-text-centered has-text-weight-bold"


# def generate_stats
