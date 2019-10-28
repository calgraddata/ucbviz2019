import os
from pandas import read_csv

root_dir = os.path.dirname(os.path.abspath(__file__))
assets_data_dir = os.path.join(root_dir, "assets/data")
csvs_raw_dir = os.path.join(assets_data_dir, "v1-1_csv")
auxiliary_data_dir = os.path.join(assets_data_dir, "aux")

program_categories = ['Other Programs', 'Optometry (OD)', 'Law (JD)', 'Business (MBA FT)',
                      'UCB-UCSF Medical (MS/MD)', 'Public Health (MPH, Dr.PH )',
                      'Public Policy (MPP)', 'Engineering (M.Eng.)',
                      'CED (M.Arch., MCP., MLA, and MUD)', 'Social Welfare (MSW)',
                      'Information (MIMS)', 'Chemistry (MS Chem Eng)', 'Stats (MA)',
                      'Development Practice (MDP)', 'UCB-UCSF Medical (MTM)',
                      'Education (Ed. Leadership, Teacher Ed. , Principal Leadership MA)',
                      'Journalism (MJ)', 'CEE (MS)']

this_year = "2019"

df = read_csv("ucbviz2019/assets/data/aux/ucb_programs.csv")
programs = list(df['Graduate Programs'])
degrees = list(df['Degrees'])
degrees = ['M.S., Ph.D.' if degree == 'Ph.D., M.S./Ph.D., M.S.' else degree for degree in degrees]
categories = list(df['Category Key'])

program_category_mappings = {}
for i in range(len(programs)):
    program_category_mappings["{} ({})".format(programs[i], degrees[i])] = categories[i]
