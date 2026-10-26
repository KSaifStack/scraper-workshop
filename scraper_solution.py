import requests
from bs4 import BeautifulSoup

# The page we want to scrape. Books to Scrape is a sandbox site made for
# practicing exactly this kind of exercise.
url = "https://books.toscrape.com/"

# Step 1: Fetch the page.
# requests.get() downloads the page. raise_for_status() makes the script fail
# loudly if the server returns an error instead of quietly parsing an error page.
response = requests.get(url)
response.raise_for_status()

# The server doesn't always declare its encoding, so requests may guess wrong
# and turn "£" into "Â£". Tell it the page is UTF-8 before parsing.
response.encoding = "utf-8"

# Step 2: Parse the HTML.
# BeautifulSoup turns the raw HTML text into a tree we can search.
# "html.parser" is Python's built-in parser, so no extra dependency is needed.
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all books.
# Every book on the page is an <article class="product_pod">. find_all()
# returns a list of every matching tag.
books = soup.find_all("article", class_="product_pod")

# Step 4: Loop and print title + price.
for book in books:
    # The title lives in the <a> tag inside the <h3>, and the full title is
    # stored in its title attribute (the link text is often truncated).
    title = book.h3.a["title"]

    # The price is in a <p class="price_color">, e.g. "£51.77".
    # .text gives us just the visible text, without the HTML tags.
    price = book.find("p", class_="price_color").text

    print(f"{title} - {price}")
