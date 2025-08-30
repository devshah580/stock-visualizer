import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


#Input ticker
#ticker_symbol = input("Enter ticker: ").upper()
ticker_symbol = "AAPL"
ticker = yf.Ticker(ticker_symbol)


#Get 1-year historical data
historical_data = ticker.history(period="1y")
current_price = ticker.info['currentPrice']
print(f"Current Price of {ticker_symbol}: {current_price}")


#Plot the stock closing price
fig, ax1 = plt.subplots()
p1, = ax1.plot(historical_data.index, historical_data['Close'], label="Close Price")

ax1.set_title("Stock Price History for " + ticker_symbol)
ax1.set_xlabel("Date")
ax1.set_ylabel("Price($)")

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %Y'))
ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
ax1.xaxis.set_minor_locator(mdates.WeekdayLocator())
plt.xticks(rotation=45)


#Plot the 30-day moving average
p2, = ax1.plot(historical_data.index, historical_data['Close'].rolling(30).mean(), label="30-Day Moving Avg")


#Plot the volume
ax2 = ax1.twinx()
p3 = ax2.bar(historical_data.index, historical_data['Volume'], label="Volume", alpha=0.45)
ax2.set_ylabel("Volume")

graphs = [p1, p2, p3]
labels = [l.get_label() for l in graphs]


#show the graph
plt.grid(True)
plt.legend(graphs, labels)
plt.tight_layout()

plt.show()

