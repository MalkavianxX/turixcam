// Función para obtener el valor del token CSRF
function successAlert(title = undefined) {
    Swal.fire({
        title: title,
        icon: 'success',
        confirmButtonText: 'Listo',
        customClass: {
            confirmButton: 'btn btn-soft-primary',
        },

    }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
            location.reload();
            
        } else if (result.isDenied) {
            Swal.fire('Ocurrio un error, intenta más tarde', '', 'info')
        }
    })
} 
function errorAlert() {
    Swal.fire({
        title: 'Ha ocurrido un error',
        text: 'Verifica todos los campos',
        icon: 'error',
    }

    )
}

function getCSRFToken() {
    const name = 'csrftoken=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i].trim();
        if (cookie.indexOf(name) === 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }

    return null;
}
function printFormData(formData) {
    for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1]);
    }
}

document.getElementById('userinfo-btn').addEventListener('click', function (event) {

    var form = document.getElementById('form-userinfo');
    var nameUserInput = document.getElementById('userinfo-nameuser');
    var nameInput = document.getElementById('userinfo-name');
    var lastnameInput = document.getElementById('userinfo-lastname');
    var emailInput = document.getElementById('userinfo-email');
    const csrftoken = getCSRFToken();

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        if (!validateForm()) {
            return;
        }
        var formData = new FormData();
        formData.append('username', nameUserInput.value);
        formData.append('name', nameInput.value);
        formData.append('lastname', lastnameInput.value);
        formData.append('email', emailInput.value);

        fetch('/up_info', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken  // Asegúrate de tener disponible el token CSRF
            }
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error de red');
                }
                return response.json();
            })
            .then(data => {
                // Aquí puedes manejar la respuesta de la vista de Django
                if (data.error) {
                    // Muestra el mensaje de error
                    alert(data.error);
                } else {
                    successAlert("Datos actualizados");
                }
            })
            .catch(error => {
                // Aquí puedes manejar cualquier error que ocurra durante la solicitud
                console.error('Error:', error);
            });

    });

    function validateForm() {
        var isValid = true;

        // Validar cada campo
        if (!nameUserInput.value.trim()) {
            nameUserInput.classList.add('is-invalid');
            nameUserInput.nextElementSibling.textContent = 'Este campo no puede estar vacío.';
            isValid = false;
        } else {
            nameUserInput.classList.remove('is-invalid');
            nameUserInput.classList.add('is-valid');
        }

        if (!nameInput.value.trim()) {
            nameInput.classList.add('is-invalid');
            nameInput.nextElementSibling.textContent = 'Este campo no puede estar vacío.';
            isValid = false;
        } else {
            nameInput.classList.remove('is-invalid');
            nameInput.classList.add('is-valid');
        }

        if (!lastnameInput.value.trim()) {
            lastnameInput.classList.add('is-invalid');
            lastnameInput.nextElementSibling.textContent = 'Este campo no puede estar vacío.';
            isValid = false;
        } else {
            lastnameInput.classList.remove('is-invalid');
            lastnameInput.classList.add('is-valid');
        }

        if (!emailInput.value.trim()) {
            emailInput.classList.add('is-invalid');
            emailInput.nextElementSibling.textContent = 'Este campo no puede estar vacío.';
            isValid = false;
        } else if (!isValidEmail(emailInput.value.trim())) {
            emailInput.classList.add('is-invalid');
            emailInput.nextElementSibling.textContent = 'El formato del correo electrónico no es válido.';
            isValid = false;
        } else {
            emailInput.classList.remove('is-invalid');
            emailInput.classList.add('is-valid');
        }

        return isValid;
    }

    function isValidEmail(email) {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    }



});


document.getElementById('pass-btn').addEventListener('click', function (event) {
    var form = document.getElementById('form-pass');
    var firstPassInput = document.getElementById('pass-firstpass');
    var secondPassInput = document.getElementById('pass-secondpass');
    const csrftoken = getCSRFToken();

    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Evita el comportamiento de envío predeterminado

        // Validar las contraseñas
        if (firstPassInput.value !== secondPassInput.value) {
            secondPassInput.classList.add('is-invalid');
            secondPassInput.nextElementSibling.textContent = 'Las contraseñas no coinciden.';
            return;
        } else {
            secondPassInput.classList.remove('is-invalid');
            secondPassInput.classList.add('is-valid');
        }

        // Crear un objeto FormData y añadir los datos del formulario
        var formData = new FormData();
        formData.append('password', firstPassInput.value);

        // Enviar los datos del formulario a la vista de Django
        fetch('/up_password', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken  // Asegúrate de tener disponible el token CSRF
            }
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error de red');
                }
                return response.json();
            })
            .then(data => {
                // Aquí puedes manejar la respuesta de la vista de Django
                if (data.error) {
                    // Muestra el mensaje de error
                    alert(data.error);
                } else {
                    // Muestra el mensaje de éxito
                    location.reload();  // Recarga la página

                }
            })
            .catch(error => {
                // Aquí puedes manejar cualquier error que ocurra durante la solicitud
                console.error('Error:', error);
            });
    });

    // Para validar en tiempo real la longitud mínima de la contraseña
    firstPassInput.addEventListener('input', function () {
        if (firstPassInput.value.length < 7) {
            firstPassInput.classList.add('is-invalid');
            firstPassInput.classList.remove('is-valid');
        } else {
            firstPassInput.classList.remove('is-invalid');
            firstPassInput.classList.add('is-valid');
        }
    });

    secondPassInput.addEventListener('input', function () {
        if (secondPassInput.value.length < 7 || secondPassInput.value !== firstPassInput.value) {
            secondPassInput.classList.add('is-invalid');
            secondPassInput.classList.remove('is-valid');
        } else {
            secondPassInput.classList.remove('is-invalid');
            secondPassInput.classList.add('is-valid');
        }
    });
});



