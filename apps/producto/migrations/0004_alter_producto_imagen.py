# Generated by Django 4.1.5 on 2023-01-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]