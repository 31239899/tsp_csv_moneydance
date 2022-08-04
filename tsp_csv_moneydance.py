#!/usr/bin/env python

# script to scrape TSP fund prices from tsp.gov
#
# Inspired by the script by mysteriousclam on bogleheads.org.
# https://www.bogleheads.org/forum/viewtopic.php?p=6801854#p6801854
#
# Run with `--json` to get JSON output instead of CSV
#
# REQUIRES: Python 3.6+ and the `requests` package
#
# WARNING: this script will overwrite JSON and CSV files with each run


import csv
import datetime
import json
import requests
import sys
from collections import defaultdict


url = 'https://www.tsp.gov/data/fund-price-history.csv'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}

page = requests.get(url, headers=headers)

reader = csv.DictReader(page.text.splitlines())

price_data = defaultdict(dict)

for row in reader:
    try:
        date = datetime.datetime.strptime(row['Date'], '%Y-%m-%d').strftime('%m/%d/%Y')
    except Exception:
        # skip rows with no/bad date
        continue
    del row['Date']

    for tag, price in row.items():
        # don't add date entry if there is no price
        if price:
            price_data[tag][date] = price

# write json
if len(sys.argv) > 1 and sys.argv[1] == '--json':
    filename = 'tsp_prices.json'
    with open(filename, 'w') as fout:
        json.dump(price_data, fout, indent=4)
    print(f'Prices written to "{filename}"')
    sys.exit()

# write csv
header = ['Date', 'High', 'Low', 'Close', 'Volume']
for tag, prices in price_data.items():
    filename = f'{tag}.csv'
    with open(filename, 'w') as fout:
        writer = csv.writer(fout)
        writer.writerow(header)
        for date, price in prices.items():
            writer.writerow([date, price, price, price, 0])
    print(f'Prices written to "{filename}"')
