# Generated by Django 3.1.1 on 2020-09-28 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_roastboast_total_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roastboast',
            name='total_votes',
        ),
    ]
