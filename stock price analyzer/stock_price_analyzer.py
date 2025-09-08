import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, filedialog

def fetch_and_plot():
    symbol = symbol_entry.get().strip()
    period = period_entry.get().strip()
    
    if not symbol:
        messagebox.showerror("Error", "Please enter a stock symbol.")
        return

    try:
        # Fetch stock data
        stock = yf.Ticker(symbol)
        df = stock.history(period=period)
        
        if df.empty:
            messagebox.showwarning("No Data", f"No data found for {symbol}.")
            return

        # Save CSV
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if save_path:
            df.to_csv(save_path)
        
        # Plot graph
        plt.figure(figsize=(10, 6))
        plt.plot(df.index, df["Close"], label="Closing Price", color="blue")
        plt.plot(df.index, df["Close"].rolling(20).mean(), label="20-day MA", color="orange")
        plt.plot(df.index, df["Close"].rolling(50).mean(), label="50-day MA", color="green")
        
        plt.title(f"{symbol} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Stock Price Analyzer")
root.geometry("400x250")
root.resizable(False, False)

tk.Label(root, text="Enter Stock Symbol (e.g. AAPL, TSLA, INFY.NS):", font=("Arial", 11)).pack(pady=5)
symbol_entry = tk.Entry(root, width=20, font=("Arial", 12))
symbol_entry.pack(pady=5)

tk.Label(root, text="Enter Period (e.g. 1mo, 3mo, 6mo, 1y, max):", font=("Arial", 11)).pack(pady=5)
period_entry = tk.Entry(root, width=10, font=("Arial", 12))
period_entry.insert(0, "6mo")
period_entry.pack(pady=5)

tk.Button(root, text="Analyze Stock", font=("Arial", 12), command=fetch_and_plot).pack(pady=20)

tk.Label(root, text="Fetches stock data, plots graph & moving averages.", font=("Arial", 10), fg="gray").pack(pady=5)

root.mainloop()
