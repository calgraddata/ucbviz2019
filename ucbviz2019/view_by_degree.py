import dash_html_components as html
import dash_core_components as dcc
from ucbviz2019.constants import program_category_mappings

program_options = [{"label": key, "value": key} for key in program_category_mappings.keys()]


def app_view_html():
    return html.Div([
        html.P("Explore Cost of Attendance by Program",
               className="is-size-3"),
        html.Label("Select your degree program:"),
        dcc.Dropdown(options=program_options,
                     id='degree_program_dropdown',
                     placeholder='Program Name or Degree type (e.g. Ph.D, M.Eng., ...)'),
        html.Table(id='degree_table'),
        dcc.Slider(id="degree_slider",
                   marks={year: "{}-{}".format(year, str(int(year) + 1))
                          for year in list(range(1998, 2020))},
                   value=2019),
        html.Div(id="degree_fees_plot", children=[])
    ])
