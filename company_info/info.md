| Category                   | Feature Examples                                                                                   | Source                  | Python Library/API                                      |
| -------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------- |
| **Price Data**             | Open, High, Low, Close, Volume, Adj Close                                                          | Yahoo Finance           | `yfinance`                                              |
| **Technical Indicators**   | SMA, EMA, RSI, MACD, Bollinger Bands, ATR, OBV, VWAP, MFI, Stochastic RSI, ADX, CCI, ROC, Momentum | Calculate yourself      | `pandas`, `numpy` (or `pandas-ta` later for validation) |
| **Returns**                | Daily, Weekly, Monthly, Log Returns                                                                | Price Data              | `pandas`                                                |
| **Volatility**             | Rolling Std, ATR, Beta, Historical Volatility                                                      | Price Data              | `pandas`, `numpy`                                       |
| **Company Profile**        | Sector, Industry, Market Cap, Employees, Country                                                   | Yahoo Finance           | `yfinance`                                              |
| **Financial Statements**   | Revenue, Net Income, EPS, Assets, Liabilities, Cash Flow                                           | Financial Modeling Prep | `requests`                                              |
| **Financial Ratios**       | PE, PB, PEG, ROE, ROCE, Debt-to-Equity, Current Ratio, Quick Ratio, Profit Margin                  | Financial Modeling Prep | `requests`                                              |
| **Macroeconomic**          | Interest Rate, Inflation, GDP, Unemployment, CPI                                                   | FRED                    | `fredapi`                                               |
| **Commodity Prices**       | Gold, Silver, Oil, Natural Gas                                                                     | Yahoo Finance           | `yfinance`                                              |
| **Currency**               | USD Index, USD/INR, EUR/USD                                                                        | Yahoo Finance           | `yfinance`                                              |
| **Market Indices**         | S&P 500, NASDAQ, NIFTY, SENSEX                                                                     | Yahoo Finance           | `yfinance`                                              |
| **Market Volatility**      | VIX                                                                                                | Yahoo Finance           | `yfinance`                                              |
| **News**                   | Headlines, Article Text, Publish Time                                                              | NewsAPI                 | `newsapi-python` or `requests`                          |
| **News Sentiment**         | Positive/Negative/Neutral Score                                                                    | Compute yourself        | `transformers` (FinBERT)                                |
| **Analyst Ratings**        | Buy/Hold/Sell                                                                                      | Finnhub                 | `requests`                                              |
| **Earnings Calendar**      | Earnings Date, Surprise %, EPS Estimate                                                            | Finnhub                 | `requests`                                              |
| **Insider Trading**        | Insider Buy/Sell                                                                                   | SEC EDGAR/OpenInsider   | `requests`                                              |
| **Institutional Holdings** | Mutual Funds, Hedge Funds                                                                          | SEC 13F                 | `requests`                                              |


--------------------------------------------------------------------------------------------------------------------------------------------------

# Ticker methods


| Code                  | Returns                                                           |
| --------------------- | ----------------------------------------------------------------- |
| `stock.history()`     | Historical OHLCV price data                                       |
| `stock.info`          | Company information                                               |
| `stock.balance_sheet` | Balance sheet                                                     |
| `stock.financials`    | Income statement                                                  |
| `stock.cashflow`      | Cash flow statement                                               |
| `stock.dividends`     | Dividend history                                                  |
| `stock.splits`        | Stock split history                                               |
| `stock.news`          | Recent news (availability depends on the version and data source) |
