from django.db import models

class reporteVentas(models.Model):
    fecha = models.DateField()
    ventas = models.DecimalField(max_digits=25,decimal_places=2,default=0)
    total_minorista = models.DecimalField(max_digits=25,decimal_places=2,default=0)
    total_mayorista = models.DecimalField(max_digits=25, decimal_places=2,default=0)
    total_iva_21 = models.DecimalField(max_digits=25,decimal_places=2,default=0)
    total_iva_10_5 = models.DecimalField(max_digits=25,decimal_places=2,default=0)
    total_iibb = models.DecimalField(max_digits=25,decimal_places=2,default=0)

    total_efectivo = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    total_transferencia = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    total_cuenta_corriente = models.DecimalField(max_digits=25, decimal_places=2, default=0)
    total_redondeo = models.DecimalField(max_digits=25, decimal_places=2, default=0)


    def save(self, *args, **kwargs):

        super(reporteVentas, self).save(*args, **kwargs)

