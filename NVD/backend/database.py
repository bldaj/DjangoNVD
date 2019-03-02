"""
Database module.

Used for making operations with PostgresQL.
"""

import peewee
from .models import CVE, db

peewee.logger.disabled = True

PG_CONFIG = {
    "user": 'admin',
    "password": '123',
    "database": 'NVD',
    "host": 'localhost',
    "port": 5432,
}

database = peewee.PostgresqlDatabase(**PG_CONFIG)

db.initialize(database)


def connect_database(db) -> bool:
    try:
        if db.is_closed():
            db.connect()
        return True

    except peewee.OperationalError as peewee_operational_error:
        print("[-] Connect Postgres database error: %s", peewee_operational_error)

    return False


def disconnect_database(db) -> bool:
    try:
        if db.is_closed():
            pass
        else:
            db.close()
        return True

    except peewee.OperationalError as peewee_operational_error:
        print("[-] Disconnect Postgres database error: %s", peewee_operational_error)

    return False


def create_table():
    connect_database(database)

    if not CVE.table_exists():
        CVE.create_table()

    disconnect_database(database)


def create_or_update_vulnerability(vulnerability: dict):
    connect_database(database)

    cve, created = CVE.get_or_create(
        cve_id=vulnerability['cve_id'],
        defaults=vulnerability
    )

    if not created:
        (CVE.insert(**vulnerability).on_conflict(
            conflict_target=(
                CVE.cve_id
            ),
            update={
                CVE.vendors: vulnerability['vendors'],
                CVE.cwes: vulnerability['cwes'],
                CVE.references: vulnerability['references'],
                CVE.descriptions: vulnerability['descriptions'],
                CVE.cpes: vulnerability['cpes'],
                CVE.impact: vulnerability['impact'],
                CVE.published_date: vulnerability['published_date'],
                CVE.last_modified_date: vulnerability['last_modified_date']
            }
        ).execute())

    disconnect_database(database)


def create_or_update_vulnerabilities(vulnerabilities: list):
    create_table()

    for vulnerability in vulnerabilities:
        create_or_update_vulnerability(vulnerability)
