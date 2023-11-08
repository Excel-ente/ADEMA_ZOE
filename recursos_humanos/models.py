from django.db import models
from django.contrib.auth.models import User  # Importa el modelo de usuario de Django

class Empleado(models.Model):
    legajo = models.CharField(max_length=50, unique=True, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación uno a uno con el modelo de usuario de Django
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    foto = models.ImageField(upload_to='empleados/', blank=True, null=True)  # Para almacenar una foto del empleado
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    fecha_de_ingreso = models.DateField(blank=True, null=True)
    fecha_de_egreso = models.DateField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"