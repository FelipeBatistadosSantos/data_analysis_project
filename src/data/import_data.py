import pandas as pd

def import_csv(file_path):
    try:
        print(f"Tentando ler o arquivo CSV em: {file_path}")
        df = pd.read_csv(file_path, delimiter=',')  # Certifique-se de que o delimitador é uma vírgula
        print("Arquivo CSV lido com sucesso!")
        return df
    except FileNotFoundError:
        return f"O arquivo {file_path} não foi encontrado"
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo CSV: {str(e)}"

def check_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"
