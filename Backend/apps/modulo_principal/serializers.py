from .models import *
from rest_framework import serializers

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"

class PersonaSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("nombres","apellidos","identificacion","foto")

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario','correo','clave','fecha_creacion','id_persona')
    id_persona = PersonaSerializer()


class UsuarioSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario','correo','id_persona')
    id_persona = PersonaSessionSerializer()

