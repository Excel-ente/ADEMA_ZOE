from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from producto.models import Producto, Categoria
from compra.models import CompraProducto
from venta.models import DetalleVenta

@admin.register(Categoria)
class CategoriaAdmin(ImportExportModelAdmin):
    list_display = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    list_display = ('nombre','categoria','descripcion','costo','precio','stock')
    list_filter = ('nombre','categoria','descripcion')
    search_fields = ('nombre',)
    list_display_links = ('categoria','nombre',)
    exclude = ('precio_bs','en_stock','precio_usd')

    def pesos(self, obj):
        return "💲{:,.2f}".format(obj.precio)  
      
    def stock(self, obj):
        
        valor =  0

        compras = CompraProducto.objects.filter(Producto__nombre=obj.nombre)
        
        for compra in compras:
            if compra.compra.estado == True:
                valor += compra.Cantidad

        ventas = DetalleVenta.objects.filter(producto__nombre=obj.nombre)

        for venta in ventas:
            if venta.venta.estado == 3:
                valor -= venta.cantidad           

        return valor   