import os
import pandas as pd

def check_csv(filepath: str, expected_filename: str, expected_extension: str):
    """
    confirms if a given file path corresponds to the expected filename and extension.

    Parameters
    ----------
    filepath : str
        The full path to the file being validated (the actual file location).
    expected_filename : str
        The full required filename (e.g., "clean_diabetes.csv").
    expected_extension : str
        The full required file extension (e.g., ".csv").

    Raises
    ------
    AssertionError
        If the filename or extension does not match the expected values.
    """
    # Extracting the base filename
    actual_filename = os.path.basename(filepath)
    
    # Extracting the file extension (e.g., '.csv')
    actual_extension = os.path.splitext(actual_filename)[1]
    
    # Using assert for validation checks
    assert actual_filename == expected_filename, \
        f"Expected filename '{expected_filename}', but got '{actual_filename}'"
        
    assert actual_extension == expected_extension, \
        f"Expected file extension '{expected_extension}', but got '{actual_extension}'"