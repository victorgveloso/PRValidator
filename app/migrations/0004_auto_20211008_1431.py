# Generated by Django 3.2.7 on 2021-10-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210913_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='classification',
            field=models.CharField(blank=True, default=None, max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='classification',
            field=models.CharField(blank=True, default=None, max_length=99, null=True),
        ),
    ]
