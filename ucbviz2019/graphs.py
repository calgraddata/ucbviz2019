import dash_core_components as dcc

from ucbviz2019.data import load_df_and_info


def get_generic_line_graph_html(fname):
    df, info = load_df_and_info(fname)

    # 'name': 'Trace 1',
    # 'mode': 'markers',
    # 'marker': {'size': 12}

    marker = {"size": 15}

    data = []
    df = df.T
    for program in df.columns:
        program_data = df[program]
        data.append({"x": program_data.index, "y": program_data.values, "name": program, "mode": "lines+markers", "marker": marker})

    layout = {
        "clickmode": "event+select",
        "hovermode": "x+y"
    }

    plot = dcc.Graph(
        id="in_state_tuition_line",
        figure={"data": data, "layout": layout}
    )

    return plot



if __name__ == "__main__":
    get_generic_line_graph_html()