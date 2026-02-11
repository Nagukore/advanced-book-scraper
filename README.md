\# Advanced Book Scraper



A scalable, multi-threaded CLI-based web scraper built in Python.



This project scrapes book data from http://books.toscrape.com and provides structured output, analytics, and CSV export.



---



\## 🚀 Features



\- Multi-threaded scraping using ThreadPoolExecutor

\- Session reuse for performance optimization

\- Automatic pagination detection

\- Retry mechanism for fault tolerance

\- CLI argument support

\- Encoding-safe data parsing

\- Structured logging

\- CSV export

\- Summary analytics (average, min, max price)



---



\## 🛠 Tech Stack



\- Python 3.x

\- requests

\- BeautifulSoup4

\- concurrent.futures

\- argparse

\- logging



---



\## 📦 Installation



Clone the repository:



git clone https://github.com/Nagukore/advanced-book-scraper.git

cd advanced-book-scraper





Create virtual environment:



python -m venv .venv

.venv\\Scripts\\activate





Install dependencies:



pip install -r requirements.txt





---



\## ▶ Usage



Basic search:



python main.py --keyword travel





Sort by price:



python main.py --keyword travel --sort asc





Limit number of pages:



python main.py --keyword travel --pages 10





Custom output file:



python main.py --keyword travel --output results.csv





---



\## 📊 Output



\- Book Title

\- Price

\- Rating

\- Page Number

\- Summary Statistics



Results are exported to CSV format.



---



\## 🎯 Learning Highlights



\- Robust web scraping architecture

\- Handling encoding issues in HTML

\- Multi-threaded execution

\- CLI tool development

\- Structured logging practices



---



\## ⚠ Disclaimer



Built for educational purposes using a public practice website.



