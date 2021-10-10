# Generated by Django 3.2.7 on 2021-10-10 09:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211008_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=99, unique=True)),
                ('following', models.IntegerField()),
                ('followers', models.IntegerField()),
                ('sponsors', models.IntegerField()),
                ('repositories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_owner', models.CharField(max_length=99)),
                ('project_repo', models.CharField(max_length=99)),
                ('stars', models.IntegerField()),
                ('forks', models.IntegerField()),
                ('issues', models.IntegerField()),
                ('pulls', models.IntegerField()),
            ],
            options={
                'unique_together': {('project_owner', 'project_repo')},
            },
        ),
    ]
