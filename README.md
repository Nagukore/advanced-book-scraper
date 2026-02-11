# Advanced Web Scraper CLI

A scalable, multi-threaded CLI-based web scraper built in Python.  
This project scrapes book data from http://books.toscrape.com and provides structured output with analytics and CSV export.

---

## 🔥 Features

- Multi-threaded scraping (ThreadPoolExecutor)
- Session reuse for performance
- Automatic pagination detection
- Retry mechanism for robustness
- CLI argument support
- Clean data parsing with encoding handling
- Structured console output
- CSV export support
- Logging integration

---

## 🛠 Tech Stack

- Python 3.x
- requests
- BeautifulSoup4
- concurrent.futures
- argparse
- logging

---

## 📂 Project Structure

advanced-web-scraper-cli/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/advanced-web-scraper-cli.git
cd advanced-web-scraper-cli


Create virtual environment:

python -m venv .venv
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


---

## 🚀 Usage

Basic search:

python main.py --keyword travel


With sorting:

python main.py --keyword travel --sort asc


Limit pages:

python main.py --keyword travel --pages 10


Custom output file:

python main.py --keyword travel --output travel_books.csv


---

## 📊 Output Example

- Title
- Price
- Rating
- Page number
- Average price summary
- Cheapest & Most expensive book

Results are saved to `results.csv` by default.

---

## 🎯 Learning Outcomes

- Handling encoding issues in scraping
- Designing scalable scraping architecture
- Implementing retry mechanisms
- Multi-threaded scraping design
- CLI tool development in Python
- Structured logging practices

---

## ⚠ Disclaimer

This scraper is built for educational purposes using a public practice website.

---

## 📌 Future Improvements

- SQLite database integration
- Category-based scraping
- REST API wrapper (FastAPI)
- Docker containerization
- Streamlit dashboard

---

## 👤 Author

Nagesh  
AI/ML & Web Development Enthusiast
