from django.shortcuts import render,redirect
from .models import *
import hashlib

# Create your views here.


def base(request):
	context = {}
	return render(request,'base.html',context)

def error_template(request):
	context = {}
	return render(request,'modulo_principal_templates/Error_servidor.html',context)


def index(request):
	id_usuario = 0
	usuario = None
	try:
		if 'usuario' in request.session:
			return render(request,'modulo_principal_templates/index.html')
		else:
			return redirect('login')
	except Exception as e:
		print(e)
		return redirect('error')
	

def login(request):
	usuario = None
	try:
		if 'usuario' in request.session:
			return redirect('index')
		if request.method == 'POST':
			contra = request.POST.get('clave')
			h = hashlib.new("sha1")
			contra = str.encode(contra)
			h.update(contra)
			#Usuario.objects.get() nos permite hacer una consulta a la base de datos para saber si el usuario esta registrado.
			usuario = Usuario.objects.filter(correo=request.POST.get('correo'),clave=h.hexdigest())
			if usuario.exists():
				usuario = Usuario.objects.get(correo=request.POST.get('correo'),clave=h.hexdigest())
				request.session['usuario'] = usuario.id_usuario
				return redirect('index')
		return render(request,'modulo_principal_templates/login.html',{})
	except Exception as e:
		raise e
	

def cerrar_sesion(request):
	try:
		if 'usuario' in request.session:
			del request.session['usuario']
			return redirect('login')
	except Exception as e:
		print(e)
		return redirect('error')

def crear_usuario(request):
	usuario = None
	persona = None
	contra  = None

	try:
		#Si la solicitud es post significa que el cliente envio un formulario a esta vista
		if request.method == 'POST':
			#guardo la contraseña ingresada en una variable llamada contra
			contra = request.POST.get('clave')
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
										 nombres=request.POST.get('nombres'),
										 apellidos=request.POST.get('apellidos'),
										 identificacion=request.POST.get('identificacion'),
										 foto=request.FILES['foto']
										 )
			#Creo un registro en mi bases de datos de Usuario y lo guardo en la variable usuario
			#las campos que son claves fonaneas como es el caso de id_persona, el requiere un objeto de esa tabla, asi que ahi guardo el objeto persona
			#que se acaba de crear arriba
			usuario = Usuario.objects.create(
											 id_persona=persona,
											 correo=request.POST.get('correo'),
											 #h.hexdigest retorna la contraseña encriptada
											 clave=h.hexdigest()
											 )
			#Si el usuario se creo sin problemas, Me redirigo al login
			if usuario:
				return redirect('login')
		#Aqui la peticion es GET, asi que solo renderiza el formulario para crear usuarios.
		return render(request,'modulo_principal_templates/crear_usuario.html',{})
	except Exception as e:
		print(e)
		return redirect('error')
		
		