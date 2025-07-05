import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("books_data.xlsx")

# Rating as numeric
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Num'] = df['Rating'].map(rating_map)

# Price Distribution
plt.figure(figsize=(8, 4))
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Count")
plt.show()

# Price vs Rating
plt.figure(figsize=(8, 4))
sns.boxplot(x="Rating", y="Price", data=df)
plt.title("Price by Rating")
plt.show()
