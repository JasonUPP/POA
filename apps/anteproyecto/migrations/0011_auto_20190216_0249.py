# Generated by Django 2.1.4 on 2019-02-16 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anteproyecto', '0010_auto_20190216_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capitulo',
            name='concepto',
        ),
        migrations.RemoveField(
            model_name='capitulo',
            name='fila',
        ),
        migrations.RemoveField(
            model_name='concepto',
            name='partidaGenerica',
        ),
        migrations.RemoveField(
            model_name='partidaespecifica',
            name='fila',
        ),
        migrations.RemoveField(
            model_name='partidagenerica',
            name='fila',
        ),
        migrations.RemoveField(
            model_name='partidagenerica',
            name='partidaEspecifica',
        ),
    ]
