from django.db import models
from producto.models import Producto
from agenda.models import proveedor,medioDeCompra
from django.core.exceptions import ValidationError
    
class Compra(models.Model):
    fecha = models.DateField()
    proveedor = models.ForeignKey(proveedor,on_delete=models.CASCADE,blank=True, null=True)
    total = models.DecimalField(max_digits=25,decimal_places=2,blank=True,null=True,default=0)
    estado = models.BooleanField(default=False)
    
    def __str__(self):
        return f'#{self.pk} | {self.proveedor}'
    
    class Meta:
        verbose_name = 'compra'
        verbose_name_plural = 'Compras'

    def clean(self):
        if self.estado == True:
            raise ValidationError("Este producto ya fué controlado. No se puede modificar.")
        super().clean()
    
    def save(self, *args, **kwargs):
        super(Compra, self).save(*args, **kwargs)
    
    def total_compra(self):
        detalles = CompraProducto.objects.filter(compra=self)
        valor = sum(float(detalle.Costo) * float(detalle.Cantidad) for detalle in detalles)
        return valor


    def validar_compra(self):  # devuele true/false si la suma de los pagos es igual a la suma del total de los productos.
        
        total = float(self.total_compra())
        pagos = float(self.total_pagos())

        if total != pagos:
            return False
        else:
            return True

    def total_pagos(self):
        detalles = medioDePago.objects.filter(compra=self)
        valor = sum(detalle.Total for detalle in detalles)
        return valor

class CompraProducto(models.Model):
    compra  = models.ForeignKey(Compra, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Costo =  models.DecimalField(max_digits=20, decimal_places=2, default=1, blank=False, null=False)
    Cantidad = models.DecimalField(max_digits=20, decimal_places=2, default=1, blank=False, null=False)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'Productos comporados'

class medioDePago(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(medioDeCompra,on_delete=models.PROTECT,blank=False,null=False,verbose_name='medio de pago')
    Total = models.DecimalField(max_digits=25, decimal_places=2, default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'pago'
        verbose_name_plural = 'Pagos realizados' 

    def clean(self):
        super().clean()
