import pandas as pd

#Função com o objetivo de excluir linhas em branco ou preencher espaçoes em branco. Lida com Valores ausentes no DataFrame
def remove_missing_values(df, strategy='drop', fill_value=None):
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill' and fill_value is not None:
        return df.fillna(fill_value)
    else:
        raise ValueError("Estrategia Inválida ou fill_value não fornecido para preenchimento")

"""Função para correção de dados. colum_types é um dicionário onde as chaves são os nomes das colunas e os valores são os 
tipos de dados desejados"""   
def correct_data_types(df, column_types):
        return df.astype(column_types)

#Função que remove duplicatas, mantendo apenas a primeira ocorrência
def remove_duplicate(df):
    return df.drop_duplicates()

def handle_outliers(df, column, method='remove', threshold=None):
    if method == 'remove':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        return df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]
    elif method == 'cap' and threshold is not None:
        df[column] = df[column].clip(upper=threshold)
        return df
    else:
        raise ValueError("Método inválido ou threshold não fornecido para capping")
    
def normalize_data(df, columns):
    for column in columns:
        df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df

def clean_data(df):
    df = remove_missing_values(df, strategy='fill', fill_value=0)
    df = correct_data_types(df, {'some_column': 'float64'})
    df = remove_duplicate(df)
    df = handle_outliers(df, 'some_column')
    df = normalize_data(df, ['some_column'])
    return df