import os

from ucbviz2019.data import get_all_data


root_dir = os.path.dirname(os.path.abspath(__file__))
assets_data_dir = os.path.join(root_dir, "assets/data")
csvs_raw_dir = os.path.join(assets_data_dir, "v1-1_csv")


this_year = "2019"

all_ucb_data = get_all_data()
