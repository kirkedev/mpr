import argparse
import asyncio

from . import get_cutout_index

parser = argparse.ArgumentParser(description='Calculate the CME Cutout Index')
parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)

days = parser.parse_args().days
print(asyncio.run(get_cutout_index(days)))
