import os
import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_upload_and_clean_csv(client):
    # Diretório e caminho do arquivo exportado
    export_dir = os.path.join(os.path.dirname(__file__), '../exports')
    export_path = os.path.join(export_dir, 'cleaned_data.csv')

    # Garante que o diretório de exportação existe
    os.makedirs(export_dir, exist_ok=True)

    # Dados de teste
    data = {
        'file': (open('tests/test_data.csv', 'rb'), 'test_data.csv')
    }

    # Testa o upload do arquivo CSV
    response = client.post('/upload', data=data, content_type='multipart/form-data')

    # Verifica se o arquivo foi salvo corretamente
    assert response.status_code == 200
    assert os.path.exists(export_path)
