import unittest
import os
import tempfile
from flask import Flask
from main import app
from data.import_data import import_csv, check_csv


class DataImportTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app = True
        self.upload_folder = tempfile.mkdtemp()

    def tearDown(self):
        #Remotion of temporary files created during the tests
        for root, dirs, files in os.walk(self.upload_folder):
            for file in files:
                os.remove(os.path.join(root, file))

    def test_upload_csv_file(self):
        csv_content = "coluna1;coluna2\nvalor1;valor2"
        temp_csv = os.path.join(self.upload_folder, 'test.csv')
        with open(temp_csv, 'w') as f:
            f.write(csv_content)
        with open(temp_csv, 'rb') as f:
            response = self.app.post('/upload', data={'file':f})
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('<table', response.data.decode('utf-8'))
        print(self.assertEqual(response.status_code, 200))
        print(self.assertIn('<table', response.data.decode('utf-8')))

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

