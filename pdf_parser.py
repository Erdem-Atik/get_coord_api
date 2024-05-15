from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
import pymupdf


import pdfplumber
print('hello')
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        text = extract_geo_coordinates(file)
        return jsonify({'coordinates': text})

def extract_geo_coordinates(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
       text = ''
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            try:
                page_text = page.extract_text()
                text += page_text if page_text else ''
            except AttributeError as e:
                # Handle the AttributeError gracefully
                print(f"Error processing page: {e}")
    return text

if __name__ == '__main__':
    app.run(debug=True)
