# Generated by Django 2.2.4 on 2020-11-04 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_principal', '0002_auto_20201019_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto_perfil/'),
        ),
    ]