# Generated by Django 4.0.2 on 2022-06-16 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dueño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('rut', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mascota', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('domicilio', models.TextField()),
                ('dueño', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.dueño')),
            ],
        ),
    ]
