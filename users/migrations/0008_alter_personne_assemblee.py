# Generated by Django 4.0.6 on 2022-08-03 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_assemblee_type_encadreur'),
        ('users', '0007_personne_is_encadreur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='assemblee',
            field=models.ForeignKey(blank=True, help_text="Si votre assemblée n'est pas disponible contactez votre encadreur", null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.assemblee'),
        ),
    ]
