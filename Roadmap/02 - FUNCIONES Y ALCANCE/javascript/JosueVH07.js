
// Ejemplos de funciones

// Función sin argumentos y sin retorno
// FUnciones existentes en el navegador
// const selectH1 = document.querySelector('h1');
// console.log(selectH1);

// alert('Hola, soy Josue y estoy aprendiendo JavaScript');


// Función con argumentos y sin retorno

function saludar(nombre) {
    console.log('Hola ' + nombre);
}
saludar('Josue');

// Función con argumentos y con retorno
function suma(n1, n2) {
    return n1 + n2;
}

console.log(suma(5, 3));

// Función sin argumentos y con retorno
function obtenerNombre() {
    return 'Josue';
}

console.log(obtenerNombre());

// Función flecha
const multiplicar = (n1, n2) => {
    return n1 * n2;
}

console.log(multiplicar(5, 3));


// FUnciones dentro de funciones

function externa() {
    function interna() {
        console.log('Soy una función interna');
    }
    interna();
}

externa();

// Funciones del lenguaje

console.log(typeof saludar);

const date = new Date();

console.log(date);

// VARIABLES

// Variables globales
let nombre = 'Josue';
const apellido = 'Vargas';
var edad = 24;

function saludar() {
    console.log('Hola ' + nombre);
}

saludar();

// Variables locales
function local() {
    let nombre = 'Jeffrey';
    console.log(nombre);
}

local();

//DIFICULTAD EXTRA

const getNumber = (text1, text2) => {
    let total = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(text1 + text2);
        } else if (i % 3 === 0) {
            console.log(text1);
        } else if (i % 5 === 0) {
            console.log(text2);
        } else {
            console.log(i);
            total += 1;
        }
    }
    return console.log(total);
}

getNumber('Fizz', 'Buzz');