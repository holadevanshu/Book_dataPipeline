import requests
import pandas as pd
import matplotlib.pyplot as plt

API_URL = "http://127.0.0.1:8000/books"

def main():
    # 1. Fetch data from REST API using requests
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    data = response.json()

    # 2. Load into Pandas DataFrame
    df = pd.DataFrame(data)
    
    print("=" * 60)
    print("RETRIEVED BOOK DATA (PANDAS DATAFRAME):")
    print("=" * 60)
    print(df.to_string(index=False))
    print("=" * 60)

    # 3. Export DataFrame to CSV
    csv_filename = "exported_books.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Data successfully exported to {csv_filename}")

    # 4. Data Visualization — Scatter Plot (Price vs Rating)
    plt.figure(figsize=(10, 6))
    plt.scatter(df["price"], df["rating"], color="blue", alpha=0.7, edgecolors="k", s=80)
    
    plt.title("Book Price vs. Star Rating", fontsize=14, fontweight="bold")
    plt.xlabel("Price (£)", fontsize=12)
    plt.ylabel("Rating (1-5 Stars)", fontsize=12)
    plt.yticks([1, 2, 3, 4, 5])
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    chart_filename = "price_vs_rating.png"
    plt.savefig(chart_filename, dpi=300)
    plt.close()
    print(f"Scatter plot visualization saved to {chart_filename}")

if __name__ == "__main__":
    main()