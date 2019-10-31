from ucbviz2019.data import load_df_and_info
import plotly.graph_objects as go
from ucbviz2019.view_common import common_info_box_html, \
    common_info_box_wide_html
from ucbviz2019.data import get_program_data_as_dict, get_program_categories
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

fees = ['registration_student_services_fee.csv',
        'health_insurance_fee.csv',
        'campus_fee.csv',
        'transit_fee.csv',
        'other_misc_fees.csv']

tuition = ['tuition.csv',
           'nrst.csv',
           'pdst.csv']

data_labels = {'health_insurance_fee.csv': 'Health Insurance Fee',
               'registration_student_services_fee.csv': 'Student Services Fee',
               'transit_fee.csv': 'Transit Fee', 'campus_fee.csv': 'Campus Fee',
               'other_misc_fees.csv': 'Other Misc. Fees',
               'tuition.csv': 'Base Tuition',
               'nrst.csv': 'Non-Resident Supplemental Tuition',
               'pdst.csv': 'Professional Degree Supplemental Tuition',
               'total_out_state.csv': 'Total (Out of State)',
               'total_in_state.csv': 'Total (In State)'
               }

program_category_mappings = get_program_categories()


def generate_fee_stack_plot(program="Other Programs"):
    """
    Generates a stacked bar chart for the specified program.

    Args:
        program: (str) Name of program or program category

    Returns:
        plotly graph object.

    """
    program_label = program
    if program in program_category_mappings:
        program = program_category_mappings[program]
    data = []
    for fee in fees:
        df, dsc = load_df_and_info(fee)
        df = df.loc[:,
             ("2019" > df.columns.values) & ("1998" <= df.columns.values)]
        data.append(go.Bar(name=data_labels[fee], x=df.loc[program].keys(),
                           y=df.loc[program],
                           hovertemplate="%{x}: $%{y}/semester "))
    fig = go.Figure(data=data)
    fig.update_layout(
        legend_orientation="h",
        legend=dict(x=0, y=1.11),
        title=go.layout.Title(
            text="Fees for {}".format(program_label),
            x=0.5,
            y=0.9),
        xaxis=dict(
            title=go.layout.xaxis.Title(text="Academic Year (Starting In)"),
            tickmode='array',
            tickvals=[year for year in df.loc[program].keys() if year < "2019"],
            # ticktext=["{}-{}".format(year, str(int(year) + 1)) for year in df.loc[program].keys()]
        ),
        yaxis=dict(
            title=go.layout.yaxis.Title(text="Total ($)")
        ))
    fig.update_layout(barmode='stack', font=dict(family="Condo"))
    return fig


def generate_tuition_stack_plot(program="Other Programs"):
    """
    Generates a stacked bar chart for the specified program.

    Args:
        program: (str) Name of program or program category

    Returns:
        plotly graph object.

    """
    program_label = program
    if program in program_category_mappings:
        program = program_category_mappings[program]
    data = []
    for fee in tuition:
        df, dsc = load_df_and_info(fee)
        df = df.loc[:,
             ("2019" > df.columns.values) & ("1998" <= df.columns.values)]
        if program in df.index:
            data.append(go.Bar(name=data_labels[fee], x=df.loc[program].keys(),
                               y=df.loc[program],
                               hovertemplate="%{x}: $%{y}/semester "))
            years = df.loc[program].keys()
    fig = go.Figure(data=data)
    fig.update_layout(
        barmode='stack',
        legend_orientation="h",
        legend=dict(x=0, y=1.11),
        title=go.layout.Title(
            text="Tuition for {}".format(program_label),
            x=0.5,
            y=0.9),
        xaxis=dict(
            title=go.layout.xaxis.Title(text="Academic Year (Starting In)"),
            tickmode='array',
            tickvals=[year for year in years if year < "2019"],
            # ticktext=["{}-{}".format(year, str(int(year) + 1)) for year in years]
        ),
        yaxis=dict(
            title=go.layout.yaxis.Title(text="Total ($)")
        ))
    return fig


common_header_style = "is-size-3 has-text-weight-bold"


def get_program_stats(program, year):
    if program in program_category_mappings:
        program = program_category_mappings[program]
    program_stats = get_program_data_as_dict()[program][str(year)]
    program_stats = {data_labels[key + ".csv"]: program_stats[key] for key in
                     program_stats}

    callback_container_mapping = {
        "Total (In State)": "total-in-state",
        "Other Misc. Fees": "other-misc-fees",
        "Total (Out of State)": "total-out-state",
        "Student Services Fee": "student-services-fee",
        "Campus Fee": "campus-fee",
        "Base Tuition": "base-tuition",
        "Non-Resident Supplemental Tuition": "nrst",
        "Transit Fee": "transit-fee",
        "Health Insurance Fee": "health-insurance-fee",
        "Professional Degree Supplemental Tuition": "pdst"
    }

    common_classname = "is-size-5-desktop has-text-bold has-text-centered ucbvc-clicker-blue"

    divs = {}
    divs_is_empty = {}
    for stat, value in program_stats.items():
        animated_id = f"degree-{callback_container_mapping[stat]}-cs"
        hidden_id = f"degree-{callback_container_mapping[stat]}-hidden-ref-cs"

        try:
            value = int(value)
        except:
            # make an invisible placeholder to make sure nothing breaks!
            animated_container = html.Div(id=animated_id, children="99999", className="is-hidden")
            hidden_ref = html.Div(id=hidden_id, children="99999", className="is-hidden")
            divs[stat] = html.Div([hidden_ref, animated_container])
            divs_is_empty[stat] = True
            continue

        label = html.Div(stat, className="is-size-5 has-text-centered ucbvc-clicker-blue")
        animated_container = html.Div(
            children="${:,}".format(value),
            id=animated_id,
            className=common_classname
        )
        hidden_ref = html.Div(
            children=int(value),
            id=hidden_id,
            className="is-hidden"
        )
        this_stat_div = html.Div([label, animated_container, hidden_ref], className="ucbvc-clicker-blue")
        divs[stat] = this_stat_div
        divs_is_empty[stat] = False

    first_column = ["Total (In State)", "Total (Out of State)", "Base Tuition"]
    second_column = ["Non-Resident Supplemental Tuition", "Professional Degree Supplemental Tuition", "Student Services Fee", "Campus Fee"]
    third_column = ["Health Insurance Fee", "Transit Fee", "Other Misc. Fees"]

    columns = []
    common_subcard_style = "column is-one-third box has-margin-5"
    for column_set in [first_column, second_column, third_column]:
        if all([divs_is_empty[k] for k in column_set]):
            no_data_text = html.Div("No data available.", className="is-size-5-desktop has-text-bold has-text-centered ucbvc-clicker-red")
            column = html.Div(no_data_text, className=common_subcard_style)
        else:
            column = html.Div([divs[k] for k in column_set], className=common_subcard_style)
        columns.append(column)

    container = html.Div(columns, className="columns")
    return container


def make_degree_info_card(program):
    if program is None:
        return None
    program_label = program
    if program in program_category_mappings:
        program = program_category_mappings[program]
    program_data = get_program_data_as_dict()[program]
    years = [int(year) for year in program_data.keys()]

    card_title = html.Div(f"Overview of attendance costs",
                          className=common_header_style)
    card_sublabel = html.Div(program_label, className="is-size-3")
    card_year = html.Div(children="", id="degree-info-card-year", className="is-size-4")
    program_stats_for_year = html.Div(id='degree_card_stats')

    minimum_year = max(min(years), 1998)
    maximum_year = min(max(years), 2018)
    initial_value = min(max(years), 2018)
    program_year_slider = dcc.Slider(
        id="degree_card_slider",
        min=minimum_year,
        max=maximum_year,
        value=initial_value,
        step=1,
        marks={k: str(k) for k in range(minimum_year, maximum_year + 1, 5)},
        className="has-margin-10"
    )
    return common_info_box_wide_html(elements=[card_title,
                                               card_sublabel,
                                               card_year,
                                               program_stats_for_year,
                                               program_year_slider])


if __name__ == '__main__':
    fig = generate_fee_stack_plot('Other Programs')
    fig.show()
