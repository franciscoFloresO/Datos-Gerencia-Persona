# Generated by Django 4.1.5 on 2024-04-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_remove_disponibilidad_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='numero_documento',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='horascompensadas',
            name='numero_documento',
            field=models.CharField(max_length=25),
        ),
    ]
