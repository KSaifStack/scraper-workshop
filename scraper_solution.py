import requests
from bs4 import BeautifulSoup

# The SimplifyJobs repo keeps its listings in the README. We use the raw file
# instead of the GitHub page so we get the Markdown/HTML directly, with no
# menus, buttons, or JavaScript in the way.
url = "https://raw.githubusercontent.com/SimplifyJobs/Summer2027-Internships/dev/README.md"

# Step 1: Fetch the README.
# requests.get() downloads it and raise_for_status() fails loudly if GitHub
# returns an error instead of the file.
response = requests.get(url)
response.raise_for_status()

# Tell requests the file is UTF-8 so special characters come through correctly.
response.encoding = "utf-8"

# Step 2: Parse the HTML tables inside the README.
# The README is Markdown, but each category's jobs are stored in an HTML
# <table>, so BeautifulSoup can search it like any other web page.
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all job rows.
# Every job is a <tr>, and every data row has five <td> cells:
# Company, Role, Location, Application, Age.
rows = soup.find_all("tr")

# Step 4: Loop and print company, role, location, and application link.
# Some rows use "↳" to mean "same company as the row above", so we remember
# the last real company name and reuse it.
last_company = ""

for row in rows:
    cells = row.find_all("td")

    # Header rows use <th> instead of <td>, so this also skips them.
    if len(cells) != 5:
        continue

    company = cells[0].get_text(" ", strip=True)

    if company == "↳":
        company = last_company
    else:
        last_company = company

    role = cells[1].get_text(" ", strip=True)
    location = cells[2].get_text(" ", strip=True)

    # The application cell holds two links: the real application first, then a
    # Simplify link. We only want the first one.
    apply_url = cells[3].find("a")["href"]

    print(f"{company} | {role} | {location} | {apply_url}")
