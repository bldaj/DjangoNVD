from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets, generics

from . import models
from . import serializers
from .filters.cve import CVEFilter


class CVEViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CVE.objects.all()
    serializer_class = serializers.CVESerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('cve_id', 'vendors', 'cwes', 'descriptions')
    ordering_fields = ('cve_id',)
    filter_class = CVEFilter


class YearsVulnerabilitiesCountViewSet(generics.ListAPIView):
    queryset = models.YearsVulnerabilitiesCount.objects.all()
    serializer_class = serializers.YearsVulnerabilitiesCountSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('year',)


class MostVulnerableVendorsViewSet(generics.ListAPIView):
    queryset = models.MostVulnerableVendors.objects.all()
    serializer_class = serializers.MostVulnerableVendorsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('year',)


class CVSSViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CVSS.objects.all()
    serializer_class = serializers.CVSSSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('year',)
