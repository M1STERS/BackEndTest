from project.serializers import PersonaSerializer
from .models import Persona
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

class PersonaViewSet(ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonaSerializer