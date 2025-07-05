# 📸 OCR Text Extraction Web App

A simple Flask-based web application that extracts text from uploaded images using the Tesseract OCR engine.

## 🚀 Features

- Upload any image containing text (PNG, JPG, JPEG).
- Extracts readable text using Tesseract OCR.
- Displays the extracted text on the same page.
- Shows a preview of the uploaded image.
- Clean, responsive UI built with Bootstrap and Font Awesome.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **OCR Engine**: Tesseract OCR
- **Frontend**: HTML5, Bootstrap 5, Font Awesome
- **Libraries**: `pytesseract`, `Pillow`

---

## 📁 Project Structure
project_2_OCR_Text_Extraction/

│
├── app.py  # Flask application logic

├── ocr_engine.py  # OCR logic using pytesseract

├── static/   # Stores uploaded images

│ └── uploads/  # Flask serves images from here

├── templates/

│ └── index.html  # Frontend UI

└── README.md  # Project documentation

🔒 static/uploads/ folder is used to store uploaded images temporarily.


## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/dhanalakshmim/cantilever/project_2_OCR_Text_Extraction.git
cd project_2_OCR_Text_Extraction

### 2. Install Python Requirements
### Make sure you have Python 3.x installed.

pip install flask pillow pytesseract

### 3. Install Tesseract OCR
Windows: Download from Tesseract OCR

Default path: C:\Program Files\Tesseract-OCR\tesseract.exe

### Linux:
sudo apt-get install tesseract-ocr

### macOS:
brew install tesseract

### Update the path in ocr_engine.py:
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


### ▶️ How to Run
python app.py
Then visit: http://127.0.0.1:5000 in your browser.

### 📷 Example Output
![Screenshot 2025-07-06 004144](https://github.com/user-attachments/assets/6496dedc-44bd-46b7-bc2c-16f245db7b68)

![image](https://github.com/user-attachments/assets/193fa333-b0ea-4d8a-bd87-bfca2bfe1f7f)

### 📝 Notes
1.Tesseract works best with clear, readable text.
2.You can enhance accuracy by pre-processing images (grayscale, resize, etc.).

### 📌 Future Enhancements
1.Download extracted text as .txt or .pdf

2.Support for multiple languages (Tamil, Hindi, etc.)

3.Batch processing of images

4.Drag and drop upload UI

### 🙋‍♀️ Developed By

DHANA LAKSHMI M

B.E. Computer Science & Engineering

Jerusalem College of Engineering


