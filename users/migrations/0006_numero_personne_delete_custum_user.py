# Generated by Django 4.0.1 on 2022-08-01 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_alter_assemblee_type_encadreur'),
        ('users', '0005_alter_custum_user_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('code_du_pays', models.PositiveIntegerField()),
                ('disponible_sur_whatsapp', models.BooleanField()),
                ('disponible_sur_appel', models.BooleanField()),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assemblee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.assemblee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Custum_user',
        ),
    ]
