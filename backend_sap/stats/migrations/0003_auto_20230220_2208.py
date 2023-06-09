# Generated by Django 2.2.4 on 2023-02-21 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20230220_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logclient',
            name='action_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='agent',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='asn',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='browser',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='currency',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='device',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='domain',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='endpoint',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='ip',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='ip_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='isp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='language',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='latitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='longitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='organization',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='os',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='page_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='page_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='platform',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='region',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='request_method',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='request_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='status_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='status_text',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='timezone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='type_request',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='logclient',
            name='version',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
