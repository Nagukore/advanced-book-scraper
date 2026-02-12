📘 Advanced Book Scraper CLI

A scalable, multi-threaded command-line web scraping tool built in Python.
Designed with production-oriented architecture, retry handling, encoding safety, and structured output.

📌 Project Overview

This project demonstrates a robust web scraping pipeline using Python.
It extracts structured book data from BooksToScrape and provides:

Parallel data extraction

Pagination automation

Clean numeric parsing

Structured logging

CLI-based filtering and sorting

CSV export with analytics summary

The goal of this project is to simulate real-world scraper design patterns rather than build a simple script.

⚙️ Core Capabilities
🔄 Concurrent Scraping

Implements ThreadPoolExecutor to fetch multiple pages efficiently.

🔁 Retry Strategy

Uses urllib3 Retry with HTTPAdapter for resilient network handling.

🔐 Session Management

Leverages requests.Session() for connection pooling and improved performance.

📄 Automatic Pagination Detection

Dynamically determines total available pages.

🧹 Encoding-Safe Data Parsing

Handles UTF-8 encoding and currency symbol anomalies.

🧾 CLI-Based Filtering & Sorting

Search books by keyword and sort results by price.

📊 Analytics Summary

Automatically calculates:

Total Matches

Average Price

Cheapest Book

Most Expensive Book

🏗 Architecture Design
BookScraper Class
│
├── Session Initialization (Retry + Headers)
├── Pagination Detection
├── Page Scraping (Concurrent Execution)
├── Data Parsing & Cleaning
├── Filtering Logic
├── Sorting Logic
├── CSV Export
└── Structured Output + Logging


This modular design improves:

Maintainability

Scalability

Testability

🛠 Tech Stack
Component	Technology
Language	Python 3.x
HTTP Client	requests
Parsing	BeautifulSoup4
Concurrency	concurrent.futures
CLI Interface	argparse
Logging	logging
Retry Handling	urllib3 Retry
🚀 Installation

Clone repository:

git clone https://github.com/Nagukore/advanced-book-scraper.git
cd advanced-book-scraper


Create virtual environment:

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

▶ Usage Examples
Basic Keyword Search
python main.py --keyword travel

Sort by Price (Ascending)
python main.py --keyword travel --sort asc

Limit Pages
python main.py --keyword travel --pages 10

Custom Output File
python main.py --keyword travel --output travel_books.csv

📊 Sample Output Structure

Console Output:

No   Title                                Price     Rating   Page
--------------------------------------------------------------------
1    It's Only the Himalayas              £45.17    Two      5
...


Summary:

Total Matches: 12
Average Price: £34.56
Cheapest: £12.95
Most Expensive: £57.83


CSV Output:

Title	Price	Rating	Page
🎯 Engineering Highlights

Designed using OOP principles

Implements concurrency for performance

Handles real-world encoding issues

Applies retry/backoff mechanism

Built as reusable CLI tool

Clean Git workflow & documentation

📈 Potential Enhancements

SQLite integration

Category-wise scraping

REST API wrapper (FastAPI)

Streamlit analytics dashboard

Docker containerization

Automated unit tests

⚠ Disclaimer

This scraper is built for educational purposes using a public sandbox website.

👤 Author

Nagesh
AI/ML & Web Development Enthusiast
Focused on scalable system design and automation tools.