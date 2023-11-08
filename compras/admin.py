from django.contrib import admin
from .Autorizaciones import AutorizarCompra,VerDetalle,DecirHola
from compras.models import Compra, DetalleCompra
from import_export.admin import ImportExportModelAdmin
from .models import MedioDePago

class articulosCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1
    fields = ('producto', 'cantidad', 'precio','descuento','total')

class MedioDePagoInline(admin.TabularInline):
    model = MedioDePago
    extra = 1  # Define el número inicial de medios de pago que se mostrarán
    fields = ('cuenta','total')

@admin.register(Compra)
class CompraAdmin(ImportExportModelAdmin):
    inlines = [MedioDePagoInline, articulosCompraInline]
    list_display = ('Compra','fecha','proveedor','total_compra','Estado',)
    #exclude = ('estado',)
    actions = [AutorizarCompra,VerDetalle,DecirHola]

    def Compra(self,obj):
        return f'Compra # {obj.pk}'

    def total_compra(self, obj):
        return "💲{:,.2f}".format(obj.total_compra())
    
    def Estado(self, obj):

        check_pagos = obj.validar_compra()



        if obj.estado == False:
            if check_pagos == True:
                msg = "🟠 Pendiente Aprobacion"
            else:
                msg = "🔴 Verificar pagos"
        else:
            msg = "🟢 Compra Aprobada"


        return msg
      
          
@admin.register(DetalleCompra)
class DetalleCompraAdmin(ImportExportModelAdmin):
    list_display = ('fecha','compra','producto','cantidad','precio_unitario','total')
    readonly_fields = ('fecha','compra','producto','cantidad','precio_unitario','total',)
    list_filter = ('fecha','compra','producto',)
    exclude=('precio',)

    def precio_unitario(self, obj):
        return "💲{:,.2f}".format(obj.precio)
    
    def total(self, obj):
        total = obj.precio * obj.cantidad
        return "💲{:,.2f}".format(total)
    
@admin.register(MedioDePago)
class MedioDePagoAdmin(ImportExportModelAdmin):
    list_display = ('compra','medio','cuenta','total')
