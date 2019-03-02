import peewee
from playhouse.postgres_ext import ArrayField

db = peewee.Proxy()


class CVE(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    cve_id = peewee.TextField(null=False, unique=True)
    vendors = ArrayField(
        peewee.TextField
    )
    cwes = ArrayField(
        peewee.TextField
    )
    references = ArrayField(
        peewee.TextField
    )
    descriptions = ArrayField(
        peewee.TextField
    )
    cpes = ArrayField(
        peewee.TextField
    )
    impact = peewee.TextField()
    published_date = peewee.TextField(null=False)
    last_modified_date = peewee.TextField(null=False)

    def __str__(self):
        return self.cve_id

    class Meta:
        database = db
        table_name = 'CVE'
