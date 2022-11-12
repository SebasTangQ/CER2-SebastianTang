# Generated by Django 4.1.3 on 2022-11-08 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=10)),
                ('fono', models.CharField(max_length=8)),
                ('propietario', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('DOCUMENTO', 'Documento'), ('ENCOMIENDA', 'Encomienda')], max_length=10)),
                ('estado', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('ENTREGADO', 'Entregado')], max_length=10)),
                ('fecha_recepcion', models.DateField()),
                ('residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.residencia')),
            ],
        ),
    ]
