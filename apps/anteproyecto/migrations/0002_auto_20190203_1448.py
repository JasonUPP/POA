# Generated by Django 2.1.4 on 2019-02-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anteproyecto',
            name='capitulo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='anteproyecto',
            name='partida',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
