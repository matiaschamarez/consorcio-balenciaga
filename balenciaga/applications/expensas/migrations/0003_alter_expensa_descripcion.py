# Generated by Django 4.2.6 on 2023-10-21 00:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expensas', '0002_remove_expensa_monto_total_arreglos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensa',
            name='descripcion',
            field=ckeditor.fields.RichTextField(help_text='Descripcion'),
        ),
    ]
