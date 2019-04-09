import json

import pandas as pd

from NVD.settings import START_YEAR
from .database import get_cves_by_year
from .utils import get_current_year


def deserialize_vendors(cves):
    deserealized_vendors = []

    for cve in cves:
        for vendor in cve.vendors:
            deserealized_vendor = json.loads(vendor)
            deserealized_vendors.append(deserealized_vendor.get('vendor', None))

    return deserealized_vendors


def save_csv_file_by_year(year: int, index: pd.Index):
    index.to_csv(
        'backend/CVEs/CSV/CVE-{year}.csv'.format(year=year),
        sep=' ',
        encoding='utf-8'
    )


def analyse_most_vulnerable_vendors():
    for year in range(START_YEAR, get_current_year()):
        cves = get_cves_by_year(year)

        deserialized_vendors = deserialize_vendors(cves)

        index = pd.Index(deserialized_vendors).value_counts()[:10]
        save_csv_file_by_year(year, index)


def main():
    analyse_most_vulnerable_vendors()
