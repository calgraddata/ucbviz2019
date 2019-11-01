import dash_html_components as html
import dash_core_components as dcc

def app_view_html():

    common_header_style = "is-size-3 has-margin-10 has-margin-top-30"
    common_txt_style = "is-size-5 has-margin-10"

    title = html.P("About CalGradData",
           className="is-size-2 has-text-weight-bold")

    explanation = dcc.Markdown(
        "This website is an entry to the **2019 UC Berkeley Graduate Assembly Data Visualization Contest.** Our goal for CalGradData is to provide clear and engaging content for visualizing graduate and professional school financial data. Thanks again for visiting!",
        className=common_txt_style
    )


    about_the_entrants = html.Div("About the entrants", className=common_header_style)
    about_the_entrants_txt = dcc.Markdown(
        "Hi there! We are [Alex Dunn](https://alexdunn.io) and [John Dagdelen](https://www.linkedin.com/in/johndagdelen/), both 3rd Year Materials Science and Engineering Ph.D. Students at UC Berkeley. We hope you enjoy this website's visualizations. If you have any questions or concerns (especially about usage), please contact us through a [Github issue](https://github.com/calgraddata/ucbviz2019).",
        className=common_txt_style
    )

    data = html.Div("Data", className=common_header_style)
    data_txt = dcc.Markdown(
        "All data except where explicitly noted is adapted from the Graduate Assembly graduate financial dataset released October 7, 2019.",
        className=common_txt_style
    )

    code = html.Div("Code", className=common_header_style)
    code_txt = dcc.Markdown(
        "The code for running this website is open source and can be found on [Github](https://github.com/calgraddata/ucbviz2019).",
        className=common_txt_style
    )

    licence = html.Div("License", className=common_header_style)
    license_txt = dcc.Markdown(
        "The code and all visualizations of this website are under the Creative Commons CC-BY-NC license version 4.0. View the license [here](https://github.com/calgraddata/ucbviz2019/blob/master/LICENSE).",
        className=common_txt_style
    )




    return html.Div(
        [
            title,
            explanation,
            about_the_entrants,
            about_the_entrants_txt,
            data,
            data_txt,
            code,
            code_txt,
            licence,
            license_txt
        ],
        className="container ucbvc-fade-in")