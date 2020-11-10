
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
import random 


class BibliotecaApi(APIView):
	def get(self,request):

		if not request.query_params.get('id'):
			lst_biblioteca = Biblioteca.objects.filter(id_usuario=request.query_params.get('id'))
		else:
			lst_biblioteca = Biblioteca.objects.filter(id_usuario=request.query_params.get('id'))
		serializer =  BibliotecaSerializer(lst_biblioteca,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	

	def post(self,request):
		nuevo_documento = Biblioteca.objects.create(
													id_usuario=request.data.get('id'),
													autor=request.data.get('autor'),
													descripcion=request.data.get('descripcion'),
													documento=request.data.get('documento')
													)
		serializer = BibliotecaSerializer(nuevo_documento,many=False)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request):
		biblioteca = Biblioteca.objects.get(id_biblioteca=request.data.get('id_bilioteca'))
		biblioteca.autor = request.data.get('autor')
		biblioteca.descripcion = request.data.get('descripcion')
		biblioteca.documento = request.data.get('documento')
		biblioteca.save()
		serializer = BibliotecaSerializer(biblioteca,many=False)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def delete(self,request):
		biblioteca = Biblioteca.objects.get(id_biblioteca=request.data.get('id_bilioteca'))
		biblioteca.delete()
		return Reponse({'elemento_borrado':'Documento eliminado'},status=status.HTTP_200_OK)
