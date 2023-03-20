# Generated by Django 2.2.4 on 2023-02-21 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogClient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('ip', models.CharField(max_length=20)),
                ('agent', models.CharField(max_length=100)),
                ('browser', models.CharField(max_length=100)),
                ('os', models.CharField(max_length=100)),
                ('device', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
                ('longitude', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('asn', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('isp', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('ip_type', models.CharField(max_length=100)),
                ('endpoint', models.CharField(max_length=100)),
                ('action_type', models.CharField(max_length=100)),
                ('page_title', models.CharField(max_length=100)),
                ('page_url', models.CharField(max_length=100)),
                ('type_request', models.CharField(max_length=100)),
                ('status_code', models.CharField(max_length=100)),
                ('status_text', models.CharField(max_length=100)),
                ('request_method', models.CharField(max_length=100)),
                ('request_url', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'log_clients',
            },
        ),
    ]
