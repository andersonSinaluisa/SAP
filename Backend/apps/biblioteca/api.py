
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
from subprocess import Popen, PIPE

import requests
import html2text
from re import sub
from sys import stderr
from traceback import print_exc
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
    valid_extensions = ['.pdf', '.doc', '.docx',
        '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
"""


class CompararDocumentoApi(APIView):

	def readPdf(self, file):
		text = ""
		documentoLectorBiblioteca = PyPDF2.PdfFileReader(file)
		numero_paginas_biblioteca_doc = documentoLectorBiblioteca.numPages
		for numero_de_pagina in range(numero_paginas_biblioteca_doc):
			#OBTENGO LA PAGINA POR NUMERO DE PAGINA
			pageobj = documentoLectorBiblioteca.getPage(numero_de_pagina)
			#EXTRIGO EL TEXTO DE ESA PAGINA
			text += pageobj.extractText()
		return text

	def readDoc(self, file):

		text = docx2txt.process(file)
		return text

	def deleteFile(self, filename):
		path = os.path.dirname(os.path.realpath('insert/'))
		pathF = os.path.join(path, filename)
		os.remove(pathF)

	def post(self, request):

		documento_origen = request.data.get('documenToExaminar')
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
		documento_origen = open('media/insert/' + str(documento_origen), 'rb')
		documento_bilioteca = open(documento.documento.path, 'rb')
		ext2 = documento_origen.name.split('.')
		#======================================================#
		textBiblioteca = ""
		textDocumentoOrigen = ""

		if ext.lower() in ['.pdf'] and ext2[1] == 'pdf':
			textBiblioteca = self.readPdf(documento_bilioteca)
			textDocumentoOrigen = self.readPdf(documento_origen)
		elif ext.lower() in ['.pdf'] and ext2[1] == 'docx':
			textBiblioteca = self.readPdf(documento_bilioteca)
			textDocumentoOrigen = self.readDoc(documento_origen)
		elif ext.lower() in ['.docx'] and ext2[1] == 'pdf':
			textBiblioteca = self.readDoc(documento_bilioteca)
			textDocumentoOrigen = self.readPdf(documento_origen)
		elif ext.lower() in ['.docx'] and ext2[1] == 'docx':
			textBiblioteca = self.readDoc(documento_bilioteca)
			textDocumentoOrigen = self.readDoc(documento_origen)

		textBiblioteca = textBiblioteca.strip()
		textDocumentoOrigen = textDocumentoOrigen.strip()

		#===========================================================#
		#============ELIMINA EL DOCUMENTO SUBIDO===============#
		self.deleteFile(str(documento_origen.name))
		#===================OBTIENE EL NUMERO DE LINEAS SEPARADAS POR PUNTOS====#
		textBiblioteca = TextBlob(textBiblioteca)
		textDocumentoOrigen = TextBlob(textDocumentoOrigen)

		#==================CREA UN CONTADOR Y UN STRING PARA EL TEXTO DE SALIDA =========================#
		salida = ''
		salida2 = ''
		count = 0
		n_words_origen = 0

		n_words_biblioteca = 0
		for a in textDocumentoOrigen.sentences:
			for i in textBiblioteca.sentences:
				a = str(a)
				i = str(i)
				for x, palabra in enumerate(a):
					for y, palabra2 in enumerate(i):
						n_words_biblioteca = n_words_biblioteca + 1
						if x == y:
							if palabra == palabra2:
								count = count+1
								salida += palabra
								salida2 += palabra2
					n_words_origen = n_words_origen+1

		result = round(jellyfish.jaro_distance(
		    str(textDocumentoOrigen), str(textBiblioteca))*100, 2)

		salida = str(salida)
		salida2 = str(salida2)
		result_str = str(result) + "%"
		serialize = {'resultado': result_str, 'documentoBiblioteca': documento.documento.name,
                    'corpus_text': salida, 'corpus_text1': salida2}

		return Response(serialize, status=status.HTTP_200_OK)


class BibliotecaApi(APIView):
	def get(self, request):
		if not request.query_params.get('id'):
			lst_biblioteca = Biblioteca.objects.filter()
		else:
			lst_biblioteca = Biblioteca.objects.filter(
			    id_usuario=request.query_params.get('id'))
		serializer = BibliotecaSerializer(lst_biblioteca, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		usuario = Usuario.objects.get(id_usuario=request.data.get('id'))
		nuevo_documento = Biblioteca.objects.create(
                    id_usuario=usuario,
                    autor=request.data.get('autor'),
                    descripcion=request.data.get('descripcion'),
                    documento=request.data.get('documento')
                )
		serializer = BibliotecaSerializer(nuevo_documento, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request):
		biblioteca = Biblioteca.objects.get(id_biblioteca=request.data.get('id'))
		biblioteca.autor = request.data.get('autor')
		biblioteca.descripcion = request.data.get('descripcion')
		biblioteca.documento = request.data.get('documento')
		biblioteca.save()
		serializer = BibliotecaSerializer(biblioteca, many=False)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request):
		print(request.query_params.get("id"))
		biblioteca = Biblioteca.objects.get(
		    id_biblioteca=request.query_params.get('id'))
		biblioteca.delete()
		return Response({'elemento_borrado': 'Documento eliminado'}, status=status.HTTP_200_OK)


class DocumentoRef(APIView):

	def readPdf(self, file):
		text = ""
		documentoLectorBiblioteca = PyPDF2.PdfFileReader(file)
		numero_paginas_biblioteca_doc = documentoLectorBiblioteca.numPages
		for numero_de_pagina in range(numero_paginas_biblioteca_doc):
			#OBTENGO LA PAGINA POR NUMERO DE PAGINA
			pageobj = documentoLectorBiblioteca.getPage(numero_de_pagina)
			#EXTRIGO EL TEXTO DE ESA PAGINA
			text += pageobj.extractText()

		return text

	def readDoc(self, file):
		text = docx2txt.process(file)
		return text

	def deleteFile(self, filename):
		path = os.path.dirname(os.path.realpath('insert/'))
		pathF = os.path.join(path, filename)
		os.remove(pathF)

	def dehtml(self, text):
		h = html2text.HTML2Text()
		h.ignore_links = True
		return h.handle(text)

	def clearString(self, text):

		texto = ""
		for i in text:
			i.rstrip('/')
			i.rstrip('\\n')
			i.rstrip('"')
			texto += i

		return texto

	def post(self, request):

		documento_origen = request.data.get('doc')
		referencia = request.data.get('referencia')
		referencia = referencia.split(',')
		#=============SI LA CARPETA NO EXISTE LA CREA ============#
		if not os.path.exists('media/insert/'):
			os.mkdir('media/insert/')

		#=========GUARDA EL DOCUMENTO EN EL DIRECTORIO CREADO ============#
		with open('media/insert/' + str(documento_origen), 'wb+') as destination:
			for chunk in documento_origen.chunks():
				destination.write(chunk)
		#===========ABRE EL DOCUMENTO SUBIDO =============================#
		documento_origen = open('media/insert/' + str(documento_origen), 'rb')
		ext2 = documento_origen.name.split('.')
		textoOrigen = ""

		#==========VERIFICA QUE TIPO DE ARCHIVO ES==========#
		if ext2[1] == 'pdf':
			textoOrigen = self.readPdf(documento_origen)
		elif ext2[1] == 'docx':
			textoOrigen = self.readDoc(documento_origen)

		#============CREA UN TEXTBLOB DEL TEXTO EXTRAIDO DEL DOCUMENTO========#
		textoOrigen = TextBlob(textoOrigen)
		#===========INICIALIZA VALORES ===========================#
		textoSalida = ""
		textRef = ""
		listaSalida = []
		count = 0
		count1 = 0
		result = 0
		#=============RECORRE LAS REFERENCIAS ========================#
		for r in referencia:
			count = count + 1
			#===========ABRE EL CONTENIDO HTML =================#
			try:
				with urllib.request.urlopen(r) as response:
					html = response.read()
					#============OBTIENE EL TEXTO DEL HTML ======================#
					text = self.dehtml(str(html))
					#==========LO CONVIERTE EN UN OBJ TEXTBLOB ==============#
					textoSentencia = TextBlob(text)
					#===========RECORRE EL TEXTO POR ORACION ==============#
					for sentenceOrigen in textoOrigen.sentences:
						#========RECORRE EL TEXTO DEL HTML =========#
						for sentences in textoSentencia.sentences:
							palabrasOrigen = TextBlob(str(sentenceOrigen))
							palabrasSentences = TextBlob(str(sentences))
							for x, wordOrigen in enumerate(palabrasOrigen.words):
								for y, word in enumerate(palabrasSentences.words):
									print(word)
									if wordOrigen == word and x==y:
										count1 = count1 + 1
										textoSalida += wordOrigen+" "
										textRef += word+" "
									

					listaSalida.append((r, textRef, textoSalida))
					textoSalida = ""
					textRef = ""

			except :
				continue
		#============ELIMINA EL DOCUMENTO SUBIDO===============#

		result = (count1/count)*0.10
		if result>100:
			result=100
		
		if count1==0:
			result=0

		result_str = str(result)+"%"
		print(result_str)
		serialize = {'resultado': result_str,
                    'corpus_text': listaSalida, 'corpus_text1': textRef}
		self.deleteFile(str(documento_origen.name))
		return Response(serialize, status=status.HTTP_200_OK)
