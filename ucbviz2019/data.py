import os

import pandas as pd

from ucbviz2019.constants import csvs_raw_dir


def get_all_data(data_dir=csvs_raw_dir):
    """
    Get all the data in one load function.

    Args:
        data_dir (str): The fully specified path of the data dir containing
            the file.

    Returns:
        ({str: dict}): String keys are the names of the datasets without the
            .csv ending. for example, "tuition", not "tuition.csv".
            Values are dicts with the format:
                key "info": value (str): The dataset's info.
                key "df": value (pd.DataFrame): The dataset as a dataframe.
    """
    fnames = get_all_filenames(data_dir, include_cpi=True)
    fnames_no_dotcsv = [f.replace(".csv", "") for f in fnames]
    data = {k: None for k in fnames_no_dotcsv}
    for i, f in enumerate(fnames):
        df, info = load_df_and_info(f)
        fname_key = fnames_no_dotcsv[i]
        data[fname_key] = {"info": info, "df": df}
    return data


def get_all_filenames(data_dir=csvs_raw_dir, include_cpi=True):
    """
    Get all the filenames for the data.

    Most of the files are of the form Programs (rows) x Years (columns) for
    various financial metrics.

    Args:
        data_dir (str): The fully specified path of the data dir containing
            the file.
        include_cpi (bool): Include the pdst_cpi.csv file, which is different
            in format from the rest of the files.

    Returns:
        ([str]): A list of the string filenames.
    """
    fnames = os.listdir(data_dir)
    valid_fnames = []
    for f in fnames:
        if ".csv" in f:
            if include_cpi:
                valid_fnames.append(f)
            else:
                if f != "pdst_cpi.csv":
                    valid_fnames.append(f)
    return valid_fnames


def load_df_and_info(
        fname, data_dir=csvs_raw_dir, remove_blank=True, drop_nan_years=True,
        drop_nan_ix=True,
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

    for c in df.columns:
        df[c] = df[c].astype(str)
        df[c] = df[c].str.replace("$", "")
        df[c] = df[c].str.replace(",", "")
        df[c] = df[c].str.replace("%", "")
        df[c] = df[c].astype(float)

    return df, info


if __name__ == "__main__":
    # for fname in os.listdir(csvs_raw_dir):
    #     if ".csv" in fname:
    #         df, info = load_df_and_info(fname, csvs_raw_dir)
    #         print(fname)
    #         # print(df.shape)
    #         # print("\n")
    #         print(info)
    #         print(df)
    #         print("\n\n\n")

    yes_cpi = get_all_filenames(include_cpi=True)
    no_cpi = get_all_filenames(include_cpi=False)

    print(f"Including cpi: {yes_cpi}")
    print(f"No cpi {no_cpi}")
