document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.imagen_nube');
    const images = document.querySelectorAll('.imagen_nube');

    form.addEventListener('mouseenter', function () {
        images.forEach(image => {
            image.style.animation = 'float 0.5s ease-in-out infinite';
        });
    });

    form.addEventListener('mouseleave', function () {
        images.forEach(image => {
            image.style.animation = '';
        });
    });
});


//Enviar el formulario al pulsar enter
document.getElementById('weatherForm').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        document.getElementById('weatherForm').submit();
    }
});


//Eliminar el texto ya escrito al cerrar y abrir
const searchContainer = document.getElementById('searchContainer');
const cityInput = document.getElementById('city');

document.addEventListener('click', function (event) {
    const isClickInsideSearch = searchContainer.contains(event.target);
    const isClickInsideInput = event.target === cityInput;

    if (!isClickInsideSearch && !isClickInsideInput) {
        cityInput.value = '';
    }
});
