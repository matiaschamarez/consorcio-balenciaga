# Generated by Django 4.2.6 on 2023-10-21 00:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arreglo', '0002_alter_arreglo_costo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arreglo',
            name='costo',
            field=models.FloatField(verbose_name='Ingrese el costo del arreglo'),
        ),
        migrations.AlterField(
            model_name='arreglo',
            name='descripcion',
            field=ckeditor.fields.RichTextField(help_text='Ingrese la descripción del arreglo'),
        ),
    ]
