from rest_framework import viewsets

from .models import CVE
from .serializers import CVESerializer


class CVEViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CVE.objects.all()
    serializer_class = CVESerializer
