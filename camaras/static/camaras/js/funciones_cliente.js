var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },

});
var swipermore = new Swiper(".mySwipermore", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
    pagination: {
        el: ".swiper-pagination",
    },
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 20
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 30
        }
    }
});

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
document.getElementById('btn_addFavorito').addEventListener('click', function(e) {
    e.preventDefault();

    var lugar = document.getElementById('id_camara').value;
    const token = getCSRFToken();
    var formData = new FormData();
    var boton = document.getElementById('btn_addFavorito');
    formData.append('id_camara', lugar);
    boton.style.animation = 'pulse 0.5s';
    setTimeout(function() {
        boton.style.animation = '';
    }, 600);
    fetch('/camaras/addFavorite', { // Asegúrate de reemplazar esto con la ruta correcta a tu función Django
        method: 'POST',
        headers: {
            'X-CSRFToken': token,
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        boton.classList.remove(data.del);
        boton.classList.add(data.add);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('btn_addGuardado').addEventListener('click', function(e) {
    e.preventDefault();

    var lugar = document.getElementById('id_camara').value;
    const token = getCSRFToken();
    var formData = new FormData();
    var boton = document.getElementById('btn_addGuardado');
    formData.append('id_camara', lugar);
    boton.style.animation = 'pulse 0.5s';
    setTimeout(function() {
        boton.style.animation = '';
    }, 600);
    fetch('/camaras/addGuardado', { // Asegúrate de reemplazar esto con la ruta correcta a tu función Django
        method: 'POST',
        headers: {
            'X-CSRFToken': token,
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        boton.classList.remove(data.del);
        boton.classList.add(data.add);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('comen_btn').addEventListener('click', function(e) {
    e.preventDefault();

    var lugar = document.getElementById('id_camara').value;
    var text = document.getElementById('comen_text').value;
    var puntuacion = document.getElementById('comen_calificacion').value;
    console.log(lugar,text,puntuacion);
    const token = getCSRFToken();
    var formData = new FormData();
    formData.append('object_id', lugar);
    formData.append('text', text);
    formData.append('puntuacion', puntuacion);
    formData.append('object_type','camara');
    formData.append('app_label','camaras');


    fetch('/camaras/addComentario', 
    { 
        method: 'POST',
        headers: {
            'X-CSRFToken': token,
        },
        body: formData,
    }) 
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.message === 'Comentario agregado.') {
            document.getElementById('comen_text').value = '';
            // Crea un nuevo elemento DOM para el comentario
            var comentarioDiv = document.createElement('div');
            comentarioDiv.innerHTML = `
                <div class="d-md-flex my-4 w-100 mb-3">
                    <div class="mt-3 ms-2 avatar avatar-lg me-3 flex-shrink-0">
                        <img class="avatar-img rounded-circle" loading="lazy"
                            src="${data.comentario.avatar_url}" alt="avatar">
                    </div>
                    <div class="w-100 mt-3 ms-2">
                        <div class="d-flex  justify-content-between mt-1 mt-md-0">
                            <div class="">
                                <h6 class="me-3 mb-0">${data.comentario.username}</h6>
                                <ul class="nav nav-divider small mb-2">
                                    <li class="nav-item" style="font-size: 0.85em;" >${data.comentario.fecha}</li>
                                    
                                </ul>
                            </div>
                            <div class="icon-md rounded text-bg-warning fs-6">${data.comentario.puntuacion}</div>
                        </div>
                        <p class="mb-2">${data.comentario.text}</p>
                    </div>
                </div>
                <hr class="mb-3">
                <div class="mb-3"></div>
            `;
            // Agrega el nuevo comentario al principio de la lista de comentarios
            var comentariosDiv = document.querySelector('.comentarios');
            comentariosDiv.insertBefore(comentarioDiv, comentariosDiv.firstChild);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    
});
