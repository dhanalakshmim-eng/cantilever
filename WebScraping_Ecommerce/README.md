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


WebScraping_Ecommerce/

├── templates/

│   └── index.html          # Frontend HTML template\

├── README.md

├── app.py                  # Flask app

├── books_data.xlsx         # Excel output of scraped data

├── requirements.txt

├── scraper.py              # Scraper logic using BeautifulSoup

├── visualize.py            # for visualization

└── webscraping document.pdf               # Project documentation


#🎥 Demo

[Click here to watch the demo video]
https://drive.google.com/file/d/1kxsY9_9gxRVDpgiRWcEpgcEePxSf_AZO/view?usp=sharing

#Author
Dhana Lakshmi M
 B.E. Computer Science
 Email: dd406652dhana@gmail.com 
GitHub: https://github.com/dhanalakshmim-eng/cantilever.git
