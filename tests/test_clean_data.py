import os
import sys
import pytest
import pandas as pd

# Adiciona o diretório 'src' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import app
from data.clean_data import clean_data

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_and_clean_csv(client):
    # Caminho do arquivo exportado
    export_path = os.path.join(os.path.dirname(__file__), '../exports/cleaned_data.csv')

    # Garante que o diretório de exportação existe
    os.makedirs(os.path.dirname(export_path), exist_ok=True)

    # Dados de teste
    data = {
        'file': (open('tests/test_data.csv', 'rb'), 'test_data.csv')
    }

    # Testa o upload do arquivo CSV
    response = client.post('/upload', data=data, content_type='multipart/form-data')

    # Verifica se o arquivo foi salvo corretamente
    assert response.status_code == 200
    assert os.path.exists(export_path)

    # Lê o conteúdo do arquivo exportado
    with open(export_path, 'r') as f:
        cleaned_data = f.read()

    # Verifica se o conteúdo do arquivo está correto
    expected_content = "coluna1,coluna2,coluna3\n1,2,3\n4,5,6\n7,8,9\n"
    assert cleaned_data == expected_content

def test_clean_data():
    # Dados de teste
    raw_data = {
        'coluna1': [1, 4, 7],
        'coluna2': [2, 5, 8],
        'coluna3': [3, 6, 9]
    }
    df = pd.DataFrame(raw_data)

    # Limpa os dados
    cleaned_df = clean_data(df)

    # Dados esperados após limpeza
    expected_data = {
        'coluna1': [1, 4, 7],
        'coluna2': [2, 5, 8],
        'coluna3': [3, 6, 9]
    }
    expected_df = pd.DataFrame(expected_data)

    # Verifica se os dados limpos estão corretos
    pd.testing.assert_frame_equal(cleaned_df, expected_df)
