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
    except:
        logging.error(f"File not found: {file_path}")
        return None
    
def process_and_save_as_parquet(df, output_parquet_path):
    """
    Processes the DataFrame by renaming columns and converting specified columns to categories,
    then saves the resulting DataFrame as a Parquet file.

    Parameters:
    df (DataFrame): The input DataFrame to process.
    output_parquet_path (str): The file path where the output Parquet file will be saved.

    Returns:
    DataFrame: The processed DataFrame.
    """
    # Drop a column
    df = df.drop(columns = ['ID'])
    # Define column names
    nombres = [
        'edad', 'trabajo', 'estado_civil', 'educacion', 'mora', 'vivienda', 
        'consumo', 'contacto', 'mes', 'dia', 'campana', 'dias_ultima_camp', 
        'no_contactos', 'resultado_anterior', 'emp_var_rate', 'cons_price_idx', 
        'cons_conf_idx', 'euriobor3m', 'nr_employed', 'y'
    ]
    
    # Rename the columns
    df.columns = nombres
    
    # Convert specified columns to categories
    categorical_columns = [
        'trabajo', 'estado_civil', 'educacion', 'mora', 'vivienda', 
        'consumo', 'contacto', 'mes', 'dia', 'resultado_anterior'
    ]
    df = df.astype(dtype={col: 'category' for col in categorical_columns})
    
    # Save the DataFrame as a Parquet file
    df.to_parquet(output_parquet_path, index=False)
    logging.info(f"Preprocessed data saved to {output_parquet_path} successfully.")
    
    # Return the processed DataFrame
    return df