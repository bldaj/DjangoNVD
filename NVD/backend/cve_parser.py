import os

from .utils import read_cve_json_file
from .cve_item import CVEItem


def parse_cve_items(cve_items: list):
    parsed_cves = []

    for cve_item in cve_items:
        parsed_cves.append(CVEItem(cve_item).to_dict())

    return parsed_cves


def parse_cves_files(filenames):
    for filename in filenames:
        parse_cve_items(read_cve_json_file(filename).get('CVE_Items', []))


def get_cve_filenames():
    filenames = []
    for dirpath, dirs, files in os.walk('CVEs/JSONs'):
        for file in files:
            filenames.append(os.path.join(dirpath, file))

    return filenames


def main():
    parse_cves_files(
        get_cve_filenames()
    )
