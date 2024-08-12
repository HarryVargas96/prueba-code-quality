from utils import read_csv_file
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Print the current working directory
current_directory = os.getcwd()
logging.info(f"Current working directory: {current_directory}")

file_path = "/home/hvarga/prueba/data/raw/train.csv"

df = read_csv_file(file_path)
if df is not None:
    print(df.head())