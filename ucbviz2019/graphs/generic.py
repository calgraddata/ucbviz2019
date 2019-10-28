import dash_core_components as dcc
import plotly.graph_objects as go

def get_generic_line_graph_html(df):
    data = []
    df = df.T
    for program in df.columns:
        program_data = df[program]
        data.append(
            {"x": program_data.index, "y": program_data.values, "name": program,
             "mode": "lines+markers", "marker": {"size": 15}, "opacity": 0.3})

    layout = {
        "clickmode": "event+select",
        "hovermode": "x+y",
        "xaxis": {"title": "Year"},
        "yaxis": {"title": "Dollars"}
    }

    plot = dcc.Graph(
        figure={"data": data, "layout": layout}
    )

    return plot


def get_generic_heatmap_html(df):
    data = [
        go.Heatmap(
            x=df.columns,
            y=df.index,
            z=df.values
        )
    ]

    layout = {
        "hovermode": "z",
    }
    plot = dcc.Graph(
        figure={"data": data, "layout": layout}
    )
    return plot


def get_generic_violin_html(df):
    fig = go.Figure()
    for year in df.columns:
        fig.add_trace(
            go.Violin(
                x=[year]*df.shape[0],
                y=df[year],
                box_visible=True,
                meanline_visible=True,
                points="all",
                name=year,
                text=df.index,
                hoverinfo="text+y+name"
            )
        )
    fig.update_layout(showlegend=True)
    plot = dcc.Graph(figure=fig)
    return plot
