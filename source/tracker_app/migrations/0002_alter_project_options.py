# Generated by Django 4.0.1 on 2022-02-17 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('add_users', 'Может добавлять пользователей в проэкт')], 'verbose_name': 'Проэкт', 'verbose_name_plural': 'Проэкты'},
        ),
    ]