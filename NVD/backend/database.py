"""
Database module.

Used for making operations with PostgresQL.
"""

import os

from . import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NVD.settings')


def create_or_update_vulnerability(vulnerability: dict):

    cve, created = models.CVE.objects.update_or_create(
        cve_id=vulnerability['cve_id'],
        defaults=vulnerability
    )


def create_or_update_vulnerabilities(vulnerabilities: list):
    for vulnerability in vulnerabilities:
        create_or_update_vulnerability(vulnerability)
