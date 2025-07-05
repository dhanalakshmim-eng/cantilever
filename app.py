from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("books_data.xlsx")

@app.route('/')
def home():
    return render_template("index.html", books=df.to_dict(orient="records"))

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    results = df[df['Title'].str.lower().str.contains(query)]
    return render_template("index.html", books=results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
