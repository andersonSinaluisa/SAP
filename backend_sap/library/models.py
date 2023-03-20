from django.db import models
from django.contrib.auth.models import User

import datetime

class Library(models.Model):
	id_biblioteca = models.AutoField(primary_key=True)
	id_usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	autor = models.CharField(blank=True,null=True,default='Sin definir',max_length=50)
	descripcion = models.TextField(default='Sin descripcion',null=True,blank=True)
	documento = models.FileField(null=False,blank=False)
	fecha_subida = models.DateField(default=datetime.date.today)
	type_doc = models.CharField(max_length=100,default='docx')

	class Meta:
		verbose_name='Library'
		verbose_name_plural='Library documents'

	def __str__(self):
		return self.documento.name


class CheckHistory(models.Model):
	id_usuario = models.ForeignKey(User,on_delete=models.CASCADE)
	fecha = models.DateField(default=datetime.date.today)
	estado = models.BooleanField(default=False)
	doc_id = models.ForeignKey(Library,on_delete=models.CASCADE)
	doc_compare_id = models.ForeignKey(Library,on_delete=models.CASCADE,related_name='doc_compare_id')

	class Meta:
		verbose_name='CheckHistory'
		verbose_name_plural='CheckHistory documents'

	def __str__(self):
		return self.archivo.name