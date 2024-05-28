from flask import Flask, request, render_template
import os
import pandas as pd
from data.import_data import import_csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', method = ['POST'])
def upload_files():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.csv'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        df = import_csv(file_path)
        if isinstance(df, pd.DataFrame):
            return df.to_html()
        else:
            return df
    else: 
        return 'Invalid file format. Please Inport a CSV file'
    
if __name__ == '__main__':
    app.run(debug=True)    
    