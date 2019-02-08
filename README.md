# StockBot
>*--Version 1.1.0--*
> - User can now select as many fields and as many subfields as desired.
> - New control file allows for easy usability (see "Control File" section below).
> - Added control.py to utils module to handle user settings.
> - Deprecated api_requests.py.

StockBot is a bot designed to recommend the best stock investments based on live stock market data and machine learning.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See Operation for notes on how to deploy the project on a live system.

**Prerequisites**  
Please install [Python version 3.6 or above](https://www.python.org/downloads/release/python-360/).


**Installing**  
Use [Git](https://git-scm.com/) (or a similar version control system) to clone the code to your local machine by entering the following command into your terminal:
```bash
git clone git@github.com:JonB94/StockBot.git
```

*NOTE*: Before continuing, it is recommended that you set up a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to avoid overwriting your currently installed libraries.

Then use a Python package manager ([pip](https://pypi.org/project/pip/) is recommended) to install the required libraries by running the following in your terminal:
```bash
python -m pip install -r requirements.txt
```

 Alternatively, you can install the following required libraries individually:
- [requests (v. 2.20.0)](http://docs.python-requests.org/en/master/) - allows you to send organic, grass-fed HTTP/1.1 requests, without the need for manual labor
- [tensorflow (v. 1.11.0)](https://www.tensorflow.org/) - An open source machine learning framework for everyone.


## Operation
**Inputs**  
The **main.py** script accepts the following input arguments:
- **-r** or **--read-control**: defaults to "control_file.json"; filename for the user control file that allows you to specify which data to pull
- **-o, --output**: defaults to "data.json"; filename for the output file that will store all of the output data from the script

**Control File**  
The control file allows a user to configure what type of information to pull. Each option can be set to "1" for "PULL" and "0" for "NO PULL". By default, the program comes with a sample control file called "control_file.json".

**Executing**  
Use the following examples to run the program:
```bash

// Template:
python main.py [-h] [-r READ_CONTROL] [-o OUTPUT]

// Example with user arguments:
python main.py -r control_file.json -o data.json

// Example with no arguments; will run default values:
python main.py
```

## Built With

- [IEX Developer Platform](https://iextrading.com/developer/) - The free IEX API is built on a proven, high-performance system, and drives many of the applications used within IEX.
- [Tensorflow](https://www.tensorflow.org/) - An open source machine learning framework for everyone.

## Authors

- **Jon Bolles**: [GitHub](https://github.com/JonB94)
- **Syihan Muhammad**: [GitHub](https://github.com/Syihan) | [Website](http://syihan.com)

---
># Deprecated
>*--v. 1.0.0--*
>*The following information has been deprecated, but is still preserved for posterity. Please only review for reference.*
>
> ## Operation
>The **api_requests.py** script accepts the following input arguments:
>- **output_file**: (zero or one input) The output file to push the extracted data to.
>- **-f** or **--field**: (one input) The field of information you want to capture. Options are: Stocks ("stocks"), Reference Data ("reference"), IEX Market Data ("iexmarket"), IEX Stats ("iexstats"), Markets ("markets")
>- **-s** or **--subfield**: (one or more inputs) The subfield of information within the field. See the References section below to know which subfield inputs are acceptable.
>
>To execute the program, run the following line in your terminal:
>```sh
>python api_requests.py [output_file] [-h] [-f FIELD] [-s SUBFIELDS [SUBFIELDS ...]]
>```
>
>Examples:
>```sh
>python api_requests.py batchrequests.json --field stocks --subfield batch-requests
>```
>```sh
>python api_requests.py batchrequests.json -f stocks -s batch-requests
>```
>```sh
>python api_requests.py --field stocks --subfield dividends earnings price
>```
>```sh
>python api_requests.py -f reference --subfield iex-corporate-actions
>```
>```sh
>python api_requests.py marketdata.json -f iexmarket -s tops last hist deep
>```
>
>## References
>**Fields and subfields:**
>- 'stocks'
>    - 'batch-requests'
>    - 'book'
>    - 'chart'
>    - 'collections'
>    - 'company'
>    - 'crypto'
>    - 'delayed-quote'
>    - 'dividends'
>    - 'earnings'
>    - 'earnings-today'
>    - 'effective-spread'
>    - 'financials'
>    - 'historical-prices'
>    - 'ipo-calendar'
>    - 'iex-regulation-sho-threshold-securities-list'
>    - 'iex-short-interest-list'
>    - 'key-stats'
>    - 'largest-trades
>    - 'list'
>    - 'response'
>    - 'logo'
>    - 'news'
>    - 'ohlc'
>    - 'open-close'
>    - 'peers'
>    - 'previous'
>    - 'price'
>    - 'quote'
>    - 'relevant'
>    - 'sector-performance'
>    - 'splits'
>    - 'time-series'
>    - 'volume-by-volume'
>- 'reference'
>    - 'symbols'
>    - 'iex-corporate-actions'
>    - 'iex-dividends'
>    - 'iex-next-day-ex-date'
>    - 'iex-listed-symbol-dictionary'
>- 'iexmarket'
>    - 'tops'
>    - 'last'
>    - 'hist'
>    - 'deep'
>    - 'book'
>    - 'trades'
>    - 'system-event'
>    - 'trading-status'
>    - 'operational-halt-status'
>    - 'short-sale-price-test-status'
>    - 'security-event'
>    - 'trade-break'
>    - 'auction'
>    - 'official-price'
>- 'iexstats'
>    - 'intraday'
>    - 'recent'
>    - 'records'
>    - 'historical-summary'
>    - 'historical-daily'
>- 'markets'
>    - 'market'
