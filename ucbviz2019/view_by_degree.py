import dash_html_components as html
import dash_core_components as dcc
from ucbviz2019 import program_options
from ucbviz2019.view_common import wrap_in_loader_html, common_info_box_html, common_header_style, \
    common_explanation_style


def app_view_html():
    # degree_card_wrapper = wrap_in_loader_html(html.Div(id="degree-card-container"))
    degree_card_wrapper = html.Div(id="degree-card-container", className="ucbvc-fade-in")

    coa_header = html.Div("Total Cost of Attendance", className=common_header_style)
    coa_explanation = html.Div(
        "The total cost of attending a graduate program is made up of both "
        "tuition and fees paid to the University. The costs of grad"
        "programs at UC Berkeley have steadily risen - on average - since 1998.",
        className=common_explanation_style
    )
    tuition_plot_header = html.Div("UC Tuition Costs", className=common_header_style)
    tuition_plot = html.Div(id="degree-tuition-plot", children=[])
    tuition_explanation2 = html.Div(
        "Hover over the points on the plot for more info or select/deselect "
        "series by touching/tapping on their label in the legend!",
        className="is-size-7 has-text-weight-bold has-margin-10")

    fees_plot_header = html.Div("Assorted UC Fees", className=common_header_style)
    fees_plot_explanation = html.Div(
        "UC Berkeley's graduate fees, including Health, Transit, Registration, "
        "Student services, and other miscellaneous fees generally increase "
        "beginning in 1998, with some discontinuities in the mid-2000s.",
        className=common_explanation_style
    )
    fees_plot = html.Div(id="degree-fees-plot", children=[])
    fees_explanation2 = html.Div(
        "Hover over the points on the plot for more info or select/deselect "
        "series by touching/tapping on their label in the legend!",
        className="is-size-7 has-text-weight-bold has-margin-10")

    common_subheader_style = "is-size-5 has-margin-10 has-text-weight-bold has-margin-top-30"
    projection_plot_header = html.Div("Projections for Total Cost of Attendance", className=common_subheader_style)
    projection_plot_explanation = html.Div(
        "In this plot we show predictions for future total cost of attendance "
        "based on trends observed over the last 20 years. "
        "These projections are made using scheduled tuition/fee data and/or simple "
        "quadratic and linear regressions on the individual fees contributing to "
        "the total costs of attendance (such as registration fee, base tuition, "
        "non-resident tuition supplement,etc) where future cost information is not "
        "available. We use linear regressions for newer degrees (<10 years of data) and "
        "quadratic regressions otherwise.",
        className=common_explanation_style
    )
    projection_plot = html.Div(
        [
            html.Div(id="degree-fees-projection", children=[])
        ]
    )

    all_plots = html.Div(
        [
            coa_header,
            coa_explanation,
            projection_plot_header,
            projection_plot_explanation,
            tuition_explanation2,
            projection_plot,
            tuition_plot_header,
            fees_explanation2,
            tuition_plot,
            fees_plot_header,
            fees_plot_explanation,
            fees_explanation2,
            fees_plot,
        ],
        className="ucbvc-fade-in"
    )
    all_plots_container = common_info_box_html(all_plots)

    find_your_degree = html.Div("Find your degree program:", className="is-size-3 has-text-weight-bold")
    find_your_degree_container = html.Div(find_your_degree, className="has-margin-top-20")

    return [html.Div([
        html.P("Graduate Programs: Cost of Attendance",
               className="is-size-2 has-text-weight-bold"),
        dcc.Markdown(
            "Welcome to Cal Grad Data, an **interactive visualization** of "
            "UC Berkeley Graduate Cost of Attendance data (as part of the "
            "[Graduate Assembly](http://ga.berkeley.edu) data visualization contest). "
            "On this page you can explore historical degree program data and "
            "**visualize tuition and fee data** for most Cal graduate "
            "and professional programs over the time period between 1998-2018. "
            "Enter your program of interest in the searchable dropdown below "
            "to start visualizing!",
            className="is-size-5"
        ),
        dcc.Markdown(
            "If you are interested in visualizations showing general trends in the"
            "cost of attending grad school at UC Berkeley, **check "
            "out the [trends](/by_analysis) page.**",
            className="is-size-6 has-margin-top-20"
        ),
        # html.Div(style={'padding': 10}),
        find_your_degree_container,
        dcc.Dropdown(options=program_options,
                     id='degree-program-dropdown',
                     value="Mechanical Engineering (M.S., Ph.D.)",
                     placeholder='Start typing program name or degree type (e.g. Ph.D, M.Eng., ...)',
                     clearable=False,
                     optionHeight=25,
                     className="has-text-size-3"
                     ),
        degree_card_wrapper,
        wrap_in_loader_html(all_plots_container),
    ],
        className="ucbvc-fade-in")]
