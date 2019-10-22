import os

import pandas as pd

from ucbviz2019.constants import csvs_raw_dir


def load_df(fname, data_dir=csvs_raw_dir):
    """
    Load a dataframe of ucb data from the refactored filename.

    Args:
        fname (str): The name of the file in the directory.
        data_dir (str): The fully specified path of the data dir containing
            the file.

    Returns:
        (pd.DataFrame): A pandas dataframe containing the data.

    """
    test_fname_full = os.path.join(data_dir, fname)
    df = pd.read_csv(test_fname_full, header=1, index_col=0)
    return df


if __name__ == "__main__":
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    for fname in os.listdir(csvs_raw_dir):
        df = load_df(fname, csvs_raw_dir)
        print(fname)
        print(df)
        print("\n\n\n")
