from django.contrib import admin
from django.contrib import messages
from .models import DetalleCompra
from django.core.exceptions import ValidationError

from django.http import HttpResponse
from django.template import loader

@admin.action(description="Mostrar modal de saludo")
def DecirHola(modeladmin, request, queryset):
    palabra_a_decir = "Hola"

    # Crea el contenido del modal
    template = loader.get_template('admin/compra/AutorizacionVenta.html')
    modal_content = template.render({'palabra_a_decir': palabra_a_decir}, request)

    # Retorna el contenido del modal en una respuesta HTTP
    return HttpResponse(modal_content)
    

@admin.action(description="Autorizar Compra")
def AutorizarCompra(modeladmin, request, queryset):
    aprobadas = 0
    no_aprobadas = 0

    for compra in queryset:
        if compra.estado == False:

            validacion = compra.validar_compra()

            if validacion == False:
                messages.error(request, f"La suma de los pagos no es igual al total de compra. Por favor verifique que el pago de la factura sea igual total de la misma.")
            else:

                # Paso a estado ok la compra
                compra.estado = True

                # Capturo los detalles de compra
                detalles_compra = DetalleCompra.objects.filter(compra__pk=compra.pk)

                for detalle_compra in detalles_compra:
                    producto = detalle_compra.producto
                    cantidad = detalle_compra.cantidad
                    costo = detalle_compra.precio
                    try:
                        producto.ingresar_stock(cantidad)
                        producto.costo = costo  # Actualizar el costo del producto
                        producto.save()
                    except ValidationError as e:
                        # Manejar el caso en el que no haya suficiente stock disponible
                        messages.error(request, f"No hay suficiente stock disponible para {producto.nombre}. {e}")

                compra.save()
                aprobadas += 1
        else:
            no_aprobadas += 1

    if aprobadas > 0:
        if no_aprobadas == 0:
            messages.success(request, f"Se autorizaron: {aprobadas} compras.")
        else:
            messages.success(
                request, f"Se autorizaron: {aprobadas} compras y se han omitido {no_aprobadas} compras debido a que ya estaban aprobadas."
            )
    else:
        messages.success(request, f"Todas las compras seleccionadas se encuentran autorizadas.")



@admin.action(description="Ver detalle")
def VerDetalle(modeladmin, request, queryset):

    for compra in queryset:

        if compra.estado == True:

            factura = compra.pk
            total_factura = compra.total_compra()
            total_pagos = compra.total_compra()

            iva = 0.21
            iibb = 0.05

            # Calcular el total de IVA y el total de IIBB
            total_iva = float(total_factura) * float(iva)
            total_iibb = float(total_factura) * float(iibb)
            total_neto = float(total_factura) - float(total_iva) - float(total_iibb)


            print(f'Factura #{factura} - Total Bruto: $ {total_factura} - Total Pagos: $ {total_pagos} - Total iva: $ {total_iva} - Total iibb: $ {total_iibb} - Total neto: $ {total_neto}')