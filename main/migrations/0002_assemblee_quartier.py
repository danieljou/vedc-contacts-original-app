# Generated by Django 4.0.1 on 2022-08-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assemblee',
            name='Quartier',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
