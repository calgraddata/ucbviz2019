import pandas as pd
from ucbviz2019.data import get_all_data


all_provided_data = get_all_data()

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)