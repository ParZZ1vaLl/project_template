def output_console(text):
    """
    Displays the given text in the console.

    Args:
        text (str): The string to be printed.
    """
    print(text)

def write_file_python(filepath, text):
    """
    Saves text to a file using standard Python file I/O.

    Args:
        filepath (str): The destination file path.
        text (str): The content to be written into the file.
    """
    with open(filepath, 'a', encoding='UTF-8') as f:
        f.write(text)
        f.write('\n')

def write_file_pandas(filepath, df):
    """
    Exports a DataFrame to a file using pandas utilities.

    Args:
        filepath (str): The destination file path.
        df (DataFrame): The pandas DataFrame to save.
    """
    df.to_csv(filepath)
