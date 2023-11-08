# ---------------- ADEMA ------------------
# Sistema desarrollado por Kevin Turkienich 2023
# Contacto: kevin_turkienich@outlook.com
# 
# ----------------------------------------------

# ---------------- IMPORTACIONES DE MODULOS ----------------->

from django.contrib import admin
from fabrica.models import *
from import_export.admin import ImportExportModelAdmin


# ---------------- ADMINISTRACION DE MODELOS  ----------------->


class IngredienteRecetaInline(admin.TabularInline):
    model = ingredientereceta
    extra = 1
    fields = ('ingrediente', 'cantidad','unidad_de_medida')

class gastosAdicionalesInline(admin.TabularInline):
    model = adicionalreceta
    extra = 1
    fields = ('adicional', 'precio',)

class RecetaAdmin(admin.ModelAdmin):

    inlines = [
        gastosAdicionalesInline,
        IngredienteRecetaInline,
    ]

    list_display = ('producto','porciones','detalle','fecha_de_actualizacion')
    ordering = ('producto',)
    list_filter = ('producto',)
    list_per_page = 50

class IngredienteAdmin(ImportExportModelAdmin):
    list_display = ('producto','proveedor','cantidad','unidad_medida','costo')
    ordering = ('producto',)
    list_filter = ('producto','proveedor')

class gastosAdicionalesAdmin(ImportExportModelAdmin):
    list_display = ('nombre',)

admin.site.register(gastosAdicionales, gastosAdicionalesAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Receta, RecetaAdmin)