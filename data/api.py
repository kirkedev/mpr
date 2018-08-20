from enum import Enum
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from requests import get
from typing import Iterator, Tuple, Optional as Maybe, Dict
from datetime import date, timedelta

class Report(Enum):
  PURCHASED_SWINE = 'LM_HG200'
  SLAUGHTERED_SWINE = 'LM_HG201'
  DIRECT_HOG_MORNING = 'LM_HG202'
  DIRECT_HOG_AFTERNOON = 'LM_HG203'
  CUTOUT_MORNING = 'LM_PK601'
  CUTOUT_AFTERNOON = 'LM_PK602'

date_format = '%m-%d-%Y'

base_url = 'https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs/{report}?\
filter={{"filters":[{{"fieldName":"Report date","operatorType":"BETWEEN","values":["{start_date}", "{end_date}"]}}]}}'

def get_optional(attr: Dict[str, str], key: str) -> Maybe[str]:
  return attr[key] if key in attr and attr[key] != "null" else None

def fetch(report: Report, start_date: date, end_date: date=date.today()) -> Iterator[Tuple[str, Element]]:
  url = base_url.format(report=report.value, start_date=start_date.strftime(date_format), end_date=end_date.strftime(date_format))
  response = get(url, stream=True)

  return ElementTree.iterparse(response.raw, events=['start', 'end'])
