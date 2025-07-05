import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []

for page in range(1,11):
    url = base_url.format(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    for book in soup.select('.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('.price_color').text.strip().replace('£', '')
        rating_class = book.p['class'][1]
        rating = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}.get(rating_class, '0')

        detail_link = book.h3.a['href']
        detail_url = "http://books.toscrape.com/catalogue/" + detail_link
        detail_res = requests.get(detail_url)
        detail_soup = BeautifulSoup(detail_res.content, 'html.parser')
        desc = detail_soup.select_one('meta[name="description"]')
        description = desc['content'].strip() if desc else "No description available"

        image_tag = book.select_one('img')
        image_url = "http://books.toscrape.com/" + image_tag['src'].replace('../', '') if image_tag else ''

        books.append({
            'Title': title,
            'Price': float(price),
            'Rating': rating,
            'Description': description,
            'Image_URL': image_url
        })

df = pd.DataFrame(books)
df.to_excel("books_data.xlsx", index=False)
print("Scraped data saved to books_data.xlsx")
