from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField


class CVE(models.Model):
    cve_id = models.TextField(null=False, unique=True)
    vendors = ArrayField(
        models.TextField()
    )
    cwes = ArrayField(
        models.TextField()
    )
    references = ArrayField(
        models.TextField()
    )
    descriptions = ArrayField(
        models.TextField()
    )
    cpes = ArrayField(
        models.TextField()
    )
    impact = JSONField()
    published_date = models.TextField(null=False)
    last_modified_date = models.TextField(null=False)

    def __str__(self):
        return self.cve_id

    class Meta:
        ordering = ['cve_id']


class YearsVulnerabilitiesCount(models.Model):
    year = models.IntegerField(unique=True)
    vulnerabilities_count = models.IntegerField()

    class Meta:
        ordering = ['year']


class MostVulnerableVendors(models.Model):
    vendor = models.TextField(null=False, blank=False)
    vulnerabilities_count = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)

    class Meta:
        ordering = ['-vulnerabilities_count']
