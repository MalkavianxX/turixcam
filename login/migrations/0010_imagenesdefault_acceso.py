# Generated by Django 5.0.4 on 2024-06-10 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_customuser_creditos'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagenesdefault',
            name='acceso',
            field=models.CharField(default='free', max_length=50),
        ),
    ]