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


    fees_plot_header = html.Div("Assorted UC Fees", className=common_header_style)
    fees_plot_explanation = html.Div(
        "UC Berkeley's graduate fees, including Health, Transit, Registration, "
        "Student services, and other miscellaneous fees generally increase "
        "beginning in 1998, with some discontinuities in the mid-2000s.",
        className=common_explanation_style
    )
    fees_plot = html.Div(id="degree-fees-plot", children=[])

    projection_plot_header = html.Div("Projection of Total Attendance Cost", className=common_header_style)
    projection_plot_explanation = html.Div(
        "The total cost of attendance can be predicted using regressions on "
        "each contributing fee. View the projections for total cost of in-state "
        "and out-of-state attendance costs below.",
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
            tuition_plot,
            fees_plot_header,
            fees_plot_explanation,
            fees_plot,
            projection_plot_header,
            projection_plot_explanation,
            projection_plot
        ],
        className="ucbvc-fade-in"
    )
    all_plots_container = common_info_box_html(all_plots)

    find_your_degree = html.Div("Find your degree program:", className="is-size-4 has-text-weight-bold")
    find_your_degree_container = html.Div(find_your_degree, className="has-margin-top-20")

    return [html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-1 has-text-weight-bold"),
        html.P(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        className="is-size-6"
    ),
        # html.Div(style={'padding': 10}),
        find_your_degree_container,
        dcc.Dropdown(options=program_options,
                     id='degree-program-dropdown',
                     value="Mechanical Engineering (M.S., Ph.D.)",
                     placeholder='Start typing program name or degree type (e.g. Ph.D, M.Eng., ...)',
                     clearable=True,
                     optionHeight=25,
                     className="has-text-size-3"
                     ),
        degree_card_wrapper,
        wrap_in_loader_html(all_plots_container),
    ],
    className="ucbvc-fade-in")]
