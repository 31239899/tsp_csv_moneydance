
# Description

This is a script to scrape TSP fund prices from tsp.gov and save to JSON or
[Moneydance](https://infinitekind.com/moneydance)-friendly CSV format. It was
inspired by the [script by
mysteriousclam](https://www.bogleheads.org/forum/viewtopic.php?p=6801854#p6801854)
on the bogleheads.org forums.

To keep things simple, the CSV/JSON files are written to the current working
directory.

# Usage

Just run the script: `python tsp_csv_moneydance.py`

Run with `--json` to get JSON output instead of CSV.

**WARNING:** This script will overwrite JSON and CSV files with each run.

# Requirements

* Python 3.6+
* `requests` package
