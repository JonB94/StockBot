import argparse
import json
import requests
import sys
from utils import ConsoleTimer, Control

# Constants
VERSION = 1.0
API_URL = f'https://api.iextrading.com/{VERSION}'
CONTROL_FILE_DEFAULT = "control_file.json"
OUTPUT_FILE_DEFAULT = 'data.json'

# Argparse settings
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--read-control", type=str, help="the user control file", default=CONTROL_FILE_DEFAULT)
parser.add_argument("-o", "--output", type=str, help="the output file", default=OUTPUT_FILE_DEFAULT)
args = parser.parse_args()

def main():
    """
    Main method.
    """

    with ConsoleTimer("LOADING USER CONTROL FILE"):
        control = Control(args.read_control)

    with ConsoleTimer("PULLING DATA FROM WEB API"):
        data = {}
        for company in control.get_companies():
            data[company] = {}
            for field in control.get_fields():
                data[company][field] = update(company=company, field=field, subfields=control.get_requests(field))

    with ConsoleTimer(f"OUTPUTTING DATA TO FILE \"{args.output.upper()}\""):
        f = open(args.output, "w+")
        f.write(json.dumps(data, indent=4))

def update(company: str, field: str, subfields: list):
    """
    Pulls the latest update from the Web API.
    
    Arguments:
        company {str} -- the NASDAQ name of the company
        field {str} -- the field from which data will be pulled from
        subfields {list} -- list of subfields from which data will be pulled from
    
    Returns:
        {dict} -- dictionary of all of the data pulled from the Web API
    """

    data = {}
    subfield_irls = {
        "stocks": {
            "batch-requests": f"/stock/{company}/batch?types=quote,news,chart&range=1m&last=1",
            "book": f"/stock/{company}/book",
            "chart": f"/stock/{company}/chart",
            "collections": f"/stock/market/collection/sector?collectionName=Health%20Care",
            "company": f"/stock/{company}/company",
            "crypto": f"/stock/market/crypto",
            "delayed-quote": f"/stock/{company}/delayed-quote",
            "dividends": f"/stock/{company}/dividends/5y",
            "earnings": f"/stock/{company}/earnings",
            "earnings-today": f"/stock/market/today-earnings",
            "effective-spread": f"/stock/{company}/effective-spread",
            "financials": f"/stock/{company}/financials",
            "historical-prices": f"/stock/{company}/chart",
            "ipo-calendar": f"/stock/market/upcoming-ipos",
            "iex-regulation-sho-threshold-securities-list": f"/stock/market/threshold-securities",
            "iex-short-interest-list": f"/stock/ziext/short-interest",
            "key-stats": f"/stock/{company}/stats",
            "largest-trades": f"/stock/{company}/largest-trades",
            "list": f"/stock/market/list/mostactive",
            "response": f"/stock/{company}/quote",
            "logo": f"/stock/{company}/logo",
            "news": f"/stock/{company}/news",
            "ohlc": f"/stock/{company}/ohlc",
            "open-close": f"/stock/{company}/ohlc",
            "peers": f"/stock/{company}/peers",
            "previous": f"/stock/{company}/previous",
            "price": f"/stock/{company}/price",
            "quote": f"/stock/{company}/quote",
            "relevant": f"/stock/{company}/relevant",
            "sector-performance": f"/stock/market/sector-performance",
            "splits": f"/stock/{company}/splits/5y",
            "time-series": f"/stock/{company}/time-series",
            "volume-by-volume": f"/stock/{company}/volume-by-venue"
        },
        "reference": {
            "symbols": f"/ref-data/symbols",
            "iex-corporate-actions": f"/ref-data/daily-list/corporate-actions",
            "iex-dividends": f"/ref-data/daily-list/dividends",
            "iex-next-day-ex-date": f"/ref-data/daily-list/next-day-ex-date",
            "iex-listed-symbol-dictionary": f"/ref-data/daily-list/symbol-directory"
        },
        "iexmarket": {
            "tops": f"/tops",
            "last": f"/tops/last",
            "hist": f"/hist?date=20170515",
            "deep": f"/deep?symbols={company}",
            "book": f"/deep/book?symbols=yelp",
            "trades": f"/deep/trades?symbols={company}",
            "system-event": f"/deep/system-event",
            "trading-status": f"/deep/trading-status?symbols={company}",
            "operational-halt-status": f"/deep/op-halt-status?symbols={company}",
            "short-sale-price-test-status": f"/deep/ssr-status?symbols={company}",
            "security-event": f"/deep/security-event?symbols={company}",
            "trade-break": f"/deep/trade-breaks?symbols={company}",
            "auction": f"/deep/auction?symbols=ziext",
            "official-price": f"/deep/official-price?symbols={company}"
        },
        "iexstats": {
            "intraday": f"/stats/intraday",
            "recent": f"/stats/recent",
            "records": f"/stats/records",
            "historical-summary": f"/stats/historical",
            "historical-daily": f"/stats/historical/daily"
        },
        "markets": {
            "market": f"/market"
        }
    }

    for sub in subfields:
        with ConsoleTimer(f"PULLING {company.upper()} {field.upper()} -> {sub.upper()} DATA"):
            data[sub] = requests.get(url = f'{API_URL}/{subfield_irls[field][sub]}').json()
    
    return data

if __name__ == "__main__":

    with ConsoleTimer("EXECUTING SCRIPT"):
        main()
