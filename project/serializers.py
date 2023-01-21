from rest_framework import serializers
from .models import Persona
from rest_framework.validators import UniqueValidator

class PersonaSerializer(serializers.ModelSerializer):
    document_type = serializers.CharField(max_length=20)
    document = serializers.IntegerField(validators=[UniqueValidator(queryset=Persona.objects.all(), message='document already exists')])
    name = serializers.CharField(max_length=20)
    lastname = serializers.CharField(max_length=20)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=Persona.objects.all(), message='email already exists')])
    hobbie = serializers.CharField(max_length=20)
    class Meta:
        model = Persona
        fields = ('id', 'document_type', 'document', 'name', 'lastname', 'email' , 'hobbie')
        
