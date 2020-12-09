
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
from difflib import SequenceMatcher
from textblob import TextBlob
import docx2txt
import jellyfish
import PyPDF2
# -*- coding: utf-8 -*-
"""
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
"""

class CompararDocumentoApi(APIView):
    	

	def readPdf(self,file):
		text =""
		documentoLectorBiblioteca = PyPDF2.PdfFileReader(file)
		numero_paginas_biblioteca_doc = documentoLectorBiblioteca.numPages
		for numero_de_pagina in range(numero_paginas_biblioteca_doc):
			#OBTENGO LA PAGINA POR NUMERO DE PAGINA 
			pageobj = documentoLectorBiblioteca.getPage(numero_de_pagina)
			#EXTRIGO EL TEXTO DE ESA PAGINA
			text += pageobj.extractText()
		return text

	
	def readDoc(self,file):
    		
			text = docx2txt.process(file)
			return text

	def deleteFile(self,filename):
			path = os.path.dirname(os.path.realpath('insert/'))
			pathF = os.path.join(path,filename)
			os.remove(pathF)



	def post(self,request):

		documento_origen =  request.data.get('documenToExaminar')
		id_documento = request.data.get('id_biblioteca')
		documento = Biblioteca.objects.get(id_biblioteca=id_documento)
		ext = os.path.splitext(documento.documento.name)[1]
		#=========SI NO EXISTE EL DIRECTORIO LO CREA ===============#
		if not os.path.exists('media/insert/'):
            			os.mkdir('media/insert/')
		
		#=========GUARDA EL DOCUMENTO EN EL DIRECTORIO CREADO ============#
		with open('media/insert/' + str(documento_origen), 'wb+') as destination:
                        for chunk in documento_origen.chunks():
                            destination.write(chunk)

		#==========ABRE EL DOCUMENTO GUARDADO ===============#
		documento_origen = open('media/insert/' + str(documento_origen),'rb')
		documento_bilioteca = open(documento.documento.path,'rb')
		ext2 = documento_origen.name.split('.')
		#======================================================#
		textBiblioteca = ""
		textDocumentoOrigen = ""

		if ext.lower() in ['.pdf'] and ext2[1]=='pdf':
					textBiblioteca=self.readPdf(documento_bilioteca)
					textDocumentoOrigen=self.readPdf(documento_origen)
		elif ext.lower() in ['.pdf'] and ext2[1]=='docx':
					textBiblioteca=self.readPdf(documento_bilioteca)
					textDocumentoOrigen=self.readDoc(documento_origen)
		elif ext.lower() in ['.docx'] and ext2[1]=='pdf':
					textBiblioteca=self.readDoc(documento_bilioteca)
					textDocumentoOrigen=self.readPdf(documento_origen)
		elif ext.lower() in ['.docx'] and ext2[1]=='docx':
					textBiblioteca=self.readDoc(documento_bilioteca)
					textDocumentoOrigen=self.readDoc(documento_origen)
    
		textBiblioteca=textBiblioteca.strip()
		textDocumentoOrigen=textDocumentoOrigen.strip()
		
		#===========================================================#
		#============ELIMINA EL DOCUMENTO SUBIDO===============#
		self.deleteFile(str(documento_origen.name))
		#===================OBTIENE EL NUMERO DE LINEAS SEPARADAS POR PUNTOS====#
		textBiblioteca = TextBlob(textBiblioteca)
		textDocumentoOrigen=TextBlob(textDocumentoOrigen)
		
	
		
		#==================CREA UN CONTADOR Y UN STRING PARA EL TEXTO DE SALIDA =========================#
		salida =''
		salida2 =''
		count=0
		#========================RECORRE EL TEXTO DE LA BIBLIOTECA ==================#
		for a in textDocumentoOrigen.sentences:
			#================ RECORRE EL TEXTO DE EL DOC =======#
			for i in textBiblioteca.sentences:
				
				
				if a ==i:
						count=count+1
						salida += str(a)
						salida2 += str(i)
		
		print(count)
		sizeOrigen = len(textDocumentoOrigen.sentences)
		sizeBiblioteca = len(textBiblioteca.sentences)
		if count==0:
    			result=0
		else:
			result = ((sizeBiblioteca+sizeBiblioteca/2)/count)*100
		
		if result >100:
    			result=100

		salida=str(salida)
		salida2=str(salida2)
		result_str = str(result) + "%"
		serialize = {'resultado':result_str,'documentoBiblioteca':documento.documento.name,'corpus_text':salida,'corpus_text1':salida2} 

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
