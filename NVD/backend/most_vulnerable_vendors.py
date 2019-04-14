import json
import csv

import pandas as pd

from NVD.settings import START_YEAR
from .database import get_cves_by_year, create_or_update_most_vulnerable_vendors
from .utils import get_current_year

CVE_PREFIX = 'CVE'


def deserialize_vendors(cves):
    deserealized_vendors = []

    for cve in cves:
        for vendor in cve.vendors:
            deserealized_vendor = json.loads(vendor)
            deserealized_vendors.append(deserealized_vendor.get('vendor', None))

    return deserealized_vendors


def read_csv_file(year: int) -> list:
    vulnerable_vendors = []

    with open('backend/CVEs/CSV/{prefix}-{year}.csv'.format(prefix=CVE_PREFIX, year=year), 'r') as f:
        reader = csv.reader(f, delimiter=' ')

        for row in reader:
            vulnerable_vendors.append({
                'vendor': row[0],
                'vulnerabilities_count': row[1],
                'year': year
            })

    return vulnerable_vendors


def save_csv_file_by_year(year: int, index: pd.Index):
    index.to_csv(
        'backend/CVEs/CSV/{prefix}-{year}.csv'.format(prefix=CVE_PREFIX, year=year),
        sep=' ',
        encoding='utf-8'
    )


def save_data_to_db():
    for year in range(START_YEAR, get_current_year()):
        vulnerable_vendors = read_csv_file(year)

        for vulnerable_vendor in vulnerable_vendors:
            create_or_update_most_vulnerable_vendors(vulnerable_vendor)


def analyse_most_vulnerable_vendors():
    for year in range(START_YEAR, get_current_year()):
        cves = get_cves_by_year(year)

        deserialized_vendors = deserialize_vendors(cves)

        index = pd.Index(deserialized_vendors).value_counts()[:10]
        save_csv_file_by_year(year, index)


def main():
    analyse_most_vulnerable_vendors()
    save_data_to_db()


if __name__ == '__main__':
    main()
