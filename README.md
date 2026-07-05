# OptimusAutomate_WebScraper
OptimusAutomate_WebScraper/ │ ├── scraper.py ├── requirements.txt └── README.md
# 📚 Web Scraper

A Python CLI-based web scraper built using **Requests** and **BeautifulSoup**.

## Features

- Scrapes book data from Books to Scrape
- Extracts:
  - Title
  - Price
  - Availability
  - Rating
- Handles pagination (all pages)
- Handles request errors
- Handles missing data
- Saves data to JSON
- Saves data to CSV
- Command Line Interface (CLI)

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- JSON
- CSV

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## Run

```bash
python scraper.py
```

## Output Files

- books.json
- books.csv

## Author

Hadia Batool
