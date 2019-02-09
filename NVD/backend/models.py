from django.db import models


class CVE(models.Model):
    cve_id = models.CharField(max_length=15, null=False)
    cvss_score = models.FloatField()
    access_vector = models.CharField(max_length=50)
    access_complexity = models.CharField(max_length=15)
    authentication = models.CharField(max_length=15)
    confidentiality_impact = models.CharField(max_length=15)
    integrity_impact = models.CharField(max_length=15)
    availability_impact = models.CharField(max_length=15)
    source = models.CharField(max_length=50)
    generated_datetime = models.DateTimeField()
    cwe_id = models.CharField(max_length=15)

    def __str__(self):
        return self.cve_id
