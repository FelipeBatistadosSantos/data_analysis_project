import sys
import os
import unittest
import tempfile
from flask import Flask
import pytest
import pandas as pd

# Adicione o diretório src ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Agora importe o app do main
from main import app
from data.import_data import import_csv, check_csv

class DataImportTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.upload_folder = tempfile.mkdtemp()

    def tearDown(self):
        # Remoção de arquivos temporários criados durante os testes
        for root, dirs, files in os.walk(self.upload_folder):
            for file in files:
                os.remove(os.path.join(root, file))

    def test_upload_csv_file(self):
        csv_content = "coluna1;coluna2\nvalor1;valor2"
        temp_csv = os.path.join(self.upload_folder, 'test.csv')
        with open(temp_csv, 'w') as f:
            f.write(csv_content)
        with open(temp_csv, 'rb') as f:
            response = self.app.post('/upload', data={'file': f})

        self.assertEqual(response.status_code, 200)
        self.assertIn('<table', response.data.decode('utf-8'))

    def test_import_csv():
    # Testa a importação do CSV
        df = import_csv('tests/test_data.csv')
        if isinstance(df, pd.DataFrame):
            assert not df.empty
            assert 'coluna1' in df.columns  # Verifica se a coluna 'coluna1' está presente
            assert 'coluna2' in df.columns  # Verifica se a coluna 'coluna2' está presente
            assert 'coluna3' in df.columns  # Verifica se a coluna 'coluna3' está presente
        else:
            pytest.fail(f"Falha ao importar CSV: {df}")

    def test_check_csv(self):
        csv_content = "coluna1;coluna2\nvalor1;valor2"
        temp_csv = os.path.join(self.upload_folder, 'test_check.csv')
        with open(temp_csv, 'w') as f:
            f.write(csv_content)

        content = check_csv(temp_csv)
        self.assertIn("coluna1;coluna2\nvalor1;valor2", content)

class DataImportTestCase(unittest.TestCase):
    def test_import_csv(self):
        df = import_csv('tests/test_data.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertIn('coluna1', df.columns)  # Verifica se a coluna 'coluna1' está presente
        self.assertIn('coluna2', df.columns)  # Verifica se a coluna 'coluna2' está presente
        self.assertIn('coluna3', df.columns)  # Verifica se a coluna 'coluna3' está presente

if __name__ == '__main__':
    unittest.main()
