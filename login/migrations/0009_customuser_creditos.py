# Generated by Django 5.0.4 on 2024-06-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_customuser_custom_avatar_uploaded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='creditos',
            field=models.IntegerField(default=0),
        ),
    ]