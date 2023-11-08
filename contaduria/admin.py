from django.contrib import admin
from .models import cuentasContables,AsientoContable
from import_export.admin import ImportExportModelAdmin

@admin.register(cuentasContables)
class cuentasContablesAdmin(ImportExportModelAdmin):
    list_display = ('cuenta','tipo','descripcion','estado')
    list_filter = ('cuenta','tipo','estado')

    
@admin.register(AsientoContable)
class asientosAdmin(ImportExportModelAdmin):
    list_display = ('fecha','cuenta','descripcion','importe','iva','iibb',)
    list_filter = ('cuenta',)
