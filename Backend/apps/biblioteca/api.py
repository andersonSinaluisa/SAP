
from .models import *
from apps.modulo_principal.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import urllib.request
#from django.core.mail import EmailMessage
from django.conf import settings
#from django.template.loader import render_to_string
#from django.template.loader import get_template 
#from email.mime.text import MIMEText
#from smtplib import *
#import random
import os

import docx2txt
import jellyfish
import PyPDF2

"""
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
"""

class CompararDocumentoApi(APIView):
	def post(self,request):

		documento_origen =  request.data.get('documenToExaminar')
		id_documento = request.data.get('id_biblioteca')
		documento = Biblioteca.objects.get(id_biblioteca=id_documento)
		ext = os.path.splitext(documento.documento.name)[1]
		if ext.lower() in ['.pdf']:
			textBiblioteca = ""
			textDocumentoOrigen = ""
			documento_bilioteca = open(documento.documento.path,'rb')
			#========== Convierte a texto el pdf de biblioteca ==========
			documentoLectorBiblioteca = PyPDF2.PdfFileReader(documento_bilioteca)
			numero_paginas_biblioteca_doc = documentoLectorBiblioteca.numPages

			for numero_de_pagina in range(numero_paginas_biblioteca_doc):
				#OBTENGO LA PAGINA POR NUMERO DE PAGINA 
				pageobj = documentoLectorBiblioteca.getPage(numero_de_pagina)
				#EXTRIGO EL TEXTO DE ESA PAGINA
				textBiblioteca += pageobj.extractText()
			
			
			#=========== CONVIERTE EN TEXT EL PDF A EXAMINAR ==========
			documentoLectorExaminar = PyPDF2.PdfFileReader(documento_bilioteca)
			numero_paginas_doc_examinar = documentoLectorExaminar.numPages
			for numero_de_paginas in range(numero_paginas_doc_examinar):
				pageobj = documentoLectorExaminar.getPage(numero_de_paginas)
				textDocumentoOrigen += pageobj.extractText()
			#print(textBiblioteca)
			#===========================================================
			
			result = round(jellyfish.jaro_distance(textDocumentoOrigen,textBiblioteca)*100,2)
			result_str = str(result) + "%"
			serialize = {'resultado':result_str,'documentoBiblioteca':documento.documento.name}
			return Response(serialize,status=status.HTTP_200_OK)

		if ext.lower() in ['.docx']:
			textoDocumentoOrigen = docx2txt.process(documento_origen)
			textoDocumentoBiblioteca = docx2txt.process(documento.documento)
			result = round(jellyfish.s(textoDocumentoOrigen,textoDocumentoBiblioteca)*100,2)
			result_str = str(result) + "%"
			serialize = {'resultado':result_str,'documentoBiblioteca':documento.documento.name} 
			return Response(serialize,status=status.HTTP_200_OK)

class BibliotecaApi(APIView):
	def get(self,request):
		if not request.query_params.get('id'):
			lst_biblioteca = Biblioteca.objects.filter()
		else:
			lst_biblioteca = Biblioteca.objects.filter(id_usuario=request.query_params.get('id'))
		serializer =  BibliotecaSerializer(lst_biblioteca,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
	

	def post(self,request):
		usuario = Usuario.objects.get(id_usuario=request.data.get('id'))
		nuevo_documento = Biblioteca.objects.create(
													id_usuario=usuario,
													autor=request.data.get('autor'),
													descripcion=request.data.get('descripcion'),
													documento=request.data.get('documento')
													)
		serializer = BibliotecaSerializer(nuevo_documento,many=False)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def put(self,request):
		biblioteca = Biblioteca.objects.get(id_biblioteca=request.data.get('id'))
		biblioteca.autor = request.data.get('autor')
		biblioteca.descripcion = request.data.get('descripcion')
		biblioteca.documento = request.data.get('documento')
		biblioteca.save()
		serializer = BibliotecaSerializer(biblioteca,many=False)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def delete(self,request):
		print(request.query_params.get("id"))
		biblioteca = Biblioteca.objects.get(id_biblioteca=request.query_params.get('id'))
		biblioteca.delete()
		return Response({'elemento_borrado':'Documento eliminado'},status=status.HTTP_200_OK)
