import argparse
import json
import requests
import sys

from utils import ConsoleTimer as consoletimer

# Constants
VERSION = 1.0
API_URL = f'https://api.iextrading.com/{VERSION}'
FILENAME_DEFAULT = 'data.json'

# Dictionary of IRLs for each subfield
# Documentation: https://iextrading.com/developer/docs/
SUBFIELDS_IRL_DICT = {                                                                          # FLAGGED '1' IF IRL HAS ADDITIONAL ARGUMENTS
    'stocks': {
        'batch-requests': '/stock/aapl/batch?types=quote,news,chart&range=1m&last=1',           # 1
        'book': '/stock/aapl/book',                                                             # 1
        'chart': '/stock/aapl/chart',                                                           # 1
        'collections': '/stock/market/collection/sector?collectionName=Health%20Care',          # 1
        'company': '/stock/aapl/company',
        'crypto': '/stock/market/crypto',
        'delayed-quote': '/stock/aapl/delayed-quote',
        'dividends': '/stock/aapl/dividends/5y',                                                # 1
        'earnings': '/stock/aapl/earnings',
        'earnings-today': '/stock/market/today-earnings',
        'effective-spread': '/stock/aapl/effective-spread',
        'financials': '/stock/aapl/financials',                                                 # 1
        'historical-prices': '/stock/aapl/chart',                                               # 1 NOTE: Same as subfield 'chart'
        'ipo-calendar': '/stock/market/upcoming-ipos',                                          # 1
        'iex-regulation-sho-threshold-securities-list': '/stock/market/threshold-securities',   # 1
        'iex-short-interest-list': '/stock/ziext/short-interest',                               # 1
        'key-stats': '/stock/aapl/stats',
        'largest-trades': '/stock/aapl/largest-trades',
        'list': '/stock/market/list/mostactive',                                                # 1
        'response': '/stock/aapl/quote',                                                        #   NOTE: Same as subfield 'quote'
        'logo': '/stock/aapl/logo',
        'news': '/stock/aapl/news',                                                             # 1
        'ohlc': '/stock/aapl/ohlc',                                                             # 1
        'open-close': '/stock/aapl/ohlc',                                                       #   NOTE: Same as subfield 'ohlc'
        'peers': '/stock/aapl/peers',
        'previous': '/stock/aapl/previous',                                                     # 1
        'price': '/stock/aapl/price',
        'quote': '/stock/aapl/quote',
        'relevant': '/stock/aapl/relevant',
        'sector-performance': '/stock/market/sector-performance',
        'splits': '/stock/aapl/splits/5y',                                                      # 1
        'time-series': '/stock/aapl/time-series',
        'volume-by-volume': '/stock/aapl/volume-by-venue'
    },
    'reference': {
        'symbols': '/ref-data/symbols',
        'iex-corporate-actions': '/ref-data/daily-list/corporate-actions',                      # 1
        'iex-dividends': '/ref-data/daily-list/dividends',                                      # 1
        'iex-next-day-ex-date': '/ref-data/daily-list/next-day-ex-date',                        # 1
        'iex-listed-symbol-dictionary': '/ref-data/daily-list/symbol-directory'                 # 1
    },
    'iexmarket': {
        'tops': '/tops',                                                                        # 1
        'last': '/tops/last',                                                                   # 1
        'hist': '/hist?date=20170515',                                                          # 1
        'deep': '/deep?symbols=snap',
        'book': '/deep/book?symbols=yelp',
        'trades': '/deep/trades?symbols=snap',
        'system-event': '/deep/system-event',
        'trading-status': '/deep/trading-status?symbols=snap',
        'operational-halt-status': '/deep/op-halt-status?symbols=snap',
        'short-sale-price-test-status': '/deep/ssr-status?symbols=snap',
        'security-event': '/deep/security-event?symbols=snap',
        'trade-break': '/deep/trade-breaks?symbols=snap',
        'auction': '/deep/auction?symbols=ziext',
        'official-price': '/deep/official-price?symbols=snap'
    },
    'iexstats': {
        'intraday': '/stats/intraday',
        'recent': '/stats/recent',
        'records': '/stats/records',
        'historical-summary': '/stats/historical',                                              # 1
        'historical-daily': '/stats/historical/daily'                                           # 1
    },
    'markets': {
        'market': '/market'
    }
}

# Read user inputs.
parser = argparse.ArgumentParser()
parser.add_argument('output_file', type=str, default=FILENAME_DEFAULT, help= 'The output file to push the extracted data to.', nargs='?')
parser.add_argument('-f', '--field', type=str, help = 'The field of information you want to capture. Options are: \
                    Stocks ("stocks"), Reference Data ("reference"), IEX Market Data ("iexmarket"), \
                    IEX Stats ("iexstats"), Markets ("markets")')
parser.add_argument('-s', '--subfields', type=str, help = 'The subfield of the primary field. Please see README.md for all available subfields', nargs='+')

def main():
    """
    Main method
    """
    args = parser.parse_args()
    filename = args.output_file
    field = args.field
    subfields = args.subfields
    data = {}

    # Verifies valid output file name.
    if not filename.endswith('.json'):
        print('Error: invalid output file. Must be a .json')
        sys.exit(0)

    # Verifies that field inputs are valid.
    if field not in SUBFIELDS_IRL_DICT:
        print(f'Error: invalid field "{field}"')
        sys.exit(0)

    # Iterates through subfields.
    for sf in subfields:
        # Verifies that subfield inputs are valid.
        if sf not in SUBFIELDS_IRL_DICT[field]:
            print(f'Error: invalid subfield "{sf}".')
            sys.exit(0)
        # Extracts data from API.
        else:
            with consoletimer(f'RETRIEVING \'{sf.upper()}\' DATA'):
                data[sf] = requests.get(url = f'{API_URL}/{SUBFIELDS_IRL_DICT[field][sf]}').json()
    
    # Outputs JSON to file.
    with consoletimer(f'WRITING TO OUTPUT FILE \'{filename}\''):
        f = open(filename, "w+")
        f.write(json.dumps(data, indent=4))

# Execute the main method.
if __name__ == '__main__':
    with consoletimer('EXECUTING SCRIPT'):
        main()
