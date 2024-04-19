from django.db import models
from django.contrib.auth.models import User
# Create your models here.

OPCIONES_RAZA= [
    ('d','Perro'),
    ('c','Gato'),
    ('h','Hamster'),
    ('p','Perico'),
]

OPCIONES_GENERO= [
    ('m','Macho'),
    ('h','Hembra'),
]


class Mascota(models.Model):
    nombre=models.CharField(max_length=300)
    especie=models.CharField(max_length=30, choices=OPCIONES_RAZA)
    edad=models.IntegerField()
    genero=models.CharField(max_length=30,choices=OPCIONES_GENERO)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre}'