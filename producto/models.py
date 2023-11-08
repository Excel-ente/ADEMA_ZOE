from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Validador personalizado para el tamaño de la imagen
def validate_image_size(value):
    width, height = value.width, value.height
    if width != 500 or height != 500:
        raise ValidationError('La imagen debe ser de 500x500 píxeles.')


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(
        upload_to='img/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']), validate_image_size]
    )
    costo = models.DecimalField(verbose_name="Costo unit.",max_digits=25, decimal_places=2,default=0 ,blank=True,null=True)
    precio_usd = models.DecimalField(verbose_name="Costo en Dolares",default=0,max_digits=25, decimal_places=2,blank=True,null=True)
    precio = models.DecimalField(verbose_name="Precio Venta",default=0,max_digits=25, decimal_places=2)

    precio_bs = models.DecimalField(verbose_name="Bolivianos",default=0,max_digits=25, decimal_places=2)
    en_stock = models.DecimalField(max_digits=25, default=0, decimal_places=2)


    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre + " " + self.descripcion

    def save(self, *args, **kwargs):
        super(Producto, self).save(*args, **kwargs)

