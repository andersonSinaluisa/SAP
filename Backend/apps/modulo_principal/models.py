from django.db import models
import datetime

# Create your models here.

class Persona(models.Model):
	id_persona = models.AutoField(primary_key=True)
	nombres = models.CharField(null=False,blank=False,max_length=50)
	apellidos = models.CharField(null=False,blank=False,max_length=50)
	identificacion = models.CharField(null=False,blank=False,max_length=10,unique=False)
	foto = models.ImageField(upload_to="foto_perfil/",null=True,blank=True)


	class Meta:
		verbose_name = 'sap_persona',
		verbose_name_plural = 'sap_personas',
		db_table = 'sap_personas'
		
	def __str__(self):
		return self.nombres

class Usuario(models.Model):
	id_usuario = models.AutoField(primary_key=True)
	correo = models.EmailField(unique=True,blank=False,null=False)
	clave = models.CharField(blank=False,null=False,max_length=50)
	id_persona = models.ForeignKey(Persona,db_column='id_persona',on_delete=models.CASCADE)
	fecha_creacion = models.DateField(null=False,blank=False,default=datetime.date.today)
	
	class Meta:
		verbose_name='sap_usuario'
		verbose_name_plural = 'sap_usuarios'
		db_table = 'sap_usuario'
	
	def __str__(self):
		return self.correo