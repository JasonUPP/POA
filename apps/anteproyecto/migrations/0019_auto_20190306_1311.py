# Generated by Django 2.1.4 on 2019-03-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0018_auto_20190306_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='anteproyecto',
        ),
        migrations.AddField(
            model_name='estado',
            name='anteproyecto',
            field=models.ManyToManyField(to='anteproyecto.AnteProyecto'),
        ),
    ]