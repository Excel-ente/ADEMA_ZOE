from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import FileExtensionValidator

CAJA = [
        ('caja_1', 'caja_1'),
        ('caja_2', 'caja_2'),
    ]

TICKET = [
        ('comandera', 'comandera'),
        ('a4', 'a4'),
    ]

# Validador personalizado para el tamaño de la imagen
def validate_image_size(value):
    width, height = value.width, value.height
    if width != 500 or height != 500:
        raise ValidationError('El logo debe ser de 500x500 píxeles.')

class Asignacion(models.Model):

    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    caja = models.CharField(max_length=10, choices=CAJA, default='caja_1')
    
    def __str__(self):
        return self.usuario.first_name

    class Meta:
        verbose_name = 'Asignacion de caja'
        verbose_name_plural ='Asignaciones de caja' 

# Definir un diccionario con el nombre de los meses en español
meses = {
    1: "ENERO",
    2: "FEBRERO",
    3: "MARZO",
    4: "ABRIL",
    5: "MAYO",
    6: "JUNIO",
    7: "JULIO",
    8: "AGOSTO",
    9: "SEPTIEMBRE",
    10: "OCTUBRE",
    11: "NOVIEMBRE",
    12: "DICIEMBRE",
}

def formatear_fecha(fecha):
    dia = fecha.day
    mes_numero = fecha.month
    mes_nombre = meses[mes_numero]
    return f"{dia} De {mes_nombre}"

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(unique=True,max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    

    
    def __str__(self):
        return self.nombre
    
class proveedor(models.Model):
    Empresa=models.CharField(max_length=120,null=False,blank=False) 
    NombreApellido=models.CharField(max_length=120,null=False,blank=False) 
    Direccion=models.CharField(max_length=120,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Telefono=models.CharField(max_length=120,null=False,blank=False)
    UltimaModificacion = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Usuario = models.CharField(max_length=120, null=True, blank=True)   

    def __str__(self):
        return self.Empresa
    
    class Meta:
        verbose_name = 'proveedor' # Como se va a nombrar el objeto de la instancia
        verbose_name_plural ='Proveedores' # Como se nombra el modelo

class Vendedor(models.Model):
    codigo = models.CharField(max_length=200, null=True, blank=True)
    nombre = models.CharField(unique=True,max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class TipoGasto(models.Model):
    descripcion = models.CharField(max_length=255,unique=True,blank=False,null=False)

    def __str__(self):
        return self.descripcion
    
class Gasto(models.Model):
    fecha = models.DateField(blank=False,null=True)
    categoria = models.ForeignKey(TipoGasto,on_delete=models.SET_NULL,blank=False,null=True)
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

class Configuracion(models.Model):
    empresa = models.CharField(max_length=255, null=False, blank=False)
    direccion = models.CharField(max_length=255, null=False, blank=False)
    telefono = models.CharField(max_length=255, null=False, blank=False)
    tipoTicket = models.CharField(max_length=255,choices=TICKET,default="comandera",blank=False,null=False)
    logo = models.ImageField(
        upload_to='img/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']), validate_image_size]
    )
    def __str__(self):
        msg = f'{self.empresa}'
        return msg
    
    class Meta:
        verbose_name = 'Configuracion'
        verbose_name_plural ='Configuraciones' 

# -----------------------------------------------------------------------------
# Metodos para acceder a los valores de forma dinamica
#   configuracion.moneda()   ---> devuelve la moneda en la que se trabaja
#
class medioDeCompra(models.Model):
    Nombre = models.CharField(max_length=200, null=True, blank=True)


    def clean(self): # Metodo para verificar algun  campo antes de guardar.
        super().clean()

    def __str__(self): # Como se muestra el objeto en una relacion foranea
        return self.Nombre
    
    class Meta: # Metodo para nombrar el modelo
        verbose_name = 'medio de pago'  # Como se va a nombrar el objeto de la instancia
        verbose_name_plural ='Medios de compra' # Como se nombra el modelo
  
# -----------------------------------------------------------------------------
# Metodos para acceder a los valores de forma dinamica
#   configuracion.moneda()   ---> devuelve la moneda en la que se trabaja
#
class medioDePago(models.Model):
    Nombre = models.CharField(max_length=200, null=True, blank=True)

    def clean(self): # Metodo para verificar algun  campo antes de guardar.
        super().clean()

    def __str__(self): # Como se muestra el objeto en una relacion foranea
        return self.Nombre
    
    class Meta: # Metodo para nombrar el modelo
        verbose_name = 'medio de pago'  # Como se va a nombrar el objeto de la instancia
        verbose_name_plural ='Medios de venta' # Como se nombra el modelo

