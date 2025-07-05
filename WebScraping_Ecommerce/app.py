from flask import Flask, render_template, request
import pandas as pd
import math

app = Flask(__name__)
df = pd.read_excel("books_data.xlsx")

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = 10
    total = len(df)
    pages = max(1, math.ceil(total / per_page))

    if page > pages:
        page = pages

    start = (page - 1) * per_page
    end = start + per_page
    books = df.iloc[start:end].to_dict(orient="records")

    return render_template("index.html", books=books, query=None, found=True, page=page, pages=pages)


@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    page = int(request.args.get('page', 1))
    per_page = 10

    filtered = df[df['Title'].str.lower().str.contains(query)]
    total = len(filtered)
    pages = max(1, math.ceil(total / per_page))

    if page > pages:
        page = pages

    start = (page - 1) * per_page
    end = start + per_page
    books = filtered.iloc[start:end].to_dict(orient="records")

    return render_template("index.html", books=books, query=query, found=not filtered.empty, page=page, pages=pages)


if __name__ == "__main__":
    app.run(debug=False)
