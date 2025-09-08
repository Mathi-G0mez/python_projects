import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books(pages=1):
    books_data = []

    for page in range(1, pages + 1):
        url = BASE_URL.format(page)
        response = requests.get(url)
        
        if response.status_code != 200:
            messagebox.showerror("Error", f"Failed to fetch page {page}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title = article.h3.a["title"]
            price = article.find("p", class_="price_color").text.strip()
            rating = article.p["class"][1]  # Example: "Three", "Four"
            availability = article.find("p", class_="instock availability").text.strip()

            books_data.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability
            })

    return books_data

def run_scraper():
    try:
        pages = int(pages_entry.get())
        if pages <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of pages.")
        return

    books = scrape_books(pages)
    
    if not books:
        messagebox.showwarning("No Data", "No books were scraped.")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if save_path:
        df = pd.DataFrame(books)
        df.to_csv(save_path, index=False)
        messagebox.showinfo("Success", f"Books saved to {save_path}")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Book Store Web Scraper")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="Enter number of pages to scrape:", font=("Arial", 12)).pack(pady=10)
pages_entry = tk.Entry(root, width=10, font=("Arial", 12))
pages_entry.pack(pady=5)

tk.Button(root, text="Start Scraping", font=("Arial", 12), command=run_scraper).pack(pady=20)

tk.Label(root, text="Scrapes book title, price, rating, and availability.", font=("Arial", 10), fg="gray").pack(pady=10)

root.mainloop()
