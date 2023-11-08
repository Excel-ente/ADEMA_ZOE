from django.db import models

TIPO = [
    ("ACTIVO","ACTIVO"),
    ("PASIVO","PASIVO"),
    ("PATRIMONIO NETO","PATRIMONIO NETO"),
    ("INGRESOS","INGRESOS"),
    ("COSTOS DE VENTAS","COSTOS DE VENTAS"),
    ("GASTOS OPERATIVOS","GASTOS OPERATIVOS"),
    ("OTROS INGRESOS","OTROS INGRESOS"),
    ("OTROS GASTOS","OTROS GASTOS"),
    ("RETIROS DE EFECTIVO","RETIROS DE EFECTIVO"),
]

class cuentasContables(models.Model):
    cuenta = models.IntegerField(blank=False,null=False,unique=True)
    tipo = models.CharField(max_length=255, choices=TIPO, default=1, blank=True, null=True)
    descripcion = models.CharField(max_length=255,blank=False,null=False)
    estado = models.BooleanField(default=False)

    def __str__(self):
        formateo =  f'{self.cuenta} - {self.descripcion}'
        return formateo

class AsientoContable(models.Model):
    fecha = models.DateField()
    cuenta = models.ForeignKey(cuentasContables, on_delete=models.SET_NULL, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=25, decimal_places=2)
    iva = models.DecimalField(max_digits=25, decimal_places=2)
    iibb = models.DecimalField(max_digits=25, decimal_places=2)

    def __str__(self):
        return f'{self.fecha} / {self.cuenta}'
    
    class Meta:
        verbose_name = 'asiento contable'
        verbose_name_plural ='Libro mayor' 
        