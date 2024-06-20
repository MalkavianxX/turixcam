# Generated by Django 5.0.4 on 2024-05-31 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camaras', '0002_camara_background_dark_web_camara_background_web_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camara',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='streams', to='camaras.stream'),
        ),
    ]