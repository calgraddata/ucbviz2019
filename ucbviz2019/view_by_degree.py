import dash_html_components as html
import dash_core_components as dcc
from ucbviz2019 import program_options
from ucbviz2019.view_common import wrap_in_loader_html, common_info_box_html, common_header_style, common_explanation_style


def app_view_html():
    # degree_card_wrapper = wrap_in_loader_html(html.Div(id="degree-card-container"))
    degree_card_wrapper = html.Div(id="degree-card-container", className="ucbvc-fade-in")

    tuition_plot_header = html.Div("UC Tuition Costs", className=common_header_style)
    tuition_plot_explanation = html.Div(
        "The accumulated tuition fees for UC Berkeley have steadily risen - "
        "on average -  since 1998.",
        className=common_explanation_style
    )
    tuition_plot = html.Div(id="degree-tuition-plot", children=[])
    tuition_explanation2 = html.Div("Hover over the points on the plot for more info!",
                                className="is-size-7 has-text-weight-bold has-margin-10")


    fees_plot_header = html.Div("Assorted UC Fees", className=common_header_style)
    fees_plot_explanation = html.Div(
        "UC Berkeley's graduate fees, including Health, Transit, Registration, "
        "Student services, and other miscellaneous fees generally increase "
        "beginning in 1998, with some discontinuities in the mid-2000s.",
        className=common_explanation_style
    )
    fees_plot = html.Div(id="degree-fees-plot", children=[])
    fees_explanation2 = html.Div("Hover over the bars on the plot for more info!",
                                className="is-size-7 has-text-weight-bold has-margin-10")

    projection_plot_header = html.Div("Projection of Total Attendance Cost", className=common_header_style)
    projection_plot_explanation = html.Div(
        "The total cost of attendance can be predicted using basic regressions on "
        "each contributing fee. These projections are made using simple quadratic and linear regressions on the fees contributing to the total costs of attendance (such as registration fee, base tuition, non-resident tuition, and professional supplemental tuition)."
        " View the projections below.",
        className=common_explanation_style
    )
    projection_plot = html.Div(
        [
            html.Div(id="degree-fees-projection", children=[])
        ]
    )

    all_plots = html.Div(
        [
            tuition_plot_header,
            tuition_plot_explanation,
            fees_explanation2,
            tuition_plot,
            fees_plot_header,
            fees_plot_explanation,
            fees_explanation2,
            fees_plot,
            projection_plot_header,
            projection_plot_explanation,
            tuition_explanation2,
            projection_plot
        ],
        className="ucbvc-fade-in"
    )
    all_plots_container = common_info_box_html(all_plots)

    find_your_degree = html.Div("Find your degree program:", className="is-size-3 has-text-weight-bold")
    find_your_degree_container = html.Div(find_your_degree, className="has-margin-top-20")

    return [html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-2 has-text-weight-bold"),
        dcc.Markdown(
        "Welcome to CalGradData, an **interactive visualization** of UC Berkeley Graduate Cost of Attendance data (as part of the [Graduate Assembly](http://ga.berkeley.edu) data visualization contest)! This is the By Degree page, where you can **visualize individual fees and tuition** for most Cal graduate and professional degree programs for years 1998-2018. So simply enter your program of interest and start visualizing!",
        className="is-size-5"
    ),
        dcc.Markdown(
            "If you are interested in visualizing data *outside* of a single major, **check out the [trends](/by_analysis) page.**",
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
