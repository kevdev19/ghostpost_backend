# Generated by Django 3.1.1 on 2020-09-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roastboast',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]
