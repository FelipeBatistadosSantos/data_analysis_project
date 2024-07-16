import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd
from data.import_data import import_csv, check_csv
from data.clean_data import clean_data
from data.export_data import save_cleaned_data

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data_frame = import_csv(file_path)
        cleaned_data_frame = clean_data(data_frame)
        
        cleaned_file_path = save_cleaned_data(cleaned_data_frame, app.config['UPLOAD_FOLDER'])
        
        return render_template('show_table.html', table=cleaned_data_frame.to_html(index=False))
    return 'File not allowed', 400

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
