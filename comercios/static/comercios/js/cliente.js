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


document.getElementById('comen_btn').addEventListener('click', function(e) {
    e.preventDefault();

    var comercio = document.getElementById('id_comercio').value;
    var text = document.getElementById('comen_text').value;
    var puntuacion = document.getElementById('comen_calificacion').value;
    console.log(comercio,text,puntuacion);
    const token = getCSRFToken();
    var formData = new FormData();
    formData.append('object_id', comercio);
    formData.append('text', text);
    formData.append('puntuacion', puntuacion);
    formData.append('object_type','comercio');
    formData.append('app_label','comercios');

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
