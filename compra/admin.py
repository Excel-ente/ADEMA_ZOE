from django.contrib import admin,messages
from compra.models import Compra,CompraProducto,medioDePago
from django.core.exceptions import ValidationError
from import_export.admin import ImportExportModelAdmin

class CompraProductoInline(admin.TabularInline):
    model = CompraProducto
    extra = 1
    fields = ('Producto', 'Cantidad','Costo')
    autocomplete_fields = ('Producto',)

class MedioDePagoInline(admin.TabularInline):
    model = medioDePago
    extra = 1  # Define el número inicial de medios de pago que se mostrarán
    fields = ('cuenta','Total')


@admin.register(Compra)
class CompraAdmin(ImportExportModelAdmin):
    list_display = ('status', 'total_')
    exclude = ('total', 'estado','Producto')
    inlines = [MedioDePagoInline, CompraProductoInline ,]

    def costo_(self, obj):
        return "💲{:,.2f}".format(obj.costo)

    def total_(self, obj):
        return "💲{:,.2f}".format(obj.total_compra())

    def status(self, obj):
        if obj.estado == True:
            return "🟢 Ingresada"
        else:
            if obj.validar_compra() == True:
                return "🟠 Pendiente de ingreso"
            else:
                return "🔴 Verificar pagos" 

    def clean(self):
        if self.estado == True:
            raise ValidationError("Este producto ya fue controlado. No se puede modificar.")
        super().clean()

    def save(self, *args, **kwargs):
        super(Compra, self).save(*args, **kwargs)

    def ingresar_compra(self, request, queryset):
        for compra in queryset:
            try:
                if compra.estado == False:
                    if compra.validar_compra() == True:
                        compra.estado = True
                        compra.save()
                        self.message_user(request, 'La compra ha sido ingresada exitosamente.', level=messages.SUCCESS)
                    else:
                        raise ValidationError('Verificar pagos')
                else:
                    raise ValidationError('La compra ya ha sido ingresada anteriormente.')
            except ValidationError as e:
                self.message_user(request, e, level='ERROR')
            
    ingresar_compra.short_description = "Ingresar mercaderia"  # Descripción de la acción

    actions = [ingresar_compra]  # Asociar la acción personalizada a la clase CompraAdmin


@admin.register(medioDePago)
class medioDePagoAdmin(ImportExportModelAdmin):
    list_display = ('compra','cuenta','Total')
    readonly_fields = ('compra','cuenta','Total')

@admin.register(CompraProducto)
class CompraProductoAdmin(ImportExportModelAdmin):
    list_display = ('compra','Producto','Costo','Cantidad')
    readonly_fields = ('compra','Producto','Costo','Cantidad')