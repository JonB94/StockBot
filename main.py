import argparse
import json
import requests
import sys
from utils import ConsoleTimer, Control, SubfieldIRLs

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
    for sub in subfields:
        with ConsoleTimer(f"PULLING {company.upper()} {field.upper()} -> {sub.upper()} DATA"):
            irl = SubfieldIRLs[field][sub].replace("[COMPANY_NAME]", company)
            data[sub] = requests.get(url = f'{API_URL}/{irl}').json()
    return data

if __name__ == "__main__":
    with ConsoleTimer("EXECUTING SCRIPT"):
        main()
