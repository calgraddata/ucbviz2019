import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ucbviz2019.data import load_auxiliary_df


from ucbviz2019 import all_provided_data

ist = all_provided_data["total_in_state"]["df"]  # total in state tuition
ost = all_provided_data["total_out_state"]["df"]  # total out state tuition


def total_cost_of_attendance_violin(mode):
    """
    Generate a total cost of attendance violin plot.

    Args:
        mode: (str): In state or out of state

    Returns:
        plot

    """
    if mode == "in-state":
        df = ist
    elif mode == "out-state":
        df = ost
    else:
        raise ValueError(f"Invalid mode: {mode} for total cost of attendance violin!")

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


def ucb_finances_vs_tuitions_html(mode):
    """
    Get a graph of ucb finances and total cost of attendance

    Args:
        mode: (str): In state or out of state

    Returns:
        plot

    """
    years = list(range(1998, 2018))
    min_ist = []
    min_ist_program = []
    max_ist = []
    max_ist_program = []
    min_ost = []
    min_ost_program = []
    max_ost = []
    max_ost_program = []
    for year in years:
        y = str(year)
        max_ist.append(ist[y].max())
        max_ist_program.append(ist[y].idxmax())
        min_ist.append(ist[y].min())
        min_ist_program.append(ist[y].idxmin())
        max_ost.append(ost[y].max())
        max_ost_program.append(ost[y].idxmax())
        min_ost.append(ost[y].min())
        min_ost_program.append(ost[y].idxmin())

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    if mode == 'in-state':
        y_high = max_ist
        y_low = min_ist
        hover_high = max_ist_program
        hover_low = min_ist_program
        caption = "In"
    elif mode == 'out-state':
        y_high = max_ost
        y_low = min_ost
        hover_high = max_ost_program
        hover_low = min_ost_program
        caption = "Out of"
    else:
        raise ValueError(f"Invalid selection for mode: {mode}.")

    fig.add_trace(
        go.Scatter(
            x=years,
            y=y_high,
            name=f"Max {caption} State Expenses",
            mode="lines+markers",
            hovertext=hover_high,
            marker_color="orange",
        ),
        secondary_y=False
    )
    fig.add_trace(
        go.Scatter(
            x=years,
            y=y_low,
            name=f"Min {caption} State Expenses",
            mode="lines+markers",
            hovertext=hover_low,
            fill="tonexty",
            fillcolor='rgba(226, 151, 0, 0.15)'
        ),
        secondary_y=False
    )

    df_expenses = load_auxiliary_df(
        "expenses_by_function_dollars_in_thousands_by_fiscal_year.csv")
    df_revenues = load_auxiliary_df(
        "revenues_dollars_in_thousands_by_fiscal_year.csv")

    # df_expenses = load_auxiliary_df("expenses_by_function_inflation_adjusted_dollars_in_thousands_by_fiscal_year.csv")
    # df_revenues = load_auxiliary_df("revenues_inflation_adjusted_dollars_in_thousands_by_fiscal_year.csv")

    expenses_billions = df_expenses.loc["Grand Total"].values
    exp_years = [c.split("-")[0] for c in df_expenses.columns]
    revenues_billions = df_revenues.loc["Grand Total"].values
    rev_years = [c.split("-")[0] for c in df_revenues.columns]

    fig.add_trace(
        go.Scatter(x=exp_years, y=expenses_billions,
                   name="UC Berkeley Expenses (Grand Total)",
                   marker_color="green"),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(x=rev_years, y=revenues_billions,
                   name="UC Berkeley Revenue (Grand Total)",
                   marker_color="blue"),
        secondary_y=True,
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Year")

    # Set y-axes titles
    fig.update_yaxes(title_text="Cost of Attendance <b>($)</b>",
                     secondary_y=False)
    fig.update_yaxes(title_text="UC Expenses/Revenue <b>(billion $)</b>",
                     secondary_y=True)

    # layout = {
    #     "clickmode": "event+select",
    #     "hovermode": "x",
    #     "xaxis": {"title": "Year"},
    #     "yaxis": {"title": "Dollars"}
    # }
    # fig.update_layout(**layout)

    fig.update_layout(legend=dict(x=-.1, y=1.5))

    plot = dcc.Graph(
        figure=fig
    )
    return plot