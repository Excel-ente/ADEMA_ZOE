from django.shortcuts import render
from .models import DetalleVenta,Venta
from django.http import JsonResponse

# Create your views here.
def ventas__venta__custom_action(request, object_id):
    # Agrega aquí la lógica de tu acción personalizada
    # Por ejemplo, redirige a otra página o realiza una acción específica.
    return render(request, 'custom_action.html', {'object_id': object_id})


def actualizar_total_detalle(request, detalle_id):
    if request.method == 'POST':
        nuevo_total = request.POST.get('total')
        detalle = DetalleVenta.objects.get(pk=detalle_id)
        detalle.total = nuevo_total
        detalle.save()
        return JsonResponse({'message': 'Total actualizado correctamente'})
    return JsonResponse({'error': 'Método no permitido'}, status=400)


def actualizar_total(request, venta_id):
    if request.method == "POST":
        venta = Venta.objects.get(pk=venta_id)

        # Realiza cálculos y guarda la factura de venta
        # Puedes incluir aquí tu lógica para actualizar la factura

        venta.save()

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})


def mostrar_modal(request):
    # Aquí puedes agregar lógica para preparar los datos que se mostrarán en el modal
    # Por ejemplo, puedes pasar un formulario, información o cualquier contenido necesario.
    context = {
        'data_to_display': 'Información para mostrar en el modal',
    }
    return render(request, 'modal_template.html', context)