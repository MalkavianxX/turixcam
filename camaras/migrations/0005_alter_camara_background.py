# Generated by Django 5.0.4 on 2024-07-03 09:07

import camaras.models
import django_bunny.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camaras', '0004_camara_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camara',
            name='background',
            field=models.ImageField(blank=True, max_length=250, null=True, storage=django_bunny.storage.BunnyStorage(), upload_to=camaras.models.Camara.camara_background_path),
        ),
    ]