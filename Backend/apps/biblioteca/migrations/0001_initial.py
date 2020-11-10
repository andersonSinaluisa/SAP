# Generated by Django 2.2.4 on 2020-10-19 22:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulo_principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id_biblioteca', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.CharField(blank=True, default='Sin definir', max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, default='Sin descripcion', null=True)),
                ('documento', models.FileField(upload_to='')),
                ('fecha_subida', models.DateField(default=datetime.date.today)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_principal.Usuario')),
            ],
            options={
                'verbose_name': 'sap_bibliteca',
                'verbose_name_plural': 'sap_bibliteca_documentos',
                'db_table': 'sap_biblioteca',
            },
        ),
    ]
