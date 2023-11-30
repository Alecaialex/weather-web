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

//Animación título
document.addEventListener('DOMContentLoaded', function () {
    const pageTitle = document.getElementById('pageTitle');
    const searchInput = document.getElementById('city');

    searchInput.addEventListener('click', function () {
        pageTitle.classList.remove('hidden');
        pageTitle.classList.add('visible');
    });

});