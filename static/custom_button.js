(function($) {
    $(document).ready(function() {
        // Agrega un botón personalizado al formulario de edición
        var customButton = '<input type="button" class="default" value="Hacer Algo" id="custom_button" />';
        $(".submit-row .submit-row").prepend(customButton);

        // Maneja el clic del botón personalizado
        $("#custom_button").on("click", function() {
            // Agrega aquí la lógica personalizada que deseas realizar
            alert("Botón personalizado clicado.");
        });
    });
})(django.jQuery);
