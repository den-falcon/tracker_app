# Generated by Django 4.0.1 on 2022-02-24 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('accounts_list', 'Может просматривать список пользователей')], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
