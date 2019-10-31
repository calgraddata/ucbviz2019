import pandas as pd
from ucbviz2019.data import get_all_data, get_program_categories, get_program_options, get_program_data_as_dict


all_provided_data = get_all_data()
program_categories = get_program_categories()
program_options = get_program_options(program_categories)
program_data_as_dict = get_program_data_as_dict()

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)