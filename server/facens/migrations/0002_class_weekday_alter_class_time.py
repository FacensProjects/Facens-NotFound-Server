# Generated by Django 4.1.7 on 2023-03-29 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='weekday',
            field=models.CharField(choices=[('0', 'Domingo'), ('1', 'Segunda'), ('2', 'Terca'), ('3', 'Quarta'), ('4', 'Quinta'), ('5', 'Sexta'), ('6', 'Sabado')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='time',
            field=models.TimeField(),
        ),
    ]