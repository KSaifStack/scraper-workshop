import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

# Step 1: Fetch the page
response = None

# Step 2: Parse the HTML
soup = None

# Step 3: Find all books
books = None

# Step 4: Loop and print title + price
for book in books:
    title = None
    price = None
    print(f"{title} - {price}")
