import dash_core_components as dcc


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
    }

    plot = dcc.Graph(
        # id=id,
        figure={"data": data, "layout": layout}
    )

    return plot


if __name__ == "__main__":
    get_generic_line_graph_html()
