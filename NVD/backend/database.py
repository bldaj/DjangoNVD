"""
Database module.

Used for making operations with PostgresQL.
"""

import os

from . import models
from .utils import get_year_from_filename

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NVD.settings')


def get_cves_by_year(year: int):
    return models.CVE.objects.filter(cve_id__contains=year)


def create_or_update_most_vulnerable_vendors(vulnerable_vendor: dict):
    models.MostVulnerableVendors.objects.update_or_create(
        **vulnerable_vendor
    )


# TODO: rename it to `create_or_update_vulnerabilities_count`
def update_vulnerabilities_count(filename: str, count: int):
    year = get_year_from_filename(filename)

    if year:
        models.YearsVulnerabilitiesCount.objects.update_or_create(
            year=year[0],
            vulnerabilities_count=count
        )


def create_or_update_vulnerability(vulnerability: dict):
    models.CVE.objects.update_or_create(
        cve_id=vulnerability['cve_id'],
        defaults=vulnerability
    )


# TODO: try to move it into cve_parser module
def create_or_update_vulnerabilities(vulnerabilities: list) -> int:
    count = 0
    for vulnerability in vulnerabilities:
        create_or_update_vulnerability(vulnerability)
        count += 1

    return count
