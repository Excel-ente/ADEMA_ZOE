from django.contrib import admin
from .models import Cliente,Gasto,TipoGasto,Retiro,Asignacion,Configuracion,proveedor,medioDeCompra,medioDePago
# Register your models here.
admin.site.register(Cliente)

@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ('empresa','direccion','telefono','tipoTicket',)

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('usuario','caja',)
        
@admin.register(Retiro)
class RetiroAdmin(admin.ModelAdmin):
    list_display = ('fecha','descripcion','total')

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('categoria','descripcion','total')

@admin.register(TipoGasto)
class TipoGastoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

# -----------------------------------------------------------------------------
# Vista proveedor
# 
@admin.register(proveedor)
class proveedorAdmin(admin.ModelAdmin):
    list_display = ('Empresa', 'NombreApellido','Direccion', 'Email','Telefono',)
    list_filter = ('Empresa', 'NombreApellido','Direccion', 'Email','Telefono',)
    search_fields = ('Empresa', 'NombreApellido','Direccion', 'Email','Telefono',)
    ordering = ('Empresa',)



# -----------------------------------------------------------------------------
# Vista Depositos
# 
@admin.register(medioDeCompra)
class medioDeCompraAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)


# -----------------------------------------------------------------------------
# Vista Depositos
# 
@admin.register(medioDePago)
class gastosAdicionalesAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
