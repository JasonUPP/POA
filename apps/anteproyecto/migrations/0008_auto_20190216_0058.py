# Generated by Django 2.1.4 on 2019-02-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0007_auto_20190215_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anteproyecto',
            name='fila',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='anteproyecto',
            name='total',
            field=models.FloatField(blank=True, max_length=30),
        ),
    ]