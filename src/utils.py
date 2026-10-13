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