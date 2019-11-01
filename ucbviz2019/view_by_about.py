import dash_html_components as html


def app_view_html():
    title = html.P("About this website",
           className="is-size-2 has-text-weight-bold")
    explanation = html.P(
        "This is where the links should go. as part of the Graduate Assembly's Data Visualization Contest.",
        className="is-size-6")
    return html.Div([title, explanation], className="ucbvc-fade-in")