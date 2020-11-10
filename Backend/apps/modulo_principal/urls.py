from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework import routers
from .api import *

#router = routers.SimpleRouter()
#router.register('PaisApi',PaisApi)

urlpatterns = [
    path('base/',base,name='base'),
    path('index/',index,name='index'),
    path('error_servidor/',error_template,name='error'),
    path('',login,name='login'),
    path('crear_usuario/',crear_usuario,name='crear_usuario'),
    path('cerrar_sesion/',cerrar_sesion,name='cerrar_sesion'),
  	path('UsuarioApi/',UsuarioApi.as_view(),name='UsuarioApi'),
  	path('SeguridadApi/',SeguridadApi.as_view(),name='SeguridadApi'),

  ]

#urlpatterns += router.urls