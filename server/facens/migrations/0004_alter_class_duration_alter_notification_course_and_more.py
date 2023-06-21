# Generated by Django 4.1.7 on 2023-06-21 18:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facens', '0003_alter_class_duration_alter_class_weekday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=3000)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facens.course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
