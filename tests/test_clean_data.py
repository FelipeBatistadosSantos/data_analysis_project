import os
import pytest
from flask import Flask
import pandas as pd

# Adiciona o diretório src ao PYTHONPATH
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app, import_csv, clean_data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_uploads')
    client = app.test_client()
    
    # Cria a pasta de uploads de teste
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    yield client
    
    # Limpa a pasta de uploads de teste após os testes
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(file_path):
            os.unlink(file_path)
    os.rmdir(app.config['UPLOAD_FOLDER'])

def test_upload_and_clean_csv(client):
    data = {
        'file': (open('tests/test_data.csv', 'rb'), 'test_data.csv')
    }
    
    # Testa o upload do arquivo CSV
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'<table border="1" class="dataframe">' in response.data

def test_import_csv():
    # Testa a importação do CSV
    df = import_csv('tests/test_data.csv')
    if isinstance(df, pd.DataFrame):
        assert not df.empty
        assert 'coluna1' in df.columns  # Substitua 'coluna1' pelo nome real da coluna
    else:
        pytest.fail(f"Falha ao importar CSV: {df}")

def test_clean_data():
    # Testa a limpeza dos dados
    df = import_csv('tests/test_data.csv')
    if isinstance(df, pd.DataFrame):
        df_cleaned = clean_data(df)
        assert not df_cleaned.empty
        # Adicione mais assertivas baseadas na limpeza que você espera
    else:
        pytest.fail(f"Falha ao importar CSV: {df}")
