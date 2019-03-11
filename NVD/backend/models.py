from django.db import models
from django.contrib.postgres.fields import ArrayField


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
    impact = models.TextField()
    published_date = models.TextField(null=False)
    last_modified_date = models.TextField(null=False)

    def __str__(self):
        return self.cve_id
