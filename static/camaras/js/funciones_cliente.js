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

    var lugar = document.getElementById('id_lugar').value;
    const token = getCSRFToken();
    var formData = new FormData();
    var boton = document.getElementById('btn_addFavorito');
    formData.append('id_lugar', lugar);
    boton.style.animation = 'pulse 0.5s';
    setTimeout(function() {
        boton.style.animation = '';
    }, 600);
    fetch('addFavorite', { // Asegúrate de reemplazar esto con la ruta correcta a tu función Django
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

    var lugar = document.getElementById('id_lugar').value;
    const token = getCSRFToken();
    var formData = new FormData();
    var boton = document.getElementById('btn_addGuardado');
    formData.append('id_lugar', lugar);
    boton.style.animation = 'pulse 0.5s';
    setTimeout(function() {
        boton.style.animation = '';
    }, 600);
    fetch('addGuardado', { // Asegúrate de reemplazar esto con la ruta correcta a tu función Django
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

    var lugar = document.getElementById('id_lugar').value;
    var text = document.getElementById('comen_text').value;
    var puntuacion = document.getElementById('comen_calificacion').value;
    const token = getCSRFToken();
    var formData = new FormData();
    formData.append('id_lugar', lugar);
    formData.append('text', text);
    formData.append('puntuacion', puntuacion);

    fetch('addComentario', { // Asegúrate de reemplazar esto con la ruta correcta a tu función Django
        method: 'POST',
        headers: {
            'X-CSRFToken': token,
        },
        body: formData,
    }) 
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Aquí puedes agregar código para actualizar la interfaz de usuario después de agregar el comentario
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
