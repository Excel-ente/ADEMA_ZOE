from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from administracion.models import Categoria,Proveedor,Familia
from administracion.models import Configuracion
from decimal import Decimal


# Validador personalizado para el tamaño de la imagen
def validate_image_size(value):
    width, height = value.width, value.height
    if width != 500 or height != 500:
        raise ValidationError('La imagen debe ser de 500x500 píxeles.')


class Producto(models.Model):
    codigo = models.CharField(max_length=100,unique=True,blank=False,null=False)
    nombre = models.CharField(max_length=100,blank=False,null=False)
    descripcion = models.CharField(max_length=200,blank=True,null=True)
    imagen = models.ImageField(
        upload_to='img/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']), validate_image_size]
    )
    en_stock = models.DecimalField(max_digits=25, decimal_places=2,blank=True,null=True)
    costo = models.DecimalField(max_digits=25, decimal_places=2,default=0 ,blank=True,null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    Proveedor = models.ForeignKey(Proveedor, default=1,on_delete=models.SET_NULL, null=True, blank=True)
    familia = models.ForeignKey(Familia, on_delete=models.SET_NULL, null=True, blank=True)
    unidades_por_caja = models.DecimalField(default=1,max_digits=25, decimal_places=2,blank=True,null=True)
    habilitar_caja = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nombre).upper() + " " + self.descripcion

    def save(self, *args, **kwargs):
        if self.en_stock:
            pass
        else:
            self.en_stock = 0
        
        super(Producto, self).save(*args, **kwargs)

    def image_tag(self):
        if self.imagen:
            return mark_safe(f'<img src="{self.imagen.url}" width="100" />')
    
    image_tag.short_description = 'Imagen Actual'
    image_tag.allow_tags = True

    def precio_unitario(self):
        config = Configuracion.objects.first()

        ganancia_minorista = Decimal(config.ganancia_minorista)
        costo = Decimal(self.costo)
        precio = costo + (costo * ganancia_minorista / Decimal(100))

        return precio

    def ingresar_stock(self, cantidad):
        """
        Aumenta el stock del producto en la cantidad especificada.

        Args:
            cantidad (decimal): La cantidad a agregar al stock.

        Raises:
            ValidationError: Si la cantidad es negativa.
        """
        if cantidad < 0:
            raise ValidationError("La cantidad debe ser mayor o igual a cero.")
        self.en_stock += cantidad
        self.save()

    def descontar_stock(self, cantidad):
        """
        Reduce el stock del producto en la cantidad especificada.

        Args:
            cantidad (decimal): La cantidad a restar del stock.

        """
        config = Configuracion.objects.first()

        venta_negativa = config.venta_negativa
        

        if venta_negativa == False:
            if cantidad < 0:
                raise ValidationError("La cantidad debe ser mayor o igual a cero.")
            if self.en_stock - cantidad < 0:
                raise ValidationError("No hay suficiente stock disponible.")
        else:
            self.en_stock -= cantidad

        self.save()