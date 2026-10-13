from pandas import DataFrame, read_csv
from pathlib import Path
from os import getcwd



def load_csv_as_dataframe(file_name: str) -> DataFrame:
    """Loads a CSV file into a pandas DataFrame from designated directories.

    The function searches for the file in the 'data/raw/' directory first. 
    If not found, it checks the parent root directory.

    Args:
        file_name: The name of the CSV file to load (including extension).

    Returns:
        DataFrame: The loaded pandas DataFrame.

    Raises:
       TypeError: If `file_name` is not a string.
        ValueError: If `file_name` does not end with a '.csv' extension.
        FileNotFoundError: If the file cannot be found in 'data/raw/' or root.

    Example:
        >>> load_csv_as_dataframe("example.csv")
        ... col1  col2  col3
        ...  0     1     2
    """

    if not isinstance(file_name, str):
        raise TypeError(f"The file path must be a string. Got type {type(file_name).__name__}")

    if not file_name.endswith(".csv"):
        raise ValueError("The file is not a csv file. Check extenstion and try again")

    parent           = Path(getcwd()).parent
    source_file_path = Path(parent / "data" / "raw" / f"{file_name}")

    if source_file_path.exists():
        return read_csv(source_file_path)

    file_path = Path(parent / f"{file_name}")

    if not file_path.exists():
        raise FileNotFoundError(f"The csv file {file_name} couldn't be located in the parent folder ({parent}) or in the /data/raw/ folder")
    
    return read_csv(file_path)



def validate_dataframe(df: DataFrame) -> None:
    if not isinstance(df, DataFrame):
        raise TypeError(
                f"df is not an instance of DataFrame. Got type {type(df).__name__}"
            )



def get_entire_row(df: DataFrame, column_name: str, min_row=True) -> DataFrame:
    """
    Takes a DataFrame and a column name and returns the entire row
    containing the minimum value in that column if the `min_row` is
    set to True else returns the maximum value in that colum

    Args:
        df (DataFrame): The DataFrame containing the data.
        column_name (str): The name of the column to search.
        min_row : bool: Defaults to True, returns the minimum value for that
                    row. if set to False returns the maximun value in that row

    Raises:
        TypeError:
            If df is not a DataFrame.
            If column_name is not a string.

    Example:
        >>> get_entire_row(df, "Age")
    """

    validate_dataframe(df)

    if not isinstance(column_name, str):
        raise TypeError(
            f"Column name is not a string. "
            f"Expected a string, got type {type(column_name).__name__}"
        )

    if not isinstance(min_row, bool):
        raise TypeError(
            f"The min_row parameter is not a bool. Got type {type(min_row).__name__}"
        )

    if min_row:
        return df.loc[[df[column_name].idxmin()]]
    return df.loc[[df[column_name].idxmax()]]