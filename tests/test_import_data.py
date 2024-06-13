import sys
import os
import unittest
import tempfile
from flask import Flask

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

    def test_import_csv(self):
        csv_content = "coluna1;coluna2\nvalor1;valor2"
        temp_csv = os.path.join(self.upload_folder, 'test_import.csv')
        with open(temp_csv, 'w') as f:
            f.write(csv_content)

        df = import_csv(temp_csv)
        self.assertFalse(df.empty)
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df.columns.tolist(), ['coluna1', 'coluna2'])
        self.assertEqual(df.iloc[0].tolist(), ['valor1', 'valor2'])

    def test_check_csv(self):
        csv_content = "coluna1;coluna2\nvalor1;valor2"
        temp_csv = os.path.join(self.upload_folder, 'test_check.csv')
        with open(temp_csv, 'w') as f:
            f.write(csv_content)

        content = check_csv(temp_csv)
        self.assertIn("coluna1;coluna2\nvalor1;valor2", content)

if __name__ == '__main__':
    unittest.main()
