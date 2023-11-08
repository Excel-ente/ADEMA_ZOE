import datetime
from datetime import date
from django.contrib import admin
from .Autorizaciones import AutorizarVenta,VerDetalle,ProbarAction
from .models import DetalleVenta,Venta,MedioDePago
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html


class articulosVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1
    fields = ('producto','venta_por_caja', 'cantidad', 'descuento','total')
    readonly_fields = ('total',)

    # class Media:
    #     js = ('custom_inline.js',)
    
class MedioDePagoInline(admin.TabularInline):
    model = MedioDePago
    extra = 1  # número inicial de medios de pago que se mostrarán
    fields = ('cuenta','total')

    def importe(self, obj):
        return obj.total



class FechaVentaFilter(admin.SimpleListFilter):
    title = 'Fecha de Venta'  # El título que se mostrará en la interfaz de administración
    parameter_name = 'fecha_venta'  # El nombre del parámetro de filtro en la URL

    def lookups(self, request, model_admin):
        # Define las opciones del filtro
        return (
            ('hoy', 'Hoy'),
            ('ultimos_7_dias', 'Últimos 7 días'),
            ('este_mes', 'Este mes'),
            ('este_anio', 'Este año'),
        )

    def queryset(self, request, queryset):
        # Aplica el filtro a la consulta en función de la opción seleccionada
        if self.value() == 'hoy':
            return queryset.filter(fecha__date=date.today())
        elif self.value() == 'ultimos_7_dias':
            return queryset.filter(fecha__gte=datetime.today() - datetime.timedelta(days=7))
        elif self.value() == 'este_mes':
            return queryset.filter(fecha__month=date.today().month, fecha__year=date.today().year)
        elif self.value() == 'este_anio':
            return queryset.filter(fecha__year=date.today().year)
        

@admin.register(Venta)
class ventaAdmin(ImportExportModelAdmin):
    inlines = [MedioDePagoInline, articulosVentaInline]
    list_display = ('Estado','fecha','forma_de_pago','cliente','total_venta','acciones',)
    readonly_fields=('total',)
    list_filter=(FechaVentaFilter,)
    actions = [AutorizarVenta,VerDetalle,ProbarAction]
    #change_form_template = 'caja.html'

    def forma_de_pago(self,obj):
        moneda = MedioDePago.objects.filter(venta=obj).first()
        if moneda:
            nombre = moneda.cuenta.nombre
        else:
            nombre = "Sin Informar"
        return nombre
    
    def Venta(self,obj):
        return f'Venta # {obj.pk}'

    def total_venta(self, obj):
        return "💲{:,.2f}".format(obj.total_venta())

    def total_iva(self, obj):
        calculo =  float(obj.total_venta())
        calculo =  round(calculo - (calculo / 1.21),2)
        return "💲{:,.2f}".format(calculo)

    def total_iibb(self, obj):
        calculo =  float(obj.total_venta())
        calculo =  round(calculo - (calculo / 1.05),2)
        return "💲{:,.2f}".format(calculo)
    
    def Estado(self, obj):
        check_pagos = obj.validar_venta()
        if obj.estado == False:
            if check_pagos == True:
                msg = "🟠"
            else:
                msg = "🔴"
        else:
            msg = "🟢"
        return msg
       
    def acciones(self, obj):
        if obj.estado == False:
            return format_html('<a href="/admin/ventas/venta/{0}/change/" class="button"> &nbsp; <b style="color:green;">Ver</b> &nbsp; </a></a><a href="/admin/ventas/venta/{0}/delete/" class="button" style="margin: 5px;background-color: rgba(179, 9, 9, 0.2);"> &nbsp; <b style="color:red;">Eliminar</b> &nbsp;</a>', obj.pk)
        else:
            return format_html('<a href="/admin/ventas/venta/{0}/change/" class="button"> &nbsp; <b style="color:green;">Ver</b> &nbsp; </a><a href="/admin/ventas/venta/{0}/delete/" class="button" style="margin: 5px;background-color: rgba(179, 9, 9, 0.2);"> &nbsp; <b style="color:red;">Eliminar</b> &nbsp; </a><a href="/pagar/{0}/change/" class="button" style="margin: 5px;"> &nbsp; <b>Descargar</b> &nbsp;</a>', obj.pk)

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     # Agrega un mensaje personalizado
    #     extra_context = extra_context or {}
    #     extra_context['message'] = "Numero de venta actual ID {}".format(object_id)
    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)


    def accion_personalizada(self, request, queryset):
        # Realiza la acción personalizada aquí
        pass

@admin.register(DetalleVenta)
class DetalleVentaAdmin(ImportExportModelAdmin):
    list_display = ('estado','venta','producto','precio_unitario','cantidad','descuento','Total',)
    readonly_fields = ('fecha','venta','producto','precio_unitario','cantidad','Total','descuento')
    list_filter = ('fecha','venta','producto',)
    exclude=('precio','total')


    def estado(self,obj):
        if obj.venta.estado == False:
            msg = "Venta pendiente"
        else:
            msg = "Venta aprobada"
        return msg
    
    def precio_unitario(self, obj):
        return "💲{:,.2f}".format(obj.producto.precio_unitario())

    def Total(self, obj):
        return "💲{:,.2f}".format(obj.total_detalles())
    

@admin.register(MedioDePago)
class MedioDePagoAdmin(ImportExportModelAdmin):
    list_display = ('cuenta','Total',)
    list_filter = ('cuenta',)
    exclude=('precio','total')

    def Total(self, obj):
        return "💲{:,.2f}".format(obj.total)
    
    # def acciones(self, obj):
    #     if obj.venta.estado == True:
    #         return format_html(' Venta #{0} &nbsp; <a href="/admin/ventas/venta/{0}/change/" class="button";">&nbsp;Ver Venta &nbsp;</a>', obj.pk)
        


