import dash_html_components as html


def app_view_html():
    layout = html.Div(
        [stats_html()]
    )

    return layout


def stats_html():
    """
    Display the fee increase as a stacked bar chart.
    Returns:

    """
    stats = []
    tuition_stats = [
        ["Average tuition", "avg", 99999, 111111],
        ["Highest tuition", "high", 222222, 333333],
        ["Lowest tuition", "low", 10000, 15000],
    ]
    for t in tuition_stats:
        stats.append(tuition_stat_counters(*t))
    return html.Div(stats)


def tuition_stat_counters(label, code, in_state_tuition, out_state_tuition):
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
    for k, tuition in {"in-state": in_state_tuition,
                       "out-state": out_state_tuition}.items():
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
            f"{labelmap[k]}", className=f"is-size-6-desktop has-text-centered"
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
    container = html.Div([stat_descriptor, stats_columns_html], className="has-margin-20")
    return container



common_stat_style = "has-margin-right-10 has-margin-left-10 has-text-centered has-text-weight-bold"