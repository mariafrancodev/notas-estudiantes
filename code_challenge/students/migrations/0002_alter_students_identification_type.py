# Generated by Django 3.2.15 on 2022-08-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='identification_type',
            field=models.CharField(choices=[('tarjeta_de_identidad', 'Tarjeta de Identidad'), ('cedula', 'Cédula')], max_length=32, verbose_name='Tipo de documento'),
        ),
    ]