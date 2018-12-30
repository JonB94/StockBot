# StockBot
StockBot is a bot designed to recommend the best stock investments based on live stock market data and machine learning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See Operation for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:
- Python (version 3 or above)


### Installing

Use the package manager [pip](https://pypi.org/project/pip/) to install the following Python packages:
- [argparse](https://docs.python.org/3/library/argparse.html) - The argparse module makes it easy to write user-friendly command-line interfaces.
- [requests](http://docs.python-requests.org/en/master/) - allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor
- [tensorflow](https://www.tensorflow.org/) - An open source machine learning framework for everyone.

You can install each package individually or you can run the following in your terminal:
```
python -m pip install -r requirements.txt
```


## Operation
The **api_requests.py** script accepts the following input arguments:
- **output_file**: (zero or one input) The output file to push the extracted data to.
- **-f** or **--field**: (one input) The field of information you want to capture. Options are: Stocks ("stocks"), Reference Data ("reference"), IEX Market Data ("iexmarket"), IEX Stats ("iexstats"), Markets ("markets")
- **-s** or **--subfield**: (one or more inputs) The subfield of information within the field. See the References section below to know which subfield inputs are acceptable.

To execute the program, run the following line in your terminal:
```sh
python api_requests.py [output_file] [-h] [-f FIELD] [-s SUBFIELDS [SUBFIELDS ...]]
```

Examples:
```sh
python api_requests.py batchrequests.json --field stocks --subfield batch-requests
```
```sh
python api_requests.py batchrequests.json -f stocks -s batch-requests
```
```sh
python api_requests.py --field stocks --subfield dividends earnings price
```
```sh
python api_requests.py -f reference --subfield iex-corporate-actions
```
```sh
python api_requests.py marketdata.json -f iexmarket -s tops last hist deep
```

## Built With

- [IEX Developer Platform](https://iextrading.com/developer/) - The free IEX API is built on a proven, high-performance system, and drives many of the applications used within IEX.
- [Tensorflow](https://www.tensorflow.org/) - An open source machine learning framework for everyone.

## Authors

- **Jon Bolles**: [GitHub](https://github.com/JonB94)
- **Syihan Muhammad**: [GitHub](https://github.com/Syihan) | [Website](http://syihan.com)


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
    - 'market'
