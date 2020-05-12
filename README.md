mpr
===
[![Test Status](https://github.com/gumballhead/mpr/workflows/tests/badge.svg)](https://github.com/gumballhead/mpr/actions?query=workflow%3Atests)
[![Coverage Status](https://coveralls.io/repos/github/gumballhead/mpr/badge.svg?branch=master)](https://coveralls.io/github/gumballhead/mpr?branch=master)

Python package for downloading, parsing, and analyzing historical [Mandatory Price Reporting](https://mpr.datamart.ams.usda.gov/) data from the USDA's [Agricultural Marketing Service](https://www.ams.usda.gov/).

- Ergonomic client for interacting with MPR DataMart
- Parses XML data into json
- Parses report data from strings into numpy dtypes and record arrays
- Builds a dynamic timeseries filesystem cache of requested data
- Aggregates data into common reports as pandas DataFrames 

See examples in the [examples notebook](examples.ipynb)

### Setup
You'll need to [install pipenv](https://github.com/pypa/pipenv#installation) to run the code.

To activate the git hooks:
```bash 
git config core.hooksPath .githooks
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

# View CME Fresh Bacon Index report
bin/bacon

# Start jupyter notebook server
bin/notebook

# Lint and run unit and acceptance tests with coverage
bin/tests

# Wipe reports cache
bin/wipe

# Build wheel for deployment
bin/build

# Remove build artifacts
bin/clean
```
