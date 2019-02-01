from datetime import date
from enum import Enum
from typing import Dict, AsyncIterator
from xml.etree import ElementTree

import aiohttp

Attributes = Dict[str, str]

date_format = "%m/%d/%Y"

base_url = 'https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs/{report}?\
filter={{"filters":[{{"fieldName":"Report date","operatorType":"BETWEEN","values":["{start}", "{end}"]}}]}}'

class Report(Enum):
  PURCHASED_SWINE = 'LM_HG200'
  SLAUGHTERED_SWINE = 'LM_HG201'
  DIRECT_HOG_MORNING = 'LM_HG202'
  DIRECT_HOG_AFTERNOON = 'LM_HG203'
  CUTOUT_MORNING = 'LM_PK602'
  CUTOUT_AFTERNOON = 'LM_PK603'

async def fetch(report: Report, start: date, end=date.today()) -> AsyncIterator[Attributes]:
  """
  The USDA reports all follow a similar nested structure, with outer metadata elements wrapping the record elements
  which hold the actual data. An example from one section of one day of the daily pork cutout report:

  <results exportTime="2018-08-20 15:25:37 CDT">
    <report label="National Daily Pork Report - Negotiated Sales" slug="LM_PK603">
      <record report_date="08/20/2018">
        <report label="Cutout and Primal Values">
          <record
            pork_carcass="67.18"
            pork_loin="75.51"
            pork_butt="89.55"
            pork_picnic="41.82"
            pork_rib="113.95"
            pork_ham="57.52"
            pork_belly="77.77" />
        </report>
      </record>
    </report>
  </results>

  This generator flattens the data by yielding a merged dictionary of all attributes from the child data elements
  up to the metadata parent elements, using a chunked stream of parsed XML elements from the api response.

  The result from the above example would be this dictionary:
  {
    'exportTime': '2018-08-20 15:25:37 CDT',
    'slug': 'LM_PK603',
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

  A real example would have multiple sections with multiple records within them. An example of a full report can be found here:

  https://mpr.datamart.ams.usda.gov/ws/report/v1/hogs/LM_pk603?filter={"filters":[{"fieldName":"Report%20date","operatorType":"BETWEEN","values":["08/20/2018","08/21/2018"]}]}
  """

  url = base_url.format(report=report.value, start=start.strftime(date_format), end=end.strftime(date_format))

  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      content = response.content
      parser = ElementTree.XMLPullParser(['start', 'end'])

      depth = 0
      metadata = dict()

      async for chunk in content.iter_any():
        parser.feed(chunk)

        for event, element in parser.read_events():
          if event == 'start':
            if depth < 4:
              metadata.update(element.items())
            else:
              yield dict(metadata.items() | element.items())

            depth += 1

          elif event == 'end':
            depth -= 1
            element.clear()

      parser.close()
