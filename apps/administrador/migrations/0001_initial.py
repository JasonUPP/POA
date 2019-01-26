# Generated by Django 2.1.4 on 2019-01-20 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=20)),
                ('apellidoM', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('sexo', models.CharField(max_length=10)),
                ('edad', models.IntegerField()),
                ('nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('domicilio', models.TextField()),
            ],
        ),
    ]
