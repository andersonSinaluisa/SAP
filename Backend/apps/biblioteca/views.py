from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import *
from apps.modulo_principal.models import *
# Create your views here.


class Listar_biblioteca(ListView):
    model = Biblioteca
    template_name = 'biblioteca_templates/listar_documentos.html'
    queryset = Biblioteca.objects.filter()
    context_object_name = 'documentos'
    def get_queryset(self):
    	return Biblioteca.objects.filter(id_usuario=self.request.session.get('usuario'))


def crear_documento(request):
	try:
		if 'usuario' in request.session:
			if request.method == 'POST':
				usuario = Usuario.objects.get(id_usuario=request.session.get('usuario'))
				documento = Biblioteca.objects.create(
													   id_usuario=usuario,	
													   autor=request.POST.get('autor'),
													   descripcion=request.POST.get('descripcion'),
													   documento=request.FILES['documento']
													 )
				if documento:
					return redirect('listar_documentos')
			return render(reques,'biblioteca_templates/crear_documento.html')
		else:
			return redirect('login')

	except Exception as e:
		return redirect('error')