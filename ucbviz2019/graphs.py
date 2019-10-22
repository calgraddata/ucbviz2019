import dash_core_components as dcc

from ucbviz2019.data import load_df_and_info


def get_total_in_state_tuition_graph_html():
    df, info = load_df_and_info("total_in_state.csv")

    df_by_program = df.T
    df =
    print(df)


if __name__ == "__main__":
    get_total_in_state_tuition_graph_html()