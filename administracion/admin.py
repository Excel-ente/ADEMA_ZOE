from django.contrib import admin
from .models import Cliente,Proveedor,Categoria,Configuracion,Retiro,Gasto,CategoriaGasto,MedioDeCompra,MedioDePago,Familia
from .data_ejemplo import CrearDataEjemplo

admin.site.site_header ="ADEMA"

@admin.register(MedioDeCompra)
class MedioDeCompraAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(MedioDePago)
class MedioDePagoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  

@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ('empresa','email','telefono','ganancia_minorista','ganancia_mayorista')   
    exclude = ()#'v001',)
    actions = [CrearDataEjemplo,]

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)   

@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre',)   
        
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','direccion','telefono')   
         
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('empresa','nombre','telefono')


@admin.register(Retiro)
class RetiroAdmin(admin.ModelAdmin):
    list_display = ('fecha','descripcion','total')

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('categoria','descripcion','total')

@admin.register(CategoriaGasto)
class CategoriaGastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','cuenta')