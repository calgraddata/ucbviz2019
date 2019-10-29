from ucbviz2019.data import load_df_and_info
import plotly.graph_objects as go
from ucbviz2019.view_common import common_info_box_html, common_info_box_wide_html
from ucbviz2019.data import get_program_data_as_dict, get_program_categories
import dash_core_components as dcc
import dash_html_components as html


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
        df = df.loc[:, ("2019" > df.columns.values) & ("1998" <= df.columns.values)]
        data.append(go.Bar(name=data_labels[fee], x=df.loc[program].keys(), y=df.loc[program],
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
    fig.update_layout(barmode='stack')
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
        df = df.loc[:, ("2019" > df.columns.values) & ("1998" <= df.columns.values)]
        if program in df.index:
            data.append(go.Bar(name=data_labels[fee], x=df.loc[program].keys(), y=df.loc[program],
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
    program_label = program
    if program in program_category_mappings:
        program = program_category_mappings[program]
    program_stats = get_program_data_as_dict()[program][year]
    program_stats = {data_labels[key]: program_stats[key] for key in program_stats}

    ## CODE TO GENERATE CARD HERE

    return html.Div()


def make_degree_info_card(program):
    if program is None:
        return None
    program_label = program
    if program in program_category_mappings:
        program = program_category_mappings[program]
    program_data = get_program_data_as_dict()[program]
    years = [int(year) for year in program_data.keys()]

    card_title = html.Div(f"Attendance Costs for {program_label}",
                          className=common_header_style)
    program_stats_for_year = html.Div()
    program_year_slider = dcc.Slider(
        id="degree-stats-year-slider",
        min=min(min(years), 1998),
        max=min(max(years), 2018),
        value=min(max(years), 2018),
        step=1,
        marks={k: str(k) for k in years},
        # tooltip="Generate stats by year"
        className="has-margin-10"
    )
    return common_info_box_wide_html(elements=[card_title,
                                          program_stats_for_year,
                                          program_year_slider])


if __name__ == '__main__':
    fig = generate_fee_stack_plot('Other Programs')
    fig.show()
