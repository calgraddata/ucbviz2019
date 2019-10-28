import os
from ucbviz2019.data import load_auxiliary_df

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

_df_by_program = load_auxiliary_df("ucb_programs.csv")
programs = list(_df_by_program['Graduate Programs'])
degrees = list(_df_by_program['Degrees'])
degrees = ['M.S., Ph.D.' if degree == 'Ph.D., M.S./Ph.D., M.S.' else degree for degree in degrees]
categories = list(_df_by_program['Category Key'])

program_category_mappings = {}
for i in range(len(programs)):
    program_category_mappings["{} ({})".format(programs[i], degrees[i])] = categories[i]