import requests
from bs4 import BeautifulSoup
import csv
import logging
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"


class BookScraper:
    def __init__(self, max_workers=5):
        self.session = self._create_session()
        self.max_workers = max_workers
        self.books = []

    def _create_session(self):
        session = requests.Session()
        session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })

        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504]
        )

        adapter = HTTPAdapter(max_retries=retries)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def get_total_pages(self):
        url = "http://books.toscrape.com/"
        response = self.session.get(url, timeout=10)
        response.encoding = "utf-8"
    
        soup = BeautifulSoup(response.text, "html.parser")
    
        pager = soup.select_one("li.current")
    
        if pager:
            text = pager.get_text(strip=True)
            total = int(text.split()[-1])
            return total
    
        return 1


    def scrape_page(self, page_number):
        url = BASE_URL.format(page_number)
        logging.info(f"Scraping page {page_number}")

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            logging.error(f"Failed to fetch page {page_number}: {e}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        results = []

        for book in books:
            try:
                title = book.h3.a["title"]

                price_text = book.find("p", class_="price_color").get_text(strip=True)

                # Keep only digits and decimal point
                clean_price = "".join(ch for ch in price_text if ch.isdigit() or ch == ".")
                
                if not clean_price:
                    raise ValueError(f"Invalid price format: {price_text}")
                
                price = float(clean_price)


                rating_class = book.find("p", class_="star-rating")["class"]
                rating = rating_class[1]

                results.append({
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "page": page_number
                })

            except Exception as e:
                logging.warning(f"Error parsing book: {e}")

        return results

    def scrape_all(self, total_pages=None):
        if total_pages is None:
            total_pages = self.get_total_pages()

        logging.info(f"Total pages detected: {total_pages}")

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(self.scrape_page, page)
                for page in range(1, total_pages + 1)
            ]

            for future in as_completed(futures):
                self.books.extend(future.result())

        logging.info(f"Total books scraped: {len(self.books)}")
        return self.books

    @staticmethod
    def search_books(books, keyword):
        return [
            book for book in books
            if keyword.lower() in book["title"].lower()
        ]

    @staticmethod
    def save_to_csv(data, filename="results.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["title", "price", "rating", "page"]
            )
            writer.writeheader()
            writer.writerows(data)

        logging.info(f"Results saved to {filename}")

    @staticmethod
    def print_results(data):
        if not data:
            print("No matching books found.")
            return

        print("\n" + "=" * 90)
        print(f"{'No':<4} {'Title':<50} {'Price':<10} {'Rating':<10} {'Page':<5}")
        print("=" * 90)

        for i, book in enumerate(data, 1):
            print(
                f"{i:<4} "
                f"{book['title'][:47]:<50} "
                f"£{book['price']:<10.2f} "
                f"{book['rating']:<10} "
                f"{book['page']:<5}"
            )

        print("=" * 90)

        avg_price = sum(b["price"] for b in data) / len(data)
        print(f"\nTotal Matches: {len(data)}")
        print(f"Average Price: £{avg_price:.2f}")
        print(f"Cheapest: £{min(b['price'] for b in data):.2f}")
        print(f"Most Expensive: £{max(b['price'] for b in data):.2f}")
        print()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    parser = argparse.ArgumentParser(description="Advanced Book Scraper")
    parser.add_argument("--keyword", required=True, help="Keyword to search")
    parser.add_argument("--pages", type=int, help="Number of pages to scrape")
    parser.add_argument("--sort", choices=["asc", "desc"], help="Sort by price")
    parser.add_argument("--output", default="results.csv", help="CSV output file")

    args = parser.parse_args()

    scraper = BookScraper(max_workers=5)

    books = scraper.scrape_all(total_pages=args.pages)

    matches = scraper.search_books(books, args.keyword)

    if args.sort == "asc":
        matches.sort(key=lambda x: x["price"])
    elif args.sort == "desc":
        matches.sort(key=lambda x: x["price"], reverse=True)

    scraper.print_results(matches)
    scraper.save_to_csv(matches, filename=args.output)


if __name__ == "__main__":
    main()
