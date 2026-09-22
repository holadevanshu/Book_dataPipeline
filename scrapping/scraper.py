import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any

URL = "https://books.toscrape.com/"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def scrape_books(limit: int = 20) -> List[Dict[str, Any]]:
    """
    Scrapes the first `limit` books from https://books.toscrape.com/
    Extracts: Title, Price (float), In Stock (bool), Rating (int 1-5).
    """
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    book_elements = soup.select("article.product_pod")[:limit]
    
    books = []
    for pod in book_elements:
        # 1. Title
        title_el = pod.select_one("h3 a")
        title = title_el["title"] if title_el and "title" in title_el.attrs else title_el.text.strip()
        
        # 2. Price
        price_text = pod.select_one("p.price_color").text.strip()
        price = float(price_text.replace("£", "").replace("Â", ""))
        
        # 3. In Stock
        availability_text = pod.select_one("p.instock.availability").text.strip()
        in_stock = "In stock" in availability_text
        
        # 4. Rating
        rating_class = pod.select_one("p.star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_MAP.get(rating_word, 0)
        
        books.append({
            "title": title,
            "price": price,
            "in_stock": in_stock,
            "rating": rating
        })
        
    return books

if __name__ == "__main__":
    scraped = scrape_books(20)
    print(f"Scraped {len(scraped)} books successfully.")
    for b in scraped[:3]:
        print(b)