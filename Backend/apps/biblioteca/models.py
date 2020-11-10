from django.db import models
from apps.modulo_principal.models import Usuario
# Create your models here.
import datetime

class Biblioteca(models.Model):
	id_biblioteca = models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	autor = models.CharField(blank=True,null=True,default='Sin definir',max_length=50)
	descripcion = models.TextField(default='Sin descripcion',null=True,blank=True)
	documento = models.FileField(null=False,blank=False)
	fecha_subida = models.DateField(default=datetime.date.today)

	class Meta:
		verbose_name='sap_bibliteca'
		verbose_name_plural='sap_bibliteca_documentos'
		db_table = 'sap_biblioteca'

	def __str__(self):
		return self.documento.name