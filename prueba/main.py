from utils import read_csv_file, process_and_save_as_parquet
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

logging.info(f"Data shape {df.shape}")

interim_data_path = "/ho/hvarga/prueba/data/interim/train.parquet"
df = process_and_save_as_parquet(df = df,output_parquet_path=interim_data_path)

