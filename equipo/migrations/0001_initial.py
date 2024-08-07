# Generated by Django 5.0.4 on 2024-05-31 23:00

import django_bunny.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellidom', models.CharField(max_length=250)),
                ('apellidop', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=250)),
                ('descripcion', models.TextField(max_length=10000)),
                ('mison', models.TextField(blank=True, max_length=10000, null=True)),
                ('vision', models.TextField(blank=True, max_length=10000, null=True)),
                ('puesto', models.CharField(blank=True, max_length=250, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, storage=django_bunny.storage.BunnyStorage(), upload_to='perfil_personal/')),
                ('foto_portada', models.ImageField(blank=True, null=True, storage=django_bunny.storage.BunnyStorage(), upload_to='portada_personal/')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
            },
        ),
    ]
