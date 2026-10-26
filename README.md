# Scraper Workshop

A beginner-friendly workshop on web scraping with Python. You'll use `requests` to download the [SimplifyJobs Summer 2027 Internships README](https://github.com/SimplifyJobs/Summer2027-Internships) and BeautifulSoup to pull every company, role, location, and application link out of its HTML tables.

## Prerequisites

- Python 3.x
- [VS Code](https://code.visualstudio.com/) (or any editor)

## Setup

Clone the repo and install the dependencies:

```bash
git clone https://github.com/KSaifStack/scraper-workshop.git
cd scraper-workshop
pip install -r requirements.txt
```

## Run it

Start with the skeleton, which has the four steps laid out with blanks to fill in:

```bash
python scraper_starter.py
```

Stuck? Compare your work against the fully commented solution:

```bash
python scraper_solution.py
```

The solution prints one line per listing, for example:

```
Royal Bank of Canada | Developer Intern | Toronto, ON, Canada | https://...
```

## Links

- [SearchTern](https://searchtern.ksaif.dev): internship and new-grad job tracker
