$(document).ready(function() {
    // Escuchar cambios en los campos de cantidad
    $('.cantidad-input').on('change', function() {
        var cantidad = parseFloat($(this).val());
        var precioUnitario = parseFloat($(this).data('precio-unitario'));
        var total = cantidad * precioUnitario;
        
        // Actualizar el campo total
        var totalField = $(this).closest('tr').find('.total-field');
        totalField.text('Total: ' + total.toFixed(2));
        
        // Actualizar el campo total en el modelo Django (puede requerir una llamada AJAX)
        var detalleId = $(this).data('detalle-id');
        updateTotalInDjangoModel(detalleId, total);
    });
});

function updateTotalInDjangoModel(detalleId, nuevoTotal) {
    // Aquí deberás realizar una llamada AJAX a una vista de Django para actualizar el total
    // utilizando el ID del detalle y el nuevo total.
    // Puedes usar jQuery para realizar la llamada AJAX.
    // Ejemplo:
    $.ajax({
        url: '/actualizar_total/' + detalleId + '/',
        method: 'POST',
        data: { total: nuevoTotal },
        success: function(data) {
            // Realizar acciones adicionales si es necesario
        }
    });
}
