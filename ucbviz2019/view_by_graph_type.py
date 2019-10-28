import dash_core_components as dcc
import dash_html_components as html


def app_view_html():
    bulk_graph_dropdown = dcc.Dropdown(
        id="bulk-graph-dropdown",
        options=[
            {"label": "Line graphs", "value": "lines"},
            {"label": "Heatmaps", "value": "heatmaps"},
            {"label": "Violin plots", "value": "violins"}
        ],
        value="lines",
    )

    bulk_graph_display = html.Div(id="bulk-graph-display")
    bulk_graph_display_loader = dcc.Loading(
        # 'graph', 'cube', 'circle', 'dot', 'default'
        type="cube",
        children=bulk_graph_display,
        className="ucbvc-fade-in"
    )
    bulk_graph_display_container = html.Div(
        bulk_graph_display_loader,
        className="ucbvc-fade-in has-margin-top-30"
    )

    title = html.Div("UC Berkeley Graduate Division Visualization",
                     className="is-size-2-desktop has-text-centered column")
    title_centered = html.Div(title, className="columns is-centered ucbvc-fade-in")

    container = html.Div(
        [
            title_centered,
            bulk_graph_dropdown,
            bulk_graph_display_container,
        ]
    )
    return container

