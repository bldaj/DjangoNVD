"""
Database module.

Used for making operations with PostgresQL.
"""

import os

from . import models
from .utils import get_year_from_filename

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NVD.settings')


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


def create_or_update_vulnerabilities(vulnerabilities: list) -> int:
    count = 0
    for vulnerability in vulnerabilities:
        create_or_update_vulnerability(vulnerability)
        count += 1

    return count
