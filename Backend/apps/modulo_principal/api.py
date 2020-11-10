from rest_framework import viewsets
from .models import *
from .serializers import *
import hashlib
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import urllib.request
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.template.loader import get_template 
from email.mime.text import MIMEText
from smtplib import *


class SeguridadApi(APIView):
	def post(self,request):
		serializer = None
		usuario = None
		try:
			contra = request.data.get('clave')
			h = hashlib.new("sha1")
			contra = str.encode(contra)
			h.update(contra)
			usuario = Usuario.objects.filter(correo=request.data.get('correo'),clave=h.hexdigest())
			if usuario.exists():
				usuario = Usuario.objects.get(correo=request.data.get('correo'),clave=h.hexdigest())
				serializer = UsuarioSessionSerializer(usuario,many=False)
				return Response(serializer.data,status=status.HTTP_200_OK)
			else:
				return Response(status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			print(e)
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		






class UsuarioApi(APIView):
	
	
	def get(self,request):
		if request.query_params.get('id'):
			usuario = Usuario.objects.get(id_usuario=request.query_params.get('id'))
			serializer = UsuarioSerializer(usuario,many=False)
			return Response(serializer.data,status=status.HTTP_200_OK)
		elif request.query_params.get('correo') :
			usuario = Usuario.objects.get(correo=request.query_params.get('correo'))
			serializer = UsuarioSerializer(usuario,many=False)
			return Response(serializer.data,status=status.HTTP_200_OK)
		else:
			usuario = Usuario.objects.all()
			serializer = UsuarioSerializer(usuario,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)

	
	def post(self,request):
		#guardo la contraseña ingresada en una variable llamada contra
		contra = request.data.get('clave')
		#Inicializo el objeto hashLib que usare para encriptar contraseñas
		h = hashlib.new("sha1")
		#str.encode () devuelve una versión codificada de la cadena.Este paso es requerido para que haslib object funcione
		contra = str.encode(contra)
		#h.update() Encripta la contraseña
		h.update(contra)
		#Persona.objects.create() me permite hacer un registro a la base de datos en la tabla persona con los datos ingresados en el formulario
		#Con request.POST.get obtenge los valores del formulario apartir del name.
		#guardo esa nueva persona creada en una variable llamada persona.
		persona = Persona.objects.create(
									 nombres=request.data.get('nombres'),
									 apellidos=request.data.get('apellidos'),
									 identificacion=request.data.get('identificacion'),
									 #foto=request.FILES['foto']
									 )
		#Creo un registro en mi bases de datos de Usuario y lo guardo en la variable usuario
		#las campos que son claves fonaneas como es el caso de id_persona, el requiere un objeto de esa tabla, asi que ahi guardo el objeto persona
		#que se acaba de crear arriba
		usuario = Usuario.objects.create(
										id_persona=persona,
										correo=request.data.get('correo'),
										#h.hexdigest retorna la contraseña encriptada
										clave=h.hexdigest()
										)
		serializer = UsuarioSerializer(usuario,many=False)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request):
		usuario = Usuario.objects.get(id_usuario=request.data.get('id_usuario'))
		usuario.correo = request.data.get('correo')
		usuario.save()
		usuario.id_persona.nombres = request.data.get('nombres')
		usuario.id_persona.apellidos = request.data.get('apellidos')
		usuario.id_persona.identificacion = request.data.get('identificacion')
		usuario.id_persona.save()
		serializer = UsuarioSerializer(usuario,many=False)
		return Response(serializer.data,status=status.HTTP_200_OK)




