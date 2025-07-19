# 📚 Web Scraping E-Commerce Flask App

This project scrapes book data from the open-source site **[BooksToScrape](https://books.toscrape.com/)** and displays it using a user-friendly Flask web app with emojis, pagination, and search features.


## 🌟 Features

- ✅ Web scraping of:
  - Title 📖
  - Price 💷
  - Rating ⭐
  - Description 📝
  - Cover Image 🖼️
- ✅ Search books by title 🔍
- ✅ View top N results with pagination ⏭️
- ✅ Store scraped data in Excel (`books_data.xlsx`) 📊
- ✅ Clean, styled UI with emojis 😎


## 💻 Tech Stack

| Technology    | Purpose                         |
|---------------|----------------------------------|
| **Python**    | Programming language             |
| **Flask**     | Web framework                    |
| **BeautifulSoup** | Web scraping HTML parser   |
| **Pandas**    | Data storage & Excel export      |
| **Matplotlib / Seaborn** *(optional)* | Data visualization 📈 |

---

## 🚀 Run the Project Locally

### 1. Clone the Repository

https://github.com/dhanalakshmim-eng/cantilever.git
cd cantilever/WebScraping_Ecommerce

#2. Install Dependencies


pip install -r requirements.txt

#3. Start the Flask App

python app.py
App will run at: http://127.0.0.1:5000

📁 Project Structure


project_1_WebScraping_Flask/
├── app.py                  # Flask app
├── scraper.py              # Scraper logic using BeautifulSoup
├── books_data.xlsx         # Excel output of scraped data
├── templates/
│   └── index.html          # Frontend HTML template
└── README.md               # Project documentation



<img width="1920" height="1080" alt="Screenshot 2025-07-19 234949" src="https://github.com/user-attachments/assets/e22d88b1-9a18-4f4d-9fa3-7ad6ee28c317


<img width="1920" height="1080" alt="Screenshot 2025-07-19 235019" src="https://github.com/user-attachments/assets/18d5e46c-274a-4329-b282-b0da8b53e7e3" />


<img width="1920" height="1080" alt="Screenshot 2025-07-19 235053" src="https://github.com/user-attachments/assets/8fbd865b-f8f8-462b-a8c1-8b2f3b5c80b5" />


<img width="1920" height="1080" alt="Screenshot 2025-07-19 235137" src="https://github.com/user-attachments/assets/50c7f5ac-c8d6-4562-a2c3-815476729206" />
