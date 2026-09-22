Book_dataPipeline/
│
├── scrapping/
│   └── scraper.py              # Web scraper using BeautifulSoup
│
├── DB access/
│   └── database.py             # BookDatabaseManager OOP SQLite CRUD class
│
├── api.py                      # FastAPI REST microservice & Pydantic models
├── client.py                   # Client script: API call, Pandas CSV export, Matplotlib plot
├── run_pipeline.py             # End-to-end orchestration runner
├── requirements.txt            # Project dependencies
├── books.db                    # SQLite database (generated during run)
├── exported_books.csv          # Output CSV (generated during run)
└── price_vs_rating.png         # Output Scatter Plot (generated during run)
