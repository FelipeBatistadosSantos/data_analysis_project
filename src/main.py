from flask import Flask, request, render_template
import os
import pandas as pd
from data.import_data import import_csv, check_csv
from data.clean_data import clean_data

app = Flask(__name__, template_folder='../templates')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../uploads')

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.csv'):
        # Cria o diretório de uploads se ele não existir
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print(f"Salvando arquivo em: {file_path}")
        file.save(file_path)
        
        # Verificar o conteúdo do CSV
        csv_content = check_csv(file_path)
        print(f"Conteúdo do arquivo CSV:\n{csv_content}")
        
        df = import_csv(file_path)
        if isinstance(df, pd.DataFrame):
            # Exibe os nomes das colunas para referência
            print(f"Colunas do DataFrame: {df.columns.tolist()}")
            
            # Limpar os dados (substitua 'some_column' pelos nomes reais das colunas)
            df = clean_data(df)
            print("Retornando DataFrame como HTML")
            return df.to_html()
        else:
            print("Erro ao processar o CSV:", df)
            return df
    else:
        return 'Invalid file format. Please upload a CSV file'

if __name__ == '__main__':
    app.run(debug=True)
