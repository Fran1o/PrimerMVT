# Generated by Django 4.1.3 on 2022-11-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiaresapp', '0002_alter_familia_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='edad',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='familia',
            name='fecha_nacimiento',
            field=models.IntegerField(),
        ),
    ]
