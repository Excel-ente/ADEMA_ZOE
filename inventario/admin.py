from django.contrib import admin
from .models import Producto
from import_export.admin import ImportExportModelAdmin
from administracion.models import Configuracion

@admin.register(Producto)
class ProductoAdmin(ImportExportModelAdmin):
    
    list_display = ('codigo','Nombre','categoria','Precio','en_stock')#'image_tag',
    list_filter = ('categoria','Proveedor')
    search_fields = ('nombre',)
    #exclude = ('precio_unitario','precio_mayorista','en_stock')

    def Nombre(self,obj):
        nombre = str(obj.nombre).upper() + " - " + str(obj.descripcion)
        return nombre
    

    def Costo(self, obj):
        return "💲{:,.2f}".format(obj.costo)  
        
    def Precio(self, obj):
        config = Configuracion.objects.first()
        costo = float(obj.costo)
        ganancia_minorista = float(config.ganancia_minorista)

        # Calcula el precio con la ganancia deseada
        precio_ganancia = costo / (1 - ganancia_minorista / 100)

        # Aplica un 20% de descuento al precio con ganancia
        precio_final = precio_ganancia * 0.8  # 0.8 representa un descuento del 20%

        return "💲{:,.2f}".format(precio_ganancia)
    
    def Precio_mayorista(self, obj):

        config = Configuracion.objects.first()
        costo = float(obj.costo)
        ganancia_mayorista = float(config.ganancia_mayorista)

        # Calcula el precio con la ganancia deseada
        precio_ganancia = costo / (1 - ganancia_mayorista / 100)

        # Aplica un 20% de descuento al precio con ganancia
        #precio_final = precio_ganancia * 0.8  # 0.8 representa un descuento del 20%

        return "💲{:,.2f}".format(precio_ganancia)


        