# Generated by Django 4.0.6 on 2022-08-03 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_assemblee_type_encadreur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assemblee',
            name='Encadreur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Encandreur', to=settings.AUTH_USER_MODEL),
        ),
    ]
