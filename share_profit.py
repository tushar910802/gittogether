import yfinance as yf

# Predefined list of shares (you can expand this as needed)
share_list = {
    "AAPL": "Apple Inc.",
    "TSLA": "Tesla, Inc.",
    "MSFT": "Microsoft Corporation",
    "AMZN": "Amazon.com, Inc.",
    "GOOGL": "Alphabet Inc. (Google)",
    "META": "Meta Platforms, Inc. (Facebook)"
}

def display_share_list():
    print("\nAvailable Shares:")
    for ticker, name in share_list.items():
        print(f"{ticker}: {name}")

def get_share_profitability(stock1, stock2, base_price):
    try:
        # Fetch current stock prices
        stock1_data = yf.Ticker(stock1)
        stock2_data = yf.Ticker(stock2)

        stock1_price = stock1_data.history(period="1d")['Close'].iloc[-1]
        stock2_price = stock2_data.history(period="1d")['Close'].iloc[-1]

        # Calculate profit percentages
        stock1_profit_percent = ((stock1_price - base_price) / base_price) * 100
        stock2_profit_percent = ((stock2_price - base_price) / base_price) * 100

        # Determine profitability or loss with current prices
        if stock1_price == base_price:
            stock1_result = (f"{stock1} ({share_list.get(stock1, 'Unknown')}): Current Price = ${stock1_price:.2f}, "
                             "No Profit, No Loss.")
        else:
            stock1_result = (f"{stock1} ({share_list.get(stock1, 'Unknown')}): Current Price = ${stock1_price:.2f}, "
                             f"{'Profit' if stock1_profit_percent >= 0 else 'Loss'} = {abs(stock1_profit_percent):.2f}%.")

        if stock2_price == base_price:
            stock2_result = (f"{stock2} ({share_list.get(stock2, 'Unknown')}): Current Price = ${stock2_price:.2f}, "
                             "No Profit, No Loss.")
        else:
            stock2_result = (f"{stock2} ({share_list.get(stock2, 'Unknown')}): Current Price = ${stock2_price:.2f}, "
                             f"{'Profit' if stock2_profit_percent >= 0 else 'Loss'} = {abs(stock2_profit_percent):.2f}%.")

        # Determine the more profitable stock
        if stock1_profit_percent > stock2_profit_percent:
            result = f"{stock1} ({share_list.get(stock1, 'Unknown')}) is more profitable."
        elif stock1_profit_percent < stock2_profit_percent:
            result = f"{stock2} ({share_list.get(stock2, 'Unknown')}) is more profitable."
        else:
            result = "Both shares have the same profitability."

        return f"{stock1_result}\n{stock2_result}\n\n{result}"
    except Exception as e:
        return f"An error occurred: {e}"

# Display share list
display_share_list()

# Input parameters
stock1 = input("\nEnter the ticker symbol for Share 1: ").upper()
stock2 = input("Enter the ticker symbol for Share 2: ").upper()
base_price = float(input("Enter the base/investment price: "))

# Get profitability result
result = get_share_profitability(stock1, stock2, base_price)
print(result)
