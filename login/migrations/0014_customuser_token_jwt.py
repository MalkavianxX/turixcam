# Generated by Django 5.0.4 on 2024-07-17 06:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_atencion_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='Jwt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('ultimo_cambio', models.DateTimeField(blank=True, null=True)),
                ('token', models.CharField(max_length=250)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
