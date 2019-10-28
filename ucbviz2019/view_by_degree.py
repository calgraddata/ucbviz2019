import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd
from ucbviz2019.constants import program_category_mappings

program_options = [{"label": key, "value": key} for key in program_category_mappings.keys()]

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})


def app_view_html():
    return html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-3"),
        html.Label("Select your degree program:"),
        dcc.Dropdown(options=program_options,
                     id='degree_program_dropdown',
                     placeholder='Program Name or Degree type (e.g. Ph.D, M.Eng., ...)'),
        dash_table.DataTable(
            id='degree_table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records')),
        html.Div(style={'padding': 10}),
        dcc.Slider(id="degree_slider",
                   marks={year: "'{}-'{}".format(str(year)[2::], str(year + 1)[2::])
                          for year in list(range(1998, 2020))},
                   value=2020,
                   min=1998,
                   max=2019),
        html.Div(style={'padding': 10}),
        html.Div(id="degree_tuition_plot", children=[]),
        html.Div(id="degree_fees_plot", children=[])
    ])
