import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from textblob import TextBlob
from datetime import datetime

# Function to fetch stock data and analyze sentiment
def analyze_stock(symbol):
    # Fetch stock data
    end = datetime.now()
    start = datetime(end.year - 1, end.month, end.day)
    stock_data = yf.download(symbol, start=start, end=end)
    
    # Sample sentiment analysis (replace with real-time news in future)
    sentiment = TextBlob("Sample news headline").sentiment.polarity
    
    # Display sentiment score
    st.write(f"Sentiment Score for {symbol}: {sentiment}")
    
        # Plot the stock closing prices using future-proof method
    st.write(f"Stock data for {symbol}:")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(stock_data['Close'], label='Close Price', color='skyblue')
    ax.set_title(f"Stock Prices for {symbol}")
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    st.pyplot(fig)


# Streamlit user interface
st.title("Real-Time Stock Sentiment Analyzer")

# Stock symbol input
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, MSFT, AMZN):")

# Button to trigger analysis
if st.button("Analyze"):
    if stock_symbol:
        # Clear previous outputs before new analysis
        st.empty()  # This clears any previous output
        
        # Call the function to display analysis and chart
        analyze_stock(stock_symbol.upper())  # Convert input to uppercase
    else:
        st.write("Please enter a stock symbol.")



