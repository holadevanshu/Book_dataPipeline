# Book_dataPipeline/
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


# Execution Instructions-

# Step 1: Environment Setup
# Create and activate virtual environment
1. python -m venv venv
2. venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Step 2: Running the End-to-End Pipeline
python run_pipeline.py

# Step 3: Run uvicorn
uvicorn api:app --reload --port 8000

# Step 4: Open your browser and go to:
http://127.0.0.1:8000/docs
