from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('cves', views.CVEViewSet, basename='cve')

urlpatterns = [
    path('', include(router.urls)),
    path('vulnerabilities_summary/', views.YearsVulnerabilitiesCountViewSet.as_view(), name='summary'),
    path('most_vulnerable_vendors/', views.MostVulnerableVendorsViewSet.as_view(), name='most_vulnerable_vendors')
]
