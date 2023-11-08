from django.db import models
from django.core.exceptions import ValidationError
from inventario.models import Producto
from administracion.models import Proveedor,MedioDeCompra

MEDIOS_DE_PAGO = [
    ("Efectivo","Efectivo"),
    ("Transferencia","Transferencia"),
    ("Cuenta Corriente","Cuenta Corriente"),
]

class Compra(models.Model):
    fecha = models.DateField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=False, null=False)
    estado = models.BooleanField(default=False)

    def clean(self):

        if self.estado == True:  # validacion que no se este haciendo modificaciones
            raise ValidationError("No se puede modificar una compra confirmada. Por favor generar una anulacion de compra.")
        
        super().clean()
    
    def validar_compra(self):  # devuele true/false si la suma de los pagos es igual a la suma del total de los productos.
        
        total = float(self.total_compra())
        pagos = float(self.total_pagos())

        if total != pagos:
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        super(Compra, self).save(*args, **kwargs)
    
    def total_compra(self):
        detalles = DetalleCompra.objects.filter(compra=self)
        valor = sum(detalle.total for detalle in detalles)
        return valor

    def total_pagos(self):
        detalles = MedioDePago.objects.filter(compra=self)
        valor = sum(detalle.total for detalle in detalles)
        return valor

    def __str__(self):
        formateo =  f'Compra # {self.pk}'
        return formateo



    
class MedioDePago(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    medio = models.CharField(max_length=25, choices=MEDIOS_DE_PAGO, default='Efectivo')
    cuenta = models.ForeignKey(MedioDeCompra,on_delete=models.SET_NULL,blank=True,null=True)
    total = models.DecimalField(max_digits=25, decimal_places=2, default=0, blank=True, null=True)

class DetalleCompra(models.Model):
    fecha = models.DateField(auto_now_add=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=25, decimal_places=2,default=1)
    precio = models.DecimalField(max_digits=25,decimal_places=2,default=0)
    descuento = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    total = models.DecimalField(max_digits=25,decimal_places=2,default=0)

    def clean(self):

        # tipo de descuento 0 es en % y 1 es para que sea por importe.
        tipo_descuento = 0

        if tipo_descuento == 0:  # validacion que no se este haciendo modificaciones

            if self.descuento > 100:
                raise ValidationError("El descuento no puede ser superior a 100%.")
            
            if self.descuento < 0:
                raise ValidationError("El descuento debe ser superior o igual a 0%.")
        
        super().clean()
    
    
    def save(self, *args, **kwargs):

        # tipo de descuento 0 es en % y 1 es para que sea por importe.
        tipo_descuento = 0

        if tipo_descuento == 0:

            if self.descuento > 100:
                raise ValidationError("El descuento no puede ser superior a 100%.")
            
            precio = float(self.precio)
            descuento = (precio * float(self.descuento) / 100)
            self.total = float(precio - descuento) * float(self.cantidad)
        else:
            self.total = float((self.precio * self.cantidad) - self.descuento)

        super(DetalleCompra, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'detalle de comrpa'
        verbose_name_plural = 'Compras por porducto' 