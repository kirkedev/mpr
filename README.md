mpr
===
[![Build Status](https://travis-ci.com/gumballhead/mpr.svg?branch=master)](https://travis-ci.com/gumballhead/mpr)
[![Coverage Status](https://coveralls.io/repos/github/gumballhead/mpr/badge.svg?branch=master)](https://coveralls.io/github/gumballhead/mpr?branch=master)

Python package for downloading, parsing, and analyzing historical [Mandatory Price Reporting](https://mpr.datamart.ams.usda.gov/) data from the USDA's [Agricultural Marketing Service](https://www.ams.usda.gov/).

- Ergonomic client for interacting with MPR DataMart
- Parses XML data into json
- Parses report data from strings into numpy dtypes and record arrays
- Builds a dynamic timeseries filesystem cache of requested data
- Aggregates data into common reports as pandas DataFrames 

See examples in the [examples notebook](examples.ipynb)

- Ergonomic client for interacting with MPR DataMart
- Parses XML data into json
- Parses report data from strings into numpy dtypes and record arrays
- Builds a dynamic timeseries filesystem cache of requested data
- Aggregates data into common reports as pandas DataFrames 

See example usage in the [examples notebook](examples.ipynb)

### Setup
This project uses [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv). Install dependencies:
```bash
pip install --user pipenv
pipenv install
```

### Commands
These all need to be run from the project root.

```bash
# View CME Lean Hog Index report for last 20 days
bin/cash --days=20

# View CME Cutout Index report (default last 10 days)
bin/cutout

# View Lean Hog Purchases report
bin/purchases

# View a USDA report by report slug
bin/report lm_hg201

# Lint and run unit tests
bin/tests

# Lint and run unit and acceptance tests
bin/check

# Wipe reports cache
bin/wipe

# Build wheel for deployment
bin/build

# Remove build artifacts
bin/clean
```
