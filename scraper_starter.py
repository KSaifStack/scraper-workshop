import requests
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/dev/README.md"

# Step 1: Fetch the README
response = None

# Step 2: Parse the HTML tables inside the README
soup = None

# Step 3: Find all job rows
rows = None

# Step 4: Loop and print company, role, location, and application link
last_company = ""

for row in rows:
    cells = row.find_all("td")

    if len(cells) != 5:
        continue

    company = None
    role = None
    location = None
    apply_url = None

    if company == "↳":
        company = last_company
    else:
        last_company = company

    print(f"{company} | {role} | {location} | {apply_url}")
