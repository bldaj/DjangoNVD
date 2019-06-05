# Generated by Django 2.1.5 on 2019-06-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_mostvulnerablevendors'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVSS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('score', models.PositiveSmallIntegerField()),
                ('count', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='cve',
            options={'ordering': ['cve_id']},
        ),
        migrations.AlterModelOptions(
            name='mostvulnerablevendors',
            options={'ordering': ['-vulnerabilities_count']},
        ),
        migrations.AlterModelOptions(
            name='yearsvulnerabilitiescount',
            options={'ordering': ['year']},
        ),
    ]
