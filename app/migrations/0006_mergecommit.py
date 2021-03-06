# Generated by Django 3.2.7 on 2021-10-10 19:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_project_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MergeCommit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commit_hash', models.CharField(max_length=50)),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.response')),
            ],
        ),
    ]
