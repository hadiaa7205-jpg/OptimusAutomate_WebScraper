import requests
import json
import csv
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"


def get_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def scrape_books(html):
    soup = BeautifulSoup(html, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    print(f"Total books found: {len(books)}\n")

    # List to store all books
    book_list = []

    for book in books:

        # Title
        title = book.h3.a.get("title", "No Title")

        # Price
        price = book.find("p", class_="price_color")
        if price:
            price = price.text.strip()
        else:
            price = "Not Available"

        # Availability
        availability = book.find("p", class_="instock availability")
        if availability:
            availability = availability.text.strip()
        else:
            availability = "Unknown"

        # Rating
        rating = book.find("p", class_="star-rating")
        if rating:
            rating = rating.get("class")[1]
        else:
            rating = "No Rating"

        # Store data in dictionary
        book_data = {
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        }

        # Add dictionary to list
        book_list.append(book_data)

        # Print book details
        print("=" * 50)
        print(book_data)

    # Return complete list
    return book_list


def save_to_json(book_list, filename="books.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(book_list, file, indent=4, ensure_ascii=False)

        print(f"\n✅ Data successfully saved to {filename}")

    except Exception as e:
        print(f"Error saving JSON: {e}")

def save_to_csv(book_list, filename="books.csv"):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["Title", "Price", "Availability", "Rating"]
            )

            writer.writeheader()

            writer.writerows(book_list)

        print(f"✅ Data successfully saved to {filename}")

    except Exception as e:
        print(f"Error saving CSV: {e}")

def scrape_all_pages():
    all_books = []

    # Loop through pages 1 to 50
    for page in range(1, 51):

        print(f"\nScraping Page {page}...")

        url = BASE_URL.format(page)

        html = get_page(url)

        if html:

            books = scrape_books(html)

            all_books.extend(books)

        else:

            print(f"Skipping page {page}")

    return all_books

# ---------------- MAIN PROGRAM ---------------- #
def main():

    while True:

        print("\n" + "=" * 50)
        print("        BOOK SCRAPER MENU")
        print("=" * 50)
        print("1. Scrape First Page")
        print("2. Scrape All Pages")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":

            html = get_page(BASE_URL.format(1))

            if html:
                books = scrape_books(html)

                save_to_json(books)
                save_to_csv(books)

                print(f"\nTotal books scraped: {len(books)}")

        elif choice == "2":

            books = scrape_all_pages()

            save_to_json(books)
            save_to_csv(books)

            print(f"\nTotal books scraped: {len(books)}")

        elif choice == "3":

            print("\nThank you for using the Book Scraper!")
            break

        else:

            print("\nInvalid choice! Please enter 1, 2 or 3.")


main()