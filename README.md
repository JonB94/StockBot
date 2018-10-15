# StockBot


## Required Libraries
*To install all the necessary libraries at once, run the following in your terminal:*
```sh
python -m pip install -r requirements.txt
```
- **Argparse**: python -m pip install argparse
- **Requests**: python -m pip install requests


## Getting Started
The **api_requests.py** script accepts the following input arguments:
- **field**: (one input) The field of information you want to capture. Options are: Stocks ("stocks"), Reference Data ("reference"), IEX Market Data ("iexmarket"), IEX Stats ("iexstats"), Markets ("markets")
- **subfield**: (one or more inputs) The subfield of information within the field. See the References section below to know which subfield inputs are acceptable.

To execute the program, run the following line in your terminal:
```sh
python api_requests.py [STRING: field] --subfield [STRING: subfield]
```

Examples:
```sh
python api_requests.py stocks --subfield batch-requests
python api_requests.py stocks --subfield dividends earnings price
python api_requests.py reference --subfield iex-corporate-actions
python api_requests.py iexmarket --subfield tops last hist deep
```


## References
**Fields and subfields:**
- 'stocks'
    - 'batch-requests'
    - 'book'
    - 'chart'
    - 'collections'
    - 'company'
    - 'crypto'
    - 'delayed-quote'
    - 'dividends'
    - 'earnings'
    - 'earnings-today'
    - 'effective-spread'
    - 'financials'
    - 'historical-prices'
    - 'ipo-calendar'
    - 'iex-regulation-sho-threshold-securities-list'
    - 'iex-short-interest-list'
    - 'key-stats'
    - 'largest-trades
    - 'list'
    - 'response'
    - 'logo'
    - 'news'
    - 'ohlc'
    - 'open-close'
    - 'peers'
    - 'previous'
    - 'price'
    - 'quote'
    - 'relevant'
    - 'sector-performance'
    - 'splits'
    - 'time-series'
    - 'volume-by-volume'
- 'reference'
    - 'symbols'
    - 'iex-corporate-actions'
    - 'iex-dividends'
    - 'iex-next-day-ex-date'
    - 'iex-listed-symbol-dictionary'
- 'iexmarket'
    - 'tops'
    - 'last'
    - 'hist'
    - 'deep'
    - 'book'
    - 'trades'
    - 'system-event'
    - 'trading-status'
    - 'operational-halt-status'
    - 'short-sale-price-test-status'
    - 'security-event'
    - 'trade-break'
    - 'auction'
    - 'official-price'
- 'iexstats'
    - 'intraday'
    - 'recent'
    - 'records'
    - 'historical-summary'
    - 'historical-daily'
- 'markets'
    = 'market'