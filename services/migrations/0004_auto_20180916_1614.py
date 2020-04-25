# Generated by Django 2.0.2 on 2018-09-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20180916_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='associated',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitud (Opcional)'),
        ),
        migrations.AddField(
            model_name='associated',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitud (Opcional)'),
        ),
    ]
