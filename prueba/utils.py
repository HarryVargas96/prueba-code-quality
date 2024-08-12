import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def read_csv_file(file_path):
    """
    Reads a CSV file from the specified absolute path and returns a DataFrame.

    Parameters:
    file_path (str): The absolute path to the CSV file.

    Returns:
    DataFrame: The DataFrame containing the data from the CSV file, or None if an error occurs.
    """
    try:
        df = pd.read_csv(file_path)
        logging.info("File read successfully!")
        return df
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None
