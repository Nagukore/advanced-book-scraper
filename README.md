# 📘 Advanced Book Scraper CLI

> A scalable, multi-threaded command-line web scraping tool built in Python.  
> Designed using production-oriented architecture with retry handling, encoding safety, concurrency, and structured output.

---

## 📌 Project Overview

This project demonstrates a robust scraping pipeline built with clean architecture principles.

It extracts structured book data from:

🔗 http://books.toscrape.com

### 🎯 Objectives

- Simulate real-world scraper architecture
- Implement concurrency for performance
- Handle encoding & currency parsing issues
- Build a reusable CLI-based scraping tool

---

## 🚀 Key Capabilities

| Capability | Description |
|------------|------------|
| 🔄 Concurrent Scraping | Uses `ThreadPoolExecutor` for parallel page extraction |
| 🔁 Retry Strategy | Implements `urllib3 Retry` with HTTPAdapter |
| 🔐 Session Pooling | Uses `requests.Session()` for connection reuse |
| 📄 Pagination Detection | Automatically detects total page count |
| 🧹 Encoding-Safe Parsing | Handles UTF-8 and currency anomalies |
| 🧾 CLI Filtering | Keyword-based filtering using `argparse` |
| 📊 Analytics Summary | Calculates average, min, and max price |
| 📁 CSV Export | Structured export to CSV |

---

## 🏗 Architecture Overview

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


### 📈 Design Benefits

- Maintainability  
- Scalability  
- Testability  
- Clean separation of concerns  

---

## 🛠 Technology Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.x |
| HTTP Client | requests |
| HTML Parsing | BeautifulSoup4 |
| Concurrency | concurrent.futures |
| CLI Interface | argparse |
| Logging | logging |
| Retry Handling | urllib3 Retry |

---

## 📦 Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Nagukore/advanced-book-scraper.git
cd advanced-book-scraper
2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶ Usage Examples
🔎 Basic Keyword Search
python main.py --keyword travel
📊 Sort by Price (Ascending)
python main.py --keyword travel --sort asc
📄 Limit Pages
python main.py --keyword travel --pages 10
📁 Custom Output File
python main.py --keyword travel --output travel_books.csv
📊 Output Structure
Console Output
Field	Description
Title	Book Title
Price	Book Price
Rating	Star Rating
Page	Page Number
Summary Metrics
Total Matches: 12
Average Price: £34.56
Cheapest: £12.95
Most Expensive: £57.83
CSV Output Columns
Title	Price	Rating	Page
🎯 Engineering Highlights
Object-Oriented Design (OOP)

Concurrent execution for performance

Retry & backoff strategy

Encoding-safe numeric parsing

Modular CLI tool design

Production-style logging

📈 Future Improvements
SQLite database integration

Category-based scraping

REST API wrapper (FastAPI)

Streamlit analytics dashboard

Docker containerization

Unit testing suite

⚠ Disclaimer
This scraper is built for educational purposes using a publicly available sandbox website.

👤 Author
Nagesh
AI/ML & Web Development Enthusiast
Focused on scalable system design and automation tools.