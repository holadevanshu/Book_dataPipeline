Book_dataPipeline/
1. scrapping/
   scraper.py                  # Web scraper using BeautifulSoup
3. DB access/
   database.py                 # BookDatabaseManager OOP SQLite CRUD class
4. api.py                      # FastAPI REST microservice & Pydantic models
5. client.py                   # Client script: API call, Pandas CSV export, Matplotlib plot
6. run_pipeline.py             # End-to-end orchestration runner
7. requirements.txt            # Project dependencies
8. books.db                    # SQLite database (generated during run)
9. exported_books.csv          # Output CSV (generated during run)
10. price_vs_rating.png         # Output Scatter Plot (generated during run)
