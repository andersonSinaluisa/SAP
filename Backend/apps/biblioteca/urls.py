from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .api import *
from rest_framework import routers

#router = routers.SimpleRouter()
#router.register('PaisApi',PaisApi)

urlpatterns = [
    path('listar_documentos/',Listar_biblioteca.as_view(),name='listar_documentos'),
    path('crear_documento/',crear_documento,name='crear_documento'),
  	path('BibliotecaApi/',BibliotecaApi.as_view(),name='BibliotecaApi'),
    path('CompararDocumentoApi/',CompararDocumentoApi.as_view(),name='CompararDocumentoApi'),
    path('ComparaRef/',DocumentoRef.as_view(),name='ComparaRef')
  ]