import pandas as pd

def remove_missing_values(df, strategy='drop', fill_value=None):
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill' and fill_value is not None:
        return df.fillna(fill_value)
    else:
        raise ValueError("Estratégia inválida ou fill_value não fornecido para preenchimento.")

def correct_data_types(df, column_types):
    for column, dtype in column_types.items():
        if column in df.columns:
            df[column] = df[column].astype(dtype)
        else:
            print(f"Coluna {column} não encontrada no DataFrame.")
    return df

def remove_duplicates(df):
    return df.drop_duplicates()

def handle_outliers(df, column, method='remove', threshold=None):
    if column not in df.columns:
        print(f"Coluna {column} não encontrada no DataFrame.")
        return df

    if method == 'remove':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        return df[~((df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR)))]
    elif method == 'cap' and threshold is not None:
        df[column] = df[column].clip(upper=threshold)
        return df
    else:
        raise ValueError("Método inválido ou threshold não fornecido para capping.")

def normalize_data(df, columns):
    for column in columns:
        if column in df.columns:
            df[column] = (df[column] - df[column].mean()) / df[column].std()
        else:
            print(f"Coluna {column} não encontrada no DataFrame.")
    return df

def clean_data(df):
    df = remove_missing_values(df, strategy='fill', fill_value=0)
    df = correct_data_types(df, {'some_column': 'float64'})  # Substitua 'some_column' pelo nome real da coluna
    df = remove_duplicates(df)
    df = handle_outliers(df, 'some_column')  # Substitua 'some_column' pelo nome real da coluna
    df = normalize_data(df, ['some_column'])  # Substitua 'some_column' pelo nome real da coluna
    return df
