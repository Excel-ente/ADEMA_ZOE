# # # # # # # # # # # # # # # # # # # # # #
#   Sistema ADEMA
#
#      
# # # # # # # # # # # # # # # # # # # # # #
from django.db import models
from contaduria.models import cuentasContables

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Familia(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,blank=True,null=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    apellido = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200,blank=True,null=True)
    telefono = models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        if self.apellido:   
            nombre = self.nombre + ", " + self.apellido
        else:
            nombre = self.nombre
        return nombre
    
class Proveedor(models.Model):
    empresa = models.CharField(max_length=200, null=False, blank=False)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200,blank=True,null=True)
    telefono = models.CharField(max_length=20,blank=True,null=True)
    
    def __str__(self):
        return f'{self.empresa} - {self.nombre}'
    
class Configuracion(models.Model):
    empresa = models.CharField(max_length=200,unique=True, null=False, blank=False)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    ganancia_minorista = models.DecimalField(max_digits=5,decimal_places=2,blank=False,null=False, default=0)
    ganancia_caja = models.DecimalField(max_digits=5,decimal_places=2,blank=False,null=False, default=0)
    ganancia_mayorista = models.DecimalField(max_digits=5,decimal_places=2,blank=False,null=False, default=0)
    venta_negativa = models.BooleanField(default=True)
    v001 = models.BooleanField(default=True)
    venta_por_caja = models.BooleanField(default=True) # True = seleccionar como default Venta por caja 

class AsignacionDeCaja(models.Model):
    pass

class MedioDeCompra(models.Model):
    cuenta = models.ForeignKey(cuentasContables, on_delete=models.SET_NULL ,null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'

class MedioDePago(models.Model):
    cuenta = models.ForeignKey(cuentasContables, on_delete=models.SET_NULL ,null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}'
    
class CategoriaGasto(models.Model):
    descripcion = models.CharField(max_length=255,unique=True,blank=False,null=False)
    cuenta = models.ForeignKey(cuentasContables,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.descripcion
    
class Gasto(models.Model):
    fecha = models.DateField(blank=False,null=True)
    categoria = models.ForeignKey(CategoriaGasto,on_delete=models.SET_NULL,blank=False,null=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False)
    total = models.DecimalField(max_digits=20,decimal_places=2,blank=False,null=False)

    def __str__(self):
        msg = f'{self.categoria} | {self.descripcion} | ${self.total}'
        return msg
    
class Retiro(models.Model):
    fecha = models.DateField(blank=False,null=True)
    descripcion = models.CharField(max_length=255, null=False, blank=False)
    total = models.DecimalField(max_digits=20,decimal_places=2,blank=False,null=False)

    def __str__(self):
        msg = f'{self.fecha} | {self.descripcion} | ${self.total}'
        return msg