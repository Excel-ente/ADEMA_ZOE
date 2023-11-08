from django.contrib import admin
from .models import Empleado
from import_export.admin import ImportExportModelAdmin

@admin.register(Empleado)
class ProductoAdmin(ImportExportModelAdmin):
    list_display = ('legajo','nombre','apellido','email',)