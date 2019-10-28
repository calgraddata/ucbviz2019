from ucbviz2019.data import load_df_and_info
import plotly.graph_objects as go
from ucbviz2019.constants import program_category_mappings, program_categories

fees = ['registration_student_services_fee.csv',
        'health_insurance_fee.csv',
        'campus_fee.csv',
        'transit_fee.csv',
        'other_misc_fees.csv']

fee_labels = {'health_insurance_fee.csv': 'Health Insurance Fee',
              'registration_student_services_fee.csv': 'Student Services Fee',
              'transit_fee.csv': 'Transit Fee', 'campus_fee.csv': 'Campus Fee',
              'other_misc_fees.csv': 'Other Misc. Fees'}


def generate_fee_stack_plot(program="Other Programs"):
    """
    Generates a stacked bar chart for the specified program.

    Args:
        program: (str) Name of program or program category

    Returns:
        plotly graph object.

    """

    if program in program_category_mappings:
        program = program_category_mappings[program]
    data = []
    for fee in fees:
        df, dsc = load_df_and_info(fee)
        data.append(go.Bar(name=fee_labels[fee], x=df.loc[program].keys(), y=df.loc[program],
                           hovertemplate="%{x}: $%{y}/semester "))
    fig = go.Figure(data=data)
    fig.update_layout(
        title=go.layout.Title(
            text="Fees for {}".format(program),
            x=0.4,
            y=0.87),
        xaxis=dict(
            title=go.layout.xaxis.Title(text="Academic Year"),
            tickmode='array',
            tickvals=df.loc[program].keys(),
            ticktext=["{}-{}".format(year, str(int(year) + 1)) for year in df.loc[program].keys()]),
        yaxis=dict(
            title=go.layout.yaxis.Title(text="Total ($)")
        ))
    fig.update_layout(barmode='stack')
    return fig


if __name__ == '__main__':
    fig = generate_fee_stack_plot('Other Programs')
    fig.show()