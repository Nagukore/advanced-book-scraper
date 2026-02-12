📚 Advanced Book Scraper CLIA production-oriented, multi-threaded command-line web scraper built in Python. This project demonstrates real-world scraping architecture including concurrency, retry strategies, and structured data analytics.🛠 Technology StackLayerTechnologyLanguagePython 3.xHTTP ClientrequestsParsingBeautifulSoup4Concurrencyconcurrent.futuresCLI FrameworkargparseResilienceurllib3 Retry🚀 Installation1. Clone the RepositoryBashgit clone https://github.com/Nagukore/advanced-book-scraper.git
cd advanced-book-scraper
2. Create Virtual EnvironmentWindows:Bashpython -m venv .venv
.venv\Scripts\activate
macOS / Linux:Bashpython3 -m venv .venv
source .venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
▶ Usage ExamplesThe scraper is highly configurable via CLI arguments.🔍 Basic Keyword SearchBashpython main.py --keyword travel
📈 Sort by Price (Ascending)Bashpython main.py --keyword travel --sort asc
📄 Limit Number of PagesBashpython main.py --keyword travel --pages 10
💾 Custom Output FileBashpython main.py --keyword travel --output travel_books.csv
📊 Output StructureConsole Analytics SummaryWhen a scrape completes, the CLI provides an instant summary:Total Matches: 12Average Price: £34.56Cheapest Book: £12.95Most Expensive: £57.83CSV SchemaThe exported data follows this structured format:Title, Price, Rating, Page🏗 Architecture OverviewCode snippetgraph TD
    A[CLI Input] --> B[BookScraper Class]
    B --> C[Session Setup w/ Retry]
    C --> D[Pagination Detection]
    D --> E[Concurrent Page Scraping]
    E --> F[Data Parsing & Cleaning]
    F --> G[Filtering & Sorting]
    G --> H[CSV Export & Logging]
Core Design BenefitsScalability: Process hundreds of items in seconds via ThreadPoolExecutor.Resilience: Built-in HTTPAdapter retry strategy for network stability.Maintainability: Strict Object-Oriented (OOP) approach for clean code.Precision: Encoding-safe parsing for currency symbols and UTF-8 characters.🔮 Future Roadmap[ ] SQLite Persistence: Move from CSV to a relational database.[ ] Category Scraping: Targeted extraction by genre.[ ] Dockerization: Containerize for easy deployment.[ ] Dashboard: Build a Streamlit UI for visual analytics.👤 AuthorNagesh AI/ML & Web Development Enthusiast Focusing on scalable system design and automation tools.⚠️ DisclaimerBuilt for educational purposes using the Books to Scrape public sandbox.