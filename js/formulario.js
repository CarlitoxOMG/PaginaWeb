$("#formulario").validate({
    rules: {
        "Email": {
            required: true,
            email: true
        },
        "Contraseña": {
            required: true,
            minlength: 6
        },
        "RepetirContraseña": {
            required: true,
            equalTo: '#id_Contraseña'
        }
    }, 
    messages: {
        "Email": {
            required: 'Ingrese Su Email!',
            email: 'No es un Email!!'
        },
        "Contraseña": {
            required: 'Ingrese Contreseña!!!',
            minlength: 'Minimo 6 Caracteres'
        },
        "RepetirContraseña": {
            required: 'Repita La Contraseña!!',
            equalTo: ' Las Contraseñas Deben De Ser Iguales!!!!'
        }
    } 
});
