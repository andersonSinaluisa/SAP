from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class LogClient(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    ip = models.CharField(max_length=20,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True, related_name='user_id')
    agent = models.CharField(max_length=255,null=True)
    browser = models.CharField(max_length=255,null=True)
    os = models.CharField(max_length=255,null=True)
    device = models.CharField(max_length=255,null=True)
    platform = models.CharField(max_length=255,null=True)
    version = models.CharField(max_length=255,null=True)
    language = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    region = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    latitude = models.CharField(max_length=255,null=True)
    longitude = models.CharField(max_length=255,null=True)
    timezone = models.CharField(max_length=255,null=True)
    continent = models.CharField(max_length=255)
    currency = models.CharField(max_length=255,null=True)
    asn = models.CharField(max_length=255,null=True)
    organization = models.CharField(max_length=255,null=True)
    isp = models.CharField(max_length=255,null=True)
    domain = models.CharField(max_length=255,null=True)
    ip_type = models.CharField(max_length=255,null=True)
    endpoint = models.CharField(max_length=255,null=True)
    action_type = models.CharField(max_length=255,null=True)
    page_title = models.CharField(max_length=255,null=True)
    page_url = models.CharField(max_length=255,null=True)
    type_request = models.CharField(max_length=255,null=True)
    status_code = models.CharField(max_length=255,null=True)
    status_text = models.CharField(max_length=255,null=True)
    request_method = models.CharField(max_length=255,null=True)
    request_url = models.CharField(max_length=255,null=True)
    

    class Meta:
        db_table = 'log_clients'

    def __str__(self):
        return self.ip


