import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
titles, prices, ratings, descriptions = [], [], [], []

for page in range(1, 6):  # scrape first 5 pages
    url = base_url.format(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text[2:]  # £51.77 → 51.77
        rating = book.p["class"][1]
        
        # Go to product page for description
        product_link = "http://books.toscrape.com/catalogue/" + book.h3.a["href"]
        prod_res = requests.get(product_link)
        prod_soup = BeautifulSoup(prod_res.content, 'html.parser')
        desc_tag = prod_soup.find("meta", attrs={"name": "description"})
        description = desc_tag["content"].strip() if desc_tag else "No description"

        titles.append(title)
        prices.append(float(price))
        ratings.append(rating)
        descriptions.append(description)

# Store in Excel
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Description": descriptions
})

df.to_excel("books_data.xlsx", index=False)
print("Scraped data saved to books_data.xlsx")
