from .models import *
def usuario_session(request):
	usuario = Usuario()
	if 'usuario' in request.session:
		usuario = Usuario.objects.get(id_usuario=request.session.get('usuario'))
	return {'usuario':usuario}
	