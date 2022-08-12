# Generated by Django 4.0.6 on 2022-08-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_assemblee_continent'),
    ]

    operations = [
        migrations.AddField(
            model_name='assemblee',
            name='Latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assemblee',
            name='Longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
