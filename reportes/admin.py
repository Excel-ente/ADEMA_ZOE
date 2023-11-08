from django.contrib import admin
from .models import reporteVentas
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(reporteVentas)
class reporteVentasAdmin(ImportExportModelAdmin):
    list_display = ('fecha','ventas','total_efectivo','total_transferencia','total_cuenta_corriente','total_redondeo','total_iva_21','total_iva_10_5','total_iibb')

