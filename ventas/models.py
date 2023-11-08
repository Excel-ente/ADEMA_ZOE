from django.db import models
from django.core.exceptions import ValidationError
from inventario.models import Producto
from administracion.models import Cliente
from administracion.models import Configuracion,MedioDePago

from django.db.models.signals import post_save
from django.dispatch import receiver
from reportes.models import reporteVentas  # Asegúrate de importar tu modelo de reportes


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, default=1, blank=True, null=True)
    estado = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True,default=0)
    
    def clean(self):

        if self.estado == True:  # validacion que no se este haciendo modificaciones
            raise ValidationError("No se puede modificar una venta confirmada. Por favor generar una anulacion de venta.")
        
        super().clean()
    
    def validar_venta(self):  # devuele true/false si la suma de los pagos es igual a la suma del total de los productos.
        
        total = float(self.total_venta())
        pagos = float(self.total_pagos())

        if total != pagos:
            return False
        else:
            return True

    def save(self, *args, **kwargs):
        self.total = float(round(self.total_venta(),2))
        super(Venta, self).save(*args, **kwargs)
    
    def total_venta(self):
        detalles = DetalleVenta.objects.filter(venta=self)
        valor = sum(detalle.total for detalle in detalles)
        return valor

    def total_pagos(self):
        detalles = MedioDePago.objects.filter(venta=self)
        valor = sum(detalle.total for detalle in detalles)
        return valor

    def __str__(self):
        formateo =  f'Venta # {self.pk}'
        return formateo

class MedioDePago(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(MedioDePago,on_delete=models.SET_NULL,default=1,blank=True,null=True)
    total = models.DecimalField(max_digits=25, decimal_places=2, default=0, blank=True, null=True)

    def clean(self):
        
        if self.total <= 0:
            raise ValidationError(f"Ingrese un importe mayor o igual a $ 0.")

        super().clean()

    class Meta:
        verbose_name = 'pago de cliente'
        verbose_name_plural ='Pagos de clientes' 

class DetalleVenta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta_por_caja = models.BooleanField(default=False)
    cantidad = models.DecimalField(max_digits=25, decimal_places=2,default=1)
    descuento = models.DecimalField(max_digits=25,decimal_places=2,default=0)
    total = models.DecimalField(max_digits=25,decimal_places=2,default=0)

    def total_unitario(self):

        # tipo de descuento 0 es en % y 1 es para que sea por importe.
        tipo_descuento = 0

        if tipo_descuento == 0:
            precio = float(self.producto.precio_unitario())
            descuento = (precio * float(self.descuento) / 100)
            calculo = float(precio - descuento)
        else:
            calculo = float(self.precio - self.descuento)

        return calculo
    
    def total_detalles(self):

        # tipo de descuento 0 es en % y 1 es para que sea por importe.
        tipo_descuento = 0
        total = 0 

        if tipo_descuento == 0:
            precio = float(self.producto.precio_unitario())
            descuento = (precio * float(self.descuento) / 100)
            if self.venta_por_caja == False:
                calculo = float(precio - descuento) * float(self.cantidad)
            else:
                calculo = float(precio - descuento) * float(self.cantidad) * float(self.producto.unidades_por_caja)
            total += calculo

        return total

    def clean(self):
        

        # tipo de descuento 0 es en % y 1 es para que sea por importe.
        tipo_descuento = 0

        if tipo_descuento == 0:

            if self.descuento > 100:
                raise ValidationError("El descuento no puede ser superior a 100%.")
            
            if self.descuento < 0:
                raise ValidationError("El descuento debe ser superior o igual a 0%.")
        

        # Verificacion de stock
        config = Configuracion.objects.first()

        venta_negativa = config.venta_negativa

            
        if self.cantidad <= 0:
            raise ValidationError(f"Ingrese un importe mayor a 0.")
            
        if venta_negativa == False:
            stock = self.producto.en_stock
            if self.cantidad > stock:
                raise ValidationError(f"El stock disponible es inferior. Stock disponible actual: {stock}")

        super().clean()
    
    def save(self, *args, **kwargs):

        # tipo de descuento 0 es en % y 1 es para que sea por importe.
        tipo_descuento = 0

        if tipo_descuento >= 0:

            if self.descuento > 100:
                raise ValidationError("El descuento no puede ser superior a 100%.")
            
            precio = float(self.producto.precio_unitario())
            descuento = (precio * float(self.descuento) / 100)

            if self.venta_por_caja == False:
                self.total = float(precio - descuento) * float(self.cantidad)
            else:
                self.total = float(precio - descuento) * float(self.cantidad) * float(self.producto.unidades_por_caja)


        super(DetalleVenta, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'detalle de venta'
        verbose_name_plural ='Ventas por producto' 

@receiver(post_save, sender=Venta)
def actualizar_totales_reporte(sender, instance, **kwargs):

    # cargar reporte ventas

    fecha_venta = instance.fecha

    ventas = float(instance.total_venta())

    iva_21 = float(1.21)
    iva_10_5 = float(1.105)
    iibb = float(1.05)

    reporte, created = reporteVentas.objects.get_or_create(fecha=fecha_venta)
    reporte.ventas = ventas
    reporte.total_minorista = 0
    reporte.total_mayorista = 0
    reporte.total_iva_21 = ventas - (ventas / iva_21)
    reporte.total_iva_10_5 = ventas - (ventas / iva_10_5)
    reporte.total_iibb = ventas - (ventas / iibb)
    reporte.save()

# Luego, registra la señal de actualización en la parte inferior de tu archivo models.py
post_save.connect(actualizar_totales_reporte, sender=Venta)
