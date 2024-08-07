# Generated by Django 5.0.4 on 2024-05-31 23:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=2500)),
                ('descripcion', models.TextField(max_length=2500)),
                ('url_accion', models.URLField(max_length=2500)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_cierre', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visto', models.BooleanField(default=False)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to='evento.evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notificaciones', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notificación',
                'verbose_name_plural': 'Notificaciones',
                'unique_together': {('usuario', 'evento')},
            },
        ),
    ]
