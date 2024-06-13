import pandas as pd

def import_csv(file_path):
    try:
        # Tente ler o arquivo CSV
        print(f"Tentando ler o arquivo CSV em: {file_path}")
        df = pd.read_csv(file_path, delimiter=';')
        print("Arquivo CSV lido com sucesso!")
        return df
    except FileNotFoundError:
        error_message = f"O arquivo {file_path} não foi encontrado"
        print(error_message)
        return error_message
    except pd.errors.ParserError:
        error_message = f"O arquivo {file_path} não pode ser analisado como CSV"
        print(error_message)
        return error_message
    except Exception as e:
        error_message = f"Erro desconhecido: {e}"
        print(error_message)
        return error_message

def check_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"
