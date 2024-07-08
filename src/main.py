from flask import Flask, request, render_template, send_file
import os
import pandas as pd
from data.import_data import import_csv, check_csv
from data.clean_data import clean_data
from data.export_data import export_data

app = Flask(__name__, template_folder='../templates')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../uploads')
app.config['EXPORT_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../exports')

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
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        os.makedirs(app.config['EXPORT_FOLDER'], exist_ok=True)

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        csv_content = check_csv(file_path)

        df = import_csv(file_path)
        if isinstance(df, pd.DataFrame):
            df_cleaned = clean_data(df)
            export_path = os.path.join(app.config['EXPORT_FOLDER'], 'cleaned_data.csv')
            df_cleaned.to_csv(export_path, index=False)
            return send_file(export_path, as_attachment=True)
        else:
            return df
    else:
        return 'Invalid file format. Please upload a CSV file'

if __name__ == '__main__':
    app.run(debug=True)
