# Generated by Django 4.2.6 on 2023-10-21 00:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasto_administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gastoadministracion',
            name='descripcion',
            field=ckeditor.fields.RichTextField(help_text='Descripcion del gasto de administración'),
        ),
        migrations.AlterField(
            model_name='gastoadministracion',
            name='fecha',
            field=models.DateField(verbose_name='Ingrese la fecha'),
        ),
        migrations.AlterField(
            model_name='gastoadministracion',
            name='monto',
            field=models.FloatField(verbose_name='Ingrese monto'),
        ),
    ]
