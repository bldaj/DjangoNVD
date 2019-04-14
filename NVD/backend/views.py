from rest_framework import viewsets, generics

from . import models
from . import serializers


class CVEViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CVE.objects.all()
    serializer_class = serializers.CVESerializer


class YearsVulnerabilitiesCountViewSet(generics.ListAPIView):
    queryset = models.YearsVulnerabilitiesCount.objects.all()
    serializer_class = serializers.YearsVulnerabilitiesCountSerializer


class MostVulnerableVendorsViewSet(generics.ListAPIView):
    queryset = models.MostVulnerableVendors.objects.all()
    serializer_class = serializers.MostVulnerableVendorsSerializer
