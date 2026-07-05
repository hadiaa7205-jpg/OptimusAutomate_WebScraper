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
## Sample Output

When you run the program:

```
Website loaded successfully!

Total books found: 20

{'Title': 'A Light in the Attic', 'Price': '£51.77', 'Availability': 'In stock', 'Rating': 'Three'}
{'Title': 'Tipping the Velvet', 'Price': '£53.74', 'Availability': 'In stock', 'Rating': 'One'}

Total books scraped: 1000

Data successfully saved to books.json
Data successfully saved to books.csv
```
## Author

Hadia Batool
