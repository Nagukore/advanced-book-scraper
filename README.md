# Advanced Book Scraper CLI

A production-oriented, multi-threaded command-line web scraper built in Python.

This project demonstrates real-world scraping architecture including concurrency, retry strategies, structured logging, CLI filtering, and CSV analytics export.

---

## Overview

The scraper extracts structured book data from:

http://books.toscrape.com

It is designed to simulate production-grade scraper design rather than a simple script.

### Core Objectives

- Implement concurrent scraping
- Apply resilient retry handling
- Ensure encoding-safe numeric parsing
- Provide structured CLI interaction
- Export clean analytics-ready data

---

## Features

| Feature | Description |
|----------|-------------|
| Concurrent Scraping | Parallel page processing using ThreadPoolExecutor |
| Retry Strategy | urllib3 Retry with HTTPAdapter |
| Session Pooling | Connection reuse via requests.Session() |
| Pagination Detection | Automatically detects total available pages |
| Encoding-Safe Parsing | Handles UTF-8 and currency anomalies |
| CLI Filtering | Keyword-based filtering via argparse |
| Sorting Support | Price-based sorting (asc/desc) |
| CSV Export | Structured CSV output |
| Analytics Summary | Calculates average, minimum, and maximum price |

---

## Architecture

BookScraper
│
├── Session Setup
│ ├── Headers
│ └── Retry Strategy
│
├── Pagination Detection
│
├── Concurrent Page Scraping
│
├── Data Parsing & Cleaning
│
├── Filtering & Sorting
│
├── CSV Export
│
└── Structured Logging


### Design Benefits

- Maintainable
- Scalable
- Testable
- Clean separation of concerns

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.x |
| HTTP Client | requests |
| Parsing | BeautifulSoup4 |
| Concurrency | concurrent.futures |
| CLI | argparse |
| Logging | logging |
| Retry Handling | urllib3 Retry |

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/Nagukore/advanced-book-scraper.git
cd advanced-book-scraper
2. Create Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Usage
Basic Keyword Search
python main.py --keyword travel
Sort by Price (Ascending)
python main.py --keyword travel --sort asc
Limit Number of Pages
python main.py --keyword travel --pages 10
Custom Output File
python main.py --keyword travel --output travel_books.csv
Output Structure
Console Output
Column	Description
Title	Book title
Price	Book price
Rating	Star rating
Page	Page number
Analytics Summary
Total Matches: 12
Average Price: £34.56
Cheapest Book: £12.95
Most Expensive Book: £57.83
CSV Columns
Title, Price, Rating, Page
Engineering Highlights
Object-Oriented Architecture

Concurrent execution for performance

Retry and backoff mechanism

Encoding-safe numeric extraction

CLI-based data filtering

Structured logging practices

Future Improvements
SQLite persistence layer

Category-wise scraping

REST API wrapper (FastAPI)

Streamlit dashboard

Docker containerization

Unit test coverage

Disclaimer
This scraper is built for educational purposes using a public sandbox website.

Author
Nagesh
AI/ML & Web Development Enthusiast
Focused on scalable system design and automation tools.