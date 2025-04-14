import os
import pandas as pd

def input_console():
    """
    This function gets the user input from the console

    Returns:
        str: The text entered by the user.
    """
    return input("Your input data: ")

def read_file_python(filepath):
    """
    Loads the content of a file using standard Python file operations.

    Args:
        filepath (str): The full path to the file.

    Returns:
        str: The file contents as a string, or None if the file is not found.
    """
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='UTF-8') as f:
            return f.read()
    return None

def read_file_pandas(filepath):
    """
    Loads data from a file using pandas.

    Args:
        filepath (str): The full path to the file.

    Returns:
        DataFrame: A pandas DataFrame with the file’s data, or None if the file is not found.
    """
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    return None
