from argparse import ArgumentParser
from asyncio import run

from . import get_cutout_index

parser = ArgumentParser(description='Calculate the CME Cutout Index', usage='cash [--days=10]')
parser.add_argument('--days', help='How many days to show', dest='days', type=int, default=10)
days = parser.parse_args().days

print(run(get_cutout_index(days)))
