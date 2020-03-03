mpr
===
[![Build Status](https://travis-ci.com/gumballhead/mpr.svg?branch=master)](https://travis-ci.com/gumballhead/mpr)
[![Coverage Status](https://coveralls.io/repos/github/gumballhead/mpr/badge.svg?branch=master)](https://coveralls.io/github/gumballhead/mpr?branch=master)

Python package for downloading, parsing, and analyzing historical [ Mandatory Price Reporting](https://mpr.datamart.ams.usda.gov/) data from the USDA's [Agricultural Marketing Service](https://www.ams.usda.gov/).

### Setup
This project uses [conda](https://conda.io/en/latest/miniconda.html). Install python packages and activate environment:
```bash
conda env create -f environment.yml
conda activate mpr
```

It's a good idea to use something like [direnv](https://direnv.net/) to activate the conda environment and add the scripts in `bin` to your path. 

My `.envrc` file looks like this:
```bash
export PATH=$PATH:./bin
source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate mpr
```

### Commands
These all need to be run from the project root. If using direnv and an envrc like above, you can omit the path and run the script directly, eg: `tests`.

```bash
# View CME Lean Hog Index report for last 20 days
bin/cash --days=20

# View CME Cutout Index report (default last 10 days)
bin/cutout

# View a USDA report by report slug
bin/report lm_hg201

# Lint and run unit tests
bin/tests

# Lint and run unit and acceptance tests
bin/check

# Build wheel for deployment
bin/build

# Remove build artifacts
bin/clean
```
