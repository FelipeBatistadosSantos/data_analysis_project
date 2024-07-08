import pandas as pd
import os

def export_data(df, file_name, output_dir='../exports'):
    """
    Exporta o DataFrame para um arquivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a ser exportado.
        file_name (str): Nome do arquivo CSV de saída.
        output_dir (str): Diretório onde o arquivo CSV será salvo.

    Returns:
        str: Caminho completo do arquivo CSV exportado.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, file_name)
    df.to_csv(output_path, index=False)
    return output_path
