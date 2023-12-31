# Generated by Django 4.1.7 on 2023-03-31 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facens', '0002_class_weekday_alter_class_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='duration',
            field=models.DurationField(default=50),
        ),
        migrations.AlterField(
            model_name='class',
            name='weekday',
            field=models.CharField(choices=[('1', 'Domingo'), ('2', 'Segunda'), ('3', 'Terca'), ('4', 'Quarta'), ('5', 'Quinta'), ('6', 'Sexta'), ('7', 'Sabado')], max_length=1),
        ),
    ]
