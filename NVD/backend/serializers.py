from rest_framework import serializers
from .models import CVE


class CVESerializer(serializers.ModelSerializer):
    class Meta:
        model = CVE
        fields = (
            'id', 'cve_id', 'vendors', 'cwes', 'references', 'descriptions',
            'cpes', 'impact', 'published_date', 'last_modified_date'
        )
