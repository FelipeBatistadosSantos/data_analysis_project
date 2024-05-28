import pandas as pd

def import_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        return f"O arquivo {file_path} não foi encontrado"
    except pd.errors.ParserError:
        return f"O arquivo {file_path} não pode ser analisado como CSV"
    except Exception as e:
        return f"Erro desconhecido: {e}"