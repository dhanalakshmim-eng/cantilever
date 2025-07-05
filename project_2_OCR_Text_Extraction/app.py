from flask import Flask, render_template, request, redirect
import os
from ocr_engine import extract_text

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
'''UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')'''
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    uploaded_image = None

    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)

        if file:
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)
            uploaded_image = file.filename
            extracted_text = extract_text(image_path)

    return render_template('index.html', extracted_text=extracted_text, uploaded_image=uploaded_image)
    
if __name__ == '__main__':
    app.run(debug=False)
