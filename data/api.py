from enum import Enum
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from requests import get, Response
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

Attributes = Dict[str, str]

def get_optional(attr: Attributes, key: str) -> Maybe[str]:
  return attr[key] if key in attr and attr[key] != 'null' else None

def fetch(report: Report, start_date: date, end_date: date=date.today()) -> Iterator[Tuple[str, Element]]:
  url = base_url.format(report=report.value, start_date=start_date.strftime(date_format), end_date=end_date.strftime(date_format))
  response = get(url, stream=True)

  return ElementTree.iterparse(response.raw, events=['start', 'end'])

def filter_section(elements: Iterator[Tuple[str, Element]], section: str) -> Iterator[Attributes]:
  """ The USDA reports all follow a similar structure, with an outer <record> holding the date metadata for each observation in the set.
      Within each date <record>, there are several <report> elements, each marking a new section with a label attribute.
      Within each section, there are one or more <record> elements which hold the actual report data.

      Example data point for one day...

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

      It's typical to use the date of each element as an index, so this method flattens the data by yielding a merged dictionary
      from the parent date <record> attributes and the child data <record> attributes matching the section filter, using a stream
      of lazily parsed XML elements from the api response. """

  depth = 0
  current_section = None

  for event, element in elements:
    if element.tag == 'report':
      current_section = element.attrib.get('label')

    if element.tag == 'record':
      if event == 'start':
        if depth == 0:
          parent = element

        if depth == 1 and current_section == section:
          yield { **parent.attrib, **element.attrib }

        depth += 1

      if event == 'end':
        depth -= 1

        if depth == 0:
          parent.clear()
          current_section = None
