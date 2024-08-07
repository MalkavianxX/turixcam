# Generated by Django 5.0.4 on 2024-07-09 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('nombres', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('mensaje', models.TextField()),
                ('motivo', models.CharField(max_length=250)),
                ('estado', models.CharField(max_length=250)),
            ],
        ),
    ]
