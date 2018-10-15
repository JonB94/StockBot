# libraries
import argparse
import json
import requests
import sys
from performance.consoletimer import consoletimer


# constants
VERSION = 1.0
API_URL = 'https://api.iextrading.com/%s' % VERSION
FILENAME = 'data.json'


# dictionary of IRLs for each subfield
# documentation: https://iextrading.com/developer/docs/
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


# reading inputs
parser = argparse.ArgumentParser()
parser.add_argument('field', help = 'The field of information you want to capture. Options are: \
                    Stocks ("stocks"), Reference Data ("reference"), IEX Market Data ("iexmarket"), \
                    IEX Stats ("iexstats"), Markets ("markets")')
parser.add_argument('-s', '--subfield', help = 'The subfield of the primary field.', nargs='+')


# main
def main():
    args = parser.parse_args()
    field = args.field
    subfields = args.subfield
    data = {}

    # verifies that inputs are valid
    if field not in SUBFIELDS_IRL_DICT:
        print('Error: invalid field')
        sys.exit(0)
    
    for sf in subfields:
        if not sf in SUBFIELDS_IRL_DICT[field]:
            print('Error: invalid subfield.')
            sys.exit(0)
    
    # extracts data from API
    with consoletimer('RETRIEVING DATA FROM FIELDS %s' % subfields):
        for sub in subfields:
            data[sub] = get_request(sub, SUBFIELDS_IRL_DICT[field][sub])
    
    with consoletimer('WRITING TO OUTPUT FILE "%s"' % FILENAME):
        f = open(FILENAME, "w")
        f.write(json.dumps(data, indent=4))


def get_request(field, irl):
    with consoletimer("RETRIEVING %s" % field):
        r = requests.get(url = '%s/%s' % (API_URL, irl))
        return r.json()

# execute
if __name__ == '__main__':
    with consoletimer('EXECUTE SCRIPT'):
        main()