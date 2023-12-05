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

// script.js

function toggleTemperatureUnit() {
    const tempElement = document.getElementById('cft');
    const flElement = document.getElementById('cfc');
    const currentTemp = tempElement.textContent;
    const isCelsius = currentTemp.includes('ºC');


    const temperature_c = tempElement.getAttribute('data-temperature-c');
    const temperature_f = tempElement.getAttribute('data-temperature-f');
    const feelslike_c = flElement.getAttribute('data-feelslike-c');
    const feelslike_f = flElement.getAttribute('data-feelslike-f');



    if (isCelsius) {
        tempElement.textContent = `${temperature_f}ºF`;
        flElement.textContent = 'Feels like: ' + `${feelslike_f}ºF`
    } else {
        tempElement.textContent = `${temperature_c}ºC`;
        flElement.textContent = 'Feels like: ' + `${feelslike_c}ºC`
    }
}

function toggleFeelsLike() {
    
}

const body = document.getElementById('weatherBody');
const isDay = body.getAttribute('data-isday');

if (isDay === '1') {
    body.style.background = 'linear-gradient(#e2fdfd, #88c8ff)';
} else {
    body.style.background = 'linear-gradient(#0b5a92, #043570)';
}