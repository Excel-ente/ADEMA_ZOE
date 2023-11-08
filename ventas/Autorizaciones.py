from django.contrib import admin
from django.contrib import messages
from .models import DetalleVenta
from django.core.exceptions import ValidationError


from django.http import HttpResponseRedirect

@admin.action(description="Probar action")
def ProbarAction(modeladmin, request, queryset):
    # Aquí puedes agregar la lógica necesaria antes de mostrar el modal
    # Por ejemplo, realizar alguna acción en los elementos seleccionados.

    # Luego, redirige al usuario a la vista que muestra el modal
    return HttpResponseRedirect('/mostrar_modal/')  # Reemplaza '/mostrar_modal/' con tu URL real

@admin.action(description="Autorizar Venta")
def AutorizarVenta(modeladmin, request, queryset):
    aprobadas = 0
    no_aprobadas = 0

    for venta in queryset:
        if venta.estado == False:

            validacion = venta.validar_venta()

            if validacion == False:
                messages.error(request, f"La suma de los pagos no es igual al total de venta. Por favor verifique que el pago de la factura sea igual total de la misma.")
            else:

                # Paso a estado ok la compra
                venta.estado = True

                # Capturo los detalles de compra
                detalles_venta = DetalleVenta.objects.filter(venta__pk=venta.pk)

                for detalle_venta in detalles_venta:
                    producto = detalle_venta.producto
                    cantidad = detalle_venta.cantidad
                    try:
                        producto.descontar_stock(cantidad)
                        producto.save()
                    except ValidationError as e:
                        # Manejar el caso en el que no haya suficiente stock disponible
                        messages.error(request, f"No hay suficiente stock disponible para {producto.nombre}. {e}")

                venta.save()
                aprobadas += 1
        else:
            no_aprobadas += 1

    if aprobadas > 0:
        if no_aprobadas == 0:
            messages.success(request, f"Se autorizaron: {aprobadas} ventas.")
        else:
            messages.success(
                request, f"Se autorizaron: {aprobadas} ventas y se han omitido {no_aprobadas} ventas debido a que ya estaban aprobadas."
            )
    else:
        messages.success(request, f"Todas las ventas seleccionadas se encuentran autorizadas.")



@admin.action(description="Ver detalle")
def VerDetalle(modeladmin, request, queryset):

    for venta in queryset:

        if venta.estado == False:

            factura = venta.pk
            total_factura = venta.total_venta()
            total_pagos = venta.total_venta()

            iva = 0.21
            iibb = 0.05

            # Calcular el total de IVA y el total de IIBB
            total_iva = float(total_factura) * float(iva)
            total_iibb = float(total_factura) * float(iibb)
            total_neto = float(total_factura) - float(total_iva) - float(total_iibb)


            print(f'Factura #{factura} - Total Bruto: $ {total_factura} - Total Pagos: $ {total_pagos} - Total iva: $ {total_iva} - Total iibb: $ {total_iibb} - Total neto: $ {total_neto}')
            messages.info(f'Factura #{factura} - Total Bruto: $ {total_factura} - Total Pagos: $ {total_pagos} - Total iva: $ {total_iva} - Total iibb: $ {total_iibb} - Total neto: $ {total_neto}')