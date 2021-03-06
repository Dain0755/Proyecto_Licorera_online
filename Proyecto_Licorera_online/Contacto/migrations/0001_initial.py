# Generated by Django 4.0.4 on 2022-05-30 20:13

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('nombre_apellido', models.CharField(max_length=50)),
                ('id', models.BigIntegerField(primary_key=builtins.id, serialize=False)),
                ('correo', models.EmailField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('celular', models.BigIntegerField()),
                ('pagar', models.DecimalField(decimal_places=3, max_digits=10)),
                ('producto_Comprado', models.CharField(max_length=50)),
            ],
        ),
    ]
