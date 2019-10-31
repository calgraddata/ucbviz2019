import dash_html_components as html


def app_view_html():
    title = html.P("About this website",
           className="is-size-1 has-text-weight-bold")
    explanation = html.P(
        "This is where the links should go. Anyway, Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        className="is-size-6")
    return html.Div([title, explanation])