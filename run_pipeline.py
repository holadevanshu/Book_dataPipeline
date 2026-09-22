import sys
import time
import subprocess
import uvicorn
import threading
import importlib

# Dynamically import Scraper & Database Manager
scraper = importlib.import_module("scrapping.scraper")
db_module = importlib.import_module("DB access.database")

def run_pipeline():
    print("[1/4] Scraping first 20 books from books.toscrape.com...")
    books = scraper.scrape_books(20)
    print(f"Successfully scraped {len(books)} books.")

    print("\n[2/4] Populating SQLite database (books.db)...")
    db = db_module.BookDatabaseManager("books.db")
    
    # Clear existing data for clean execution
    with db.get_connection() as conn:
        conn.cursor().execute("DELETE FROM books")
        conn.commit()

    for b in books:
        db.create_book(b["title"], b["price"], b["in_stock"], b["rating"])
    print("Database populated successfully.")

    print("\n[3/4] Starting FastAPI Server...")
    config = uvicorn.Config("api:app", host="127.0.0.1", port=8000, log_level="error")
    server = uvicorn.Server(config)
    server_thread = threading.Thread(target=server.run, daemon=True)
    server_thread.start()
    
    # Wait briefly for FastAPI to bind
    time.sleep(2)

    print("\n[4/4] Executing client.py data retrieval, export, and plotting...")
    # FIX: Use sys.executable instead of hardcoded "python"
    subprocess.run([sys.executable, "client.py"], check=True)
    print("\nPipeline execution completed successfully!")

if __name__ == "__main__":
    run_pipeline()