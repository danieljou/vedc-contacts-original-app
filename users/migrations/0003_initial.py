# Generated by Django 4.0.1 on 2022-07-19 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_delete_custumuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custum_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Gestionnaire', 'Gestionnaire'), ('Agent CFC', 'Agent CFC'), ('Supperviseur', 'Supperviseur'), ('Administrateur', 'Administrateur')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
