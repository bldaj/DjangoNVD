from django.db.models import Q

from NVD.settings import START_YEAR
from .models import CVE, CVSS
from .utils import get_current_year


def analyze_cvss():
    for year in range(START_YEAR, get_current_year()):
        for value in range(1, 11):
            count = CVE.objects.filter(
                Q(year=year)
                & Q(impact__baseMetricV2__cvssV2__baseScore=value)
            ).values('impact').count()

            CVSS.objects.update_or_create(
                year=year, score=value,
                defaults={'year': year, 'score': value, 'count': count}
            )


def main():
    analyze_cvss()
