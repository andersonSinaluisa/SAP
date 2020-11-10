from rest_framework import serializers
from .models import *

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = "__all__"