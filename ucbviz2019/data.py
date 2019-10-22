import os

import pandas as pd

from ucbviz2019.constants import csvs_raw_dir


def load_df_and_info(
        fname, data_dir=csvs_raw_dir, remove_blank=True, drop_nan_years=True,
        drop_nan_ix=True
):
    """
    Load a dataframe and info of ucb data from the refactored filename.

    Args:
        fname (str): The name of the file in the directory.
        data_dir (str): The fully specified path of the data dir containing
            the file.
        remove_blank (bool): If True, removes the random [blank] row in the
            data
        drop_nan_years (bool): If True, removes the year columns with
            all nan values (i.e., no values have been recorded/expected).
        drop_nan_ix (bool): If True, removes rows with nan index (e.g.,
            info-only rows).

    Returns:
        ((pd.DataFrame, str)): A pandas dataframe containing the data and a
            string describing what the data is.

    """
    test_fname_full = os.path.join(data_dir, fname)

    with open(test_fname_full, "r") as f:
        df_name = f.readlines()[0].replace(",", "'").replace("\'", "").strip()

    df = pd.read_csv(test_fname_full, header=1, index_col=0)
    info = df_name

    if remove_blank:
        blank_key = "[blank]"
        if blank_key in df.index:
            df = df.drop(blank_key, axis=0)

    if drop_nan_years:
        na_cols = df.columns[df.isna().all()]
        df = df.drop(columns=na_cols)

    if drop_nan_ix:
        df = df.loc[df.index.dropna()]

    return df, info


if __name__ == "__main__":
    for fname in os.listdir(csvs_raw_dir):
        if ".csv" in fname:
            df, info = load_df_and_info(fname, csvs_raw_dir)
            print(fname)
            # print(df.shape)
            # print("\n")
            print(info)
            print(df)
            print("\n\n\n")
