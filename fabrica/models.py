# ---------------- ADEMA ------------------
# Sistema desarrollado por Kevin Turkienich 2023
# Contacto: kevin_turkienich@outlook.com
# 
# ----------------------------------------------

# ---------------- IMPORTACIONES DE MODULOS ----------------->
import datetime
from decimal import Decimal, DivisionByZero
from django.db import models
from django.core.exceptions import ValidationError
from administracion.models import Cliente,Proveedor,Categoria
from inventario.models import Producto
# ------------------------------------------------------------------

# ---------------------- TABLAS DE DATOS --------------------------------------->
UnidadDeMedida = [
    ("Unidades","Unidades"),
    ("Kilogramos","Kilogramos"),
    ("Litros","Litros"),
    ("Onzas","Onzas"),
    ("Libras","Libras"),
]
Estado = [
    ("Pendiente","Pendiente"),
    ("Controlada","Controlada"),
]
Estado_orden = [
    ("Pendiente","Pendiente"),
    ("En curso","En curso"),
    ("Finalizada","Finalizada"),
]
Medio_De_Pago = [
    ("Efectivo","Efectivo"),
    ("Transferencia","Transferencia"),
    ("Cuenta Corriente","Cuenta Corriente"),
]
UnidadDeMedidaSalida = [
    ("Unidades","Unidades"),
    ("Gramos","Gramos"),
    ("Mililitros","Mililitros"),
    ("Onzas","Onzas"),
    ("Libras","Libras"),
]
# ------------------------------------------------------------------
# ---------------- MODELADO DE BASES DE DATOS --------------------------------->

class gastosAdicionales(models.Model):
    nombre  = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        return self.nombre
# ------------------------------------------------------------------
# ------------------------------------------------------------------  
class Ingrediente(models.Model):
    producto = models.CharField(max_length=120, null=False, blank=False)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE,blank=True,null=True)
    detalle = models.TextField(null=True, blank=True)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=False, null=False)
    unidad_medida = models.CharField(max_length=10, choices=UnidadDeMedida, default="Unidades", null=False, blank=False)
    costo = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=False, null=False)
    ultima_actualizacion = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = 'ingrediente'
        verbose_name_plural ='Ingredientes' 

    def __str__(self):
        cadena = f'{self.producto} (x {self.cantidad} {self.unidad_medida})'
        return cadena


    def save(self, *args, **kwargs):
        super(Ingrediente, self).save(*args, **kwargs)
# ------------------------------------------------------------------
# ------------------------------------------------------------------
class Receta(models.Model):
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE,null=False,blank=False)
    porciones=models.DecimalField(max_digits=8,decimal_places=2,default=1,blank=False,null=False)
    detalle=models.TextField(null=True,blank=True) 
    fecha_de_actualizacion = models.DateField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return f'{self.producto}'
    
    def clean(self):
        super().clean()

    class Meta:
        verbose_name = 'receta'
        verbose_name_plural ='Recetas' 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
# ------------------------------------------------------------------ 
# ------------------------------------------------------------------ 
class ingredientereceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente  = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    unidad_de_medida = models.CharField(max_length=10, choices=UnidadDeMedidaSalida, default="Unidades", null=False, blank=False)
    cantidad = models.DecimalField(max_digits=20, decimal_places=2, default=1, blank=False, null=False)

    class Meta:
        verbose_name = 'ingrediente'
        verbose_name_plural ='Productos incluidos en la receta' 

    def __str__(self):
        return f'{self.receta.producto}'
    
    def clean(self):

        if self.cantidad <= 0:
            raise ValidationError("Por favor ingrese una cantidad superior a 0.")
        
        # validar los gramajes

        super().clean()

    def save(self, *args, **kwargs):
        super(ingredientereceta,self).save(*args, **kwargs)
# ------------------------------------------------------------------
# ------------------------------------------------------------------ 
class adicionalreceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    adicional  = models.ForeignKey(gastosAdicionales, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=20, decimal_places=2,blank=False,null=False)
