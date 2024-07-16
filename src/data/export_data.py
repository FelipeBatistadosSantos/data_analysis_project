import os
import pandas as pd

def save_cleaned_data(data_frame, upload_folder, filename='cleaned_data.csv'):
    """
    Salva o DataFrame limpo como um arquivo CSV.

    Args:
    data_frame (pd.DataFrame): O DataFrame que será salvo.
    upload_folder (str): O diretório onde o arquivo será salvo.
    filename (str): O nome do arquivo a ser salvo.

    Returns:
    str: O caminho completo do arquivo salvo.
    """
    cleaned_file_path = os.path.join(upload_folder, filename)
    data_frame.to_csv(cleaned_file_path, index=False)
    return cleaned_file_path
