from rest_framework import viewsets, generics

from . import models
from . import serializers


class YearsVulnerabilitiesCountViewSet(generics.ListAPIView):
    queryset = models.YearsVulnerabilitiesCount.objects.all()
    serializer_class = serializers.YearsVulnerabilitiesCountSerializer


class CVEViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CVE.objects.all()
    serializer_class = serializers.CVESerializer
