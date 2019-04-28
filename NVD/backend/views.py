from rest_framework import viewsets, generics
from rest_framework import filters

from . import models
from . import serializers


class CVEViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CVE.objects.all()
    serializer_class = serializers.CVESerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('cve_id', 'vendors', 'cwes', 'descriptions')
    ordering_fields = ('cve_id',)


class YearsVulnerabilitiesCountViewSet(generics.ListAPIView):
    queryset = models.YearsVulnerabilitiesCount.objects.all()
    serializer_class = serializers.YearsVulnerabilitiesCountSerializer


class MostVulnerableVendorsViewSet(generics.ListAPIView):
    queryset = models.MostVulnerableVendors.objects.all()
    serializer_class = serializers.MostVulnerableVendorsSerializer
