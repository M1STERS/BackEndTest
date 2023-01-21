from django.db import models

# Create your models here.
class Persona(models.Model):
    document_type = models.CharField(max_length=20)
    document = models.BigIntegerField()
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    hobbie = models.CharField(max_length=20)
