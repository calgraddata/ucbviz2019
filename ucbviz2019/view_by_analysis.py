import dash_html_components as html
import dash_core_components as dcc

from ucbviz2019 import all_provided_data
from ucbviz2019.view_common import wrap_in_loader_html, common_info_box_html, common_header_style, common_explanation_style

ist = all_provided_data["total_in_state"]["df"]  # total in state tuition
ost = all_provided_data["total_out_state"]["df"]  # total out state tuition


def app_view_html():
    title = html.P("The Broader View - Trends in Graduate Fees",
           className="is-size-2 has-text-weight-bold")
    explanation = html.P(
        "Looking at individual programs tells us about the minutia of fees and "
        "tuitions, but fails to show overall trends on an institutional level. "
        "What can we learn from looking at the Graduate Financial data from a "
        "broader view? Let's take a deeper look into the data as a whole.",
           className="is-size-5"
    )

    # total attendance cost violin
    stats_header = html.Div("Most and Least Expensive Programs",
                            className=common_header_style)
    stats_explanation = html.Div("Whether you've just won the lottery or are shopping for education on a budget, looking at the most and least expensive graduate programs at UC Berkeley is interesting. The Haas Business School and Berkeley Law are almost always the most expensive, while Academic programs (Ph.D., etc.) are the cheapest.",
                                 className=common_explanation_style)
    stats_explanation2 = html.Div("Slide the slider to change the year!",
                                className="is-size-7 has-text-weight-bold has-margin-top-30")

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
    stats_container = html.Div(id="analysis-stats-container", className="ucbvc-fade-in")
    stats = common_info_box_html(
        elements=[stats_header, stats_explanation, stats_container, stats_year_slider, stats_explanation2])

    # total attendance cost violin
    tacv_header = html.Div("Total Attendance Cost Distribution", className=common_header_style)
    tacv_explanation = html.Div("Here we graph the distributions of Total Cost of Attendance (COA) for years 1998-2018. These distributions show us how the cost spread of graduate school at UC Berkeley has changed over 20 years! The split view (orange and blue) shows comparisons of the in and out of state COA. While it's apparent the mean COAs increase yearly, it is remarkable that the spread of costs is growing yearly as well. ",
                                className=common_explanation_style)

    tacv_explanation2 = html.Div("These are known as 'split' violin plots. Hover over them to reveal their data points and distributional data, or narrow the data selection with the selection bar above. ",
                                className="is-size-7 has-text-weight-bold")

    tacv_container = html.Div(id="analysis-tacv-container", children=dcc.Graph())
    tacv_dropdown = dcc.Dropdown(
        id="analysis-tacv-dropdown",
        options=[
            {"value": "in-state", "label": "In state cost of attendance"},
            {"value": "out-state", "label": "Out of state cost of attendance"},
            {"value": "both",  "label": "In state and Out of state (side by side)"}
        ],
        value="both",
        className="has-margin-10"
    )
    tacv_explanation3 = html.Div("Select a total cost of attendance with the dropdown:",
                                className="is-size-7 has-text-weight-bold has-margin-10 has-margin-top-30")
    tacv = common_info_box_html(elements=[tacv_header, tacv_explanation, tacv_explanation3, tacv_dropdown, tacv_container, tacv_explanation2])


    combined_header = html.Div("Comparing with External Sources", className=common_header_style)
    combined_explanation = html.Div("We've seen how the price of going to graduate or professional school at UC Berkeley has changed over the years, but how does this measure up with external factors? More importantly, we will see how the relative cost of UC Berkeley graduate school is changing for both students (via the consumer price index) and the school as a whole (via the school's gross revenues and expenses).", className=common_explanation_style)


    common_subheader_style = "is-size-5 has-margin-10 has-text-weight-bold has-margin-top-30"
    cpi_header = html.Div("The Consumer Price Index", className=common_subheader_style)
    cpi_explanation = dcc.Markdown("The [Consumer Price Index](https://www.bls.gov/cpi/) is a measure of how expensive common goods and services are for the 'average' buyer. This is a plot of all program's total costs of attendance vs. the increase in consumer price index. While the CPI experienced a ~50% increase since 2000, higher cost programs at UC Berkeley have increased the total cost of attendance by 100-200%. For smaller fees like the Campus Fee, the fee increase is much larger, near 500%. Thus the 'buying power' of the UC Berkeley Graduate or Professional student has drastically fallen since the mid 2000s.",
                                   className=common_explanation_style)

    cpi_dropdown = dcc.Dropdown(
        id="analysis-cpi-dropdown",
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
    cpi_container = html.Div(id="analysis-cpi-container", children=dcc.Graph())
    cpi_explanation2 = html.Div("Select a fee to compare to the CPI; hover over points to highlight program:",
                                className="is-size-7 has-text-weight-bold has-margin-10 has-margin-top-30")
    cpi = html.Div([cpi_header, cpi_explanation, cpi_explanation2, cpi_dropdown, cpi_container, ])

    # comparison of ucb finances with total cost of attendance
    ucb_finances_header = html.Div("Attendance Cost and UC Operating Expenses",
                                   className=common_subheader_style)
    ucb_finances_explanation = dcc.Markdown(
        "It can also be interesting to compare the student costs to the costs and revenues of UC Berkeley itself. This plot shows the range - the maximum and minimum total costs of attendance - for all graduate and professional programs compared with UC Berkeley's gross cash flows. Note that UC Berkeley's cash flows contain much more than Graduate Student tuitions and fees, such as undergraduate fees and expenses. All UC Berkeley Revenue and Expense Data was downloaded from the official [University of California Infocenter.](https://www.universityofcalifornia.edu/infocenter/revenue-and-expense-data)",
        className=common_explanation_style)
    ucb_finances = html.Div(id="analysis-ucb-finances-container", children=[])
    ucb_finances_dropdown = dcc.Dropdown(
        id="analysis-ucb-finances-dropdown",
        options=[
            {"value": "in-state", "label": "In state cost of attendance"},
            {"value": "out-state", "label": "Out of state cost of attendance"}
        ],
        value="out-state",
        className="has-margin-10"
    )

    ucb_explanation2 = html.Div("Select a range to compare with Cal's gross cash flows; hover over points for numbers:",
                                className="is-size-7 has-text-weight-bold has-margin-10 has-margin-top-30")

    ucbf = html.Div([
            ucb_finances_header,
            ucb_finances_explanation,
        ucb_explanation2,
        ucb_finances_dropdown,
            ucb_finances
        ]
    )

    external_comparisons = common_info_box_html(elements=[combined_header, combined_explanation, cpi, ucbf])


    layout = html.Div(
        [
            title,
            explanation,
            tacv,
            stats,
            external_comparisons
        ],
        className="ucbvc-fade-in"
    )

    return wrap_in_loader_html(layout)


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