# Generated by Django 4.2.6 on 2023-10-17 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arreglo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arreglo',
            name='costo',
            field=models.FloatField(verbose_name='Ingrese el costso del arreglo'),
        ),
    ]