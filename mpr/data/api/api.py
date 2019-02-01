from datetime import date
from enum import Enum
from typing import Dict, Iterator, Optional, Tuple
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
import io

import aiohttp
import numpy as np

Attributes = Dict[str, str]
ParsedElement = Tuple[str, Element]

class Report(Enum):
  PURCHASED_SWINE = 'LM_HG200'
  SLAUGHTERED_SWINE = 'LM_HG201'
  DIRECT_HOG_MORNING = 'LM_HG202'
  DIRECT_HOG_AFTERNOON = 'LM_HG203'
  CUTOUT_MORNING = 'LM_PK602'
  CUTOUT_AFTERNOON = 'LM_PK603'

date_format = "%m-%d-%Y"

base_url = 'https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs/{report}?\
filter={{"filters":[{{"fieldName":"Report date","operatorType":"BETWEEN","values":["{start_date}", "{end_date}"]}}]}}'

def get_optional(attr: Attributes, key: str) -> Optional[str]:
  return attr[key] if key in attr and attr[key] != 'null' else None

def opt_float(attr: Attributes, key: str) -> Optional[float]:
  value = get_optional(attr, key)
  return float(value.replace(',', '')) if value else None

def opt_int(attr: Attributes, key: str) -> Optional[int]:
  value = get_optional(attr, key)
  return int(value.replace(',', '')) if value else None

def date_interval(days: int) -> Tuple[date, date]:
  today = date.today()
  start = np.busday_offset(today, -days).astype('O')

  return (start, today)

async def fetch(report: Report, start_date: date, end_date=date.today()) -> Iterator[Attributes]:
  url = base_url.format(
    report=report.value,
    start_date=start_date.strftime(date_format),
    end_date=end_date.strftime(date_format))

  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      data = io.BytesIO(await response.read())
      elements = ElementTree.iterparse(data, events=['start', 'end'])

      return parse_elements(elements)

def parse_elements(elements: Iterator[ParsedElement]) -> Iterator[Attributes]:
  """ The USDA reports all follow a similar structure, with an outer <record> holding the date for each observation in the set.
      Within each date <record>, there are several <report> elements, each marking a new section with a label attribute.
      Within each section, there are one or more <record> elements which hold the actual report data.

      Here is an example of the layout described above, from one section of one day of the daily pork cutout report:

      <results exportTime="2018-09-07 12:25:37 CDT">
        <report label="National Daily Pork Report - Negotiated Sales" slug="LM_PK603">
          <record report_date="08/20/2018">
            <report label="Cutout and Primal Values">
              <record
                pork_carcass="67.18"
                pork_loin="75.51"
                pork_butt="89.55"`
                pork_picnic="41.82"
                pork_rib="113.95"
                pork_ham="57.52"
                pork_belly="77.77" />
            </report>
          </record>
        </report>
      </results>

      This generator flattens the data by yielding a merged dictionary of all attributes from the child data elements
      up to the parent elements, using a stream of lazily parsed XML elements from the api response.

      The result from the above example would be this dictionary:
      {
        'report_date': '08/20/2018',
        'label': 'Cutout and Primal Values',
        'pork_carcass': '67.18',
        'pork_loin': '75.51',
        'pork_butt': '89.55"',
        'pork_picnic': '41.82',
        'pork_rib': '113.95',
        'pork_ham': '57.52',
        'pork_belly': '77.77'
      }
  """

  depth = 0
  metadata = dict()

  for event, element in elements:
    if event == 'start':
      if 1 < depth < 4:
        # collect report_date and label into metadata dict
        metadata.update(element.items())

      elif depth == 4:
        # yield merged dictionary of metadata and record attributes
        yield dict(metadata.items() | element.items())

      depth += 1

    if event == 'end':
      depth -= 1

      # clear after parsing each date
      if depth == 2:
        element.clear()
        metadata.clear()
