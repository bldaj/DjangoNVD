from rest_framework import serializers
from . import models


class CVESerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CVE
        fields = (
            'id', 'cve_id', 'vendors', 'cwes', 'references', 'descriptions',
            'cpes', 'impact', 'published_date', 'last_modified_date'
        )


class YearsVulnerabilitiesCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.YearsVulnerabilitiesCount
        fields = (
            'year', 'vulnerabilities_count'
        )


class MostVulnerableVendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MostVulnerableVendors
        fields = (
            'vendor', 'vulnerabilities_count', 'year'
        )
