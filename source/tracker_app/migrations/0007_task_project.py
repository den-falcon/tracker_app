# Generated by Django 4.0.1 on 2022-01-31 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker_app', '0006_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Tasks', to='tracker_app.project', verbose_name='Проэкт'),
            preserve_default=False,
        ),
    ]
