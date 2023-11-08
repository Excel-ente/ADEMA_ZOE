$(document).ready(function () {
    $("#cantidad").on("change", function () {
        var ventaId = $(this).data("venta-id");

        // Realiza una solicitud POST AJAX para actualizar la factura
        $.ajax({
            url: "/actualizar_total/" + ventaId + "/",
            type: "POST",
            data: {
                // Envía los datos necesarios para la actualización
                cantidad: $(this).val(),
                // Otros datos necesarios
            },
            success: function (data) {
                if (data.success) {
                    // Si la actualización fue exitosa, puedes mostrar un mensaje o realizar otras acciones
                    console.log("Factura actualizada con éxito.");
                } else {
                    console.log("Error al actualizar la factura.");
                }
            }
        });
    });
});

