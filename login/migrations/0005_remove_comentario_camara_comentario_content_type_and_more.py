# Generated by Django 5.0.4 on 2024-06-05 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('login', '0004_alter_customuser_foto_perfil_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='camara',
        ),
        migrations.AddField(
            model_name='comentario',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]