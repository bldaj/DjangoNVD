import django_filters

from backend.models import CVE


class CVEFilter(django_filters.FilterSet):
    cve_id = django_filters.CharFilter(lookup_expr='iexact')
    cvss = django_filters.NumberFilter(field_name='impact', method='filter_cvss')

    class Meta:
        model = CVE
        fields = ['cve_id', ]

    def filter_cvss(self, queryset, name, value):
        value = float(value)
        return queryset.filter(impact__baseMetricV2__cvssV2__baseScore=value)
