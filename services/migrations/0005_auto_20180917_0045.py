# Generated by Django 2.0.2 on 2018-09-17 03:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20180916_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]