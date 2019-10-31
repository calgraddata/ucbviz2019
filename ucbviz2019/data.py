import os
import pandas as pd
import numpy as np
from ucbviz2019.constants import csvs_raw_dir, auxiliary_data_dir


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


def load_auxiliary_df(fname, data_dir=auxiliary_data_dir):
    """
    Load an auxiliary data file.

    If the auxiliary data file is financial data from UCB, loads all numbers
    as integers, in BILLIONS

    Args:
        fname (str): The filename
        data_dir (str): The auxiliary data directory.

    Returns:
        pd.Dataframe

    """
    test_fname_full = os.path.join(data_dir, fname)
    if fname != "ucb_programs.csv":
        df = pd.read_csv(test_fname_full, header=1, index_col=0)
        df.columns = [convert_janky_year_to_readable(c) for c in df.columns]
        for c in df.columns:
            df[c] = df[c].astype(str)
            df[c] = df[c].str.replace("$", "")
            df[c] = df[c].str.replace(",", "")
            df[c] = df[c].str.replace("%", "")
            df[c] = df[c].astype(float) * 1000/1e9
    else:
        df = pd.read_csv(test_fname_full)
    return df


def convert_janky_year_to_readable(janky_fiscal_year):
    """
    Convert the janky csv formatitng caused by Excel to readable dataframe
    formats by fiscal year. Only applicable to some auxiliary data files.

    Args:
        janky_fiscal_year (str): The column name in the form "3-4" meaning
            2003-2004.

    Returns:
        (str): the corrected column name, e.g., "3-4" --> "2003-2004"

    """
    years = janky_fiscal_year.split("-")
    year1 = years[0]
    year2 = years[1]
    first_year = "200" + year1 if int(year1) < 10 else "20" + year1
    second_year = "200" + year2 if int(year2) < 10 else "20" + year2
    label = f"{first_year}-{second_year}"
    return label


def get_program_categories():
    """
    Get the program categories

    """
    _df_by_program = load_auxiliary_df("ucb_programs.csv")
    programs = list(_df_by_program['Graduate Programs'])
    degrees = list(_df_by_program['Degrees'])
    degrees = ['M.S., Ph.D.' if degree == 'Ph.D., M.S./Ph.D., M.S.' else degree
               for degree in degrees]
    categories = list(_df_by_program['Category Key'])

    program_category_mappings = {}
    for i in range(len(programs)):
        program_category_mappings["{} ({})".format(programs[i], degrees[i])] = \
        categories[i]
    return program_category_mappings


def get_program_options():
    """
    Get the program options

    Returns:

    """
    program_category_mappings = get_program_categories()
    program_options = [{"label": key, "value": key} for key in
                       program_category_mappings.keys()]
    return program_options


def get_program_data_as_dict():
    data = get_all_data()
    full_data = {}
    for key in data:
        df = data[key]['df']
        for program in df.index:
            for year in df.loc[program].index:
                val = df.loc[program].loc[year]
                if np.isnan(val):
                    val = "Data not available."
                if program not in full_data:
                    full_data[program] = {year: {key: val}}
                elif year not in full_data[program]:
                    full_data[program].update({year: {key: val}})
                elif key not in full_data[program][year]:
                    full_data[program][year].update({key: val})
                else:
                    full_data[program][year][key] = val
    return full_data

if __name__ == "__main__":
    print(load_auxiliary_df("revenues_inflation_adjusted_dollars_in_thousands_by_fiscal_year.csv"))