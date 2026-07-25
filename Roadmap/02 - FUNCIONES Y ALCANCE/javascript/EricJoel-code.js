// Funciones

// Función sin parámetros y sin retorno

function sinParametros() {
    console.log("Esta es una funcion sin parámetros y sin retorno")
}
sinParametros();

// Funición con un parámetro y sin retorno

function conUnParametro(parametro) {
    console.log(`Esta es una función con un parámetro y sin retorno, el parámetro es: ${parametro}`)
}
conUnParametro("Hola Mundo");

// Función con multiples parámetros y sin retorno

function conMultiplesParametros(param1, param2, param3) {
    console.log(`Esta es una función con múltiples parámetros y sin retorno, los parámetros son: ${param1}, ${param2}, ${param3}`)
}
conMultiplesParametros("Hola", "Mundo", "!");

// Función sin parámetros y con retorno

function sinParametrosConRetrono() {
    return "Esta es una función sin parámetros y con retorno"
}
console.log(sinParametrosConRetrono());

// Función con un parámetro y con retorno

function conUnParametroConRetornoo(parametro) {
    return `Esta es una función con un parámetro y con retorno, el parámetro es: ${parametro}`
}
console.log(conUnParametroConRetornoo(10));

// Función con múltiples parámetros y con retorno

function conMultiplesParametrosConRetrono(param1, param2) {
    return param1 + param2
}
console.log(conMultiplesParametrosConRetrono(10, 20));

// Función dentro de otra función

function funcionPrincipal() {
    console.log("Esta es la función principal");

    function funcionAnidada() {
        console.log("Esta es la función anidada");
    }
    funcionAnidada();
}

funcionPrincipal();

// Funciones ya creacdas en el lenguaje

// Función para convertir un string a mayúsculas

function convertirAMayusculas(texto) {
    return texto.toUpperCase();
}
console.log(convertirAMayusculas("hola mundo"));

// Función para convertir un string a minúsculas

function convertirAMinusculas(texto) {
    return texto.toLowerCase();
}

console.log(convertirAMinusculas("HOLA MUNDO"));

// Función para redondear un numero

function redondearNumero(numero) {
    return Math.round(numero);
}

console.log(redondearNumero(3.6));

// Funcion para gernerar un numero aleatorio entre 0 y 1

function generarNuemeroAleatorio() {
    return Math.random();
}

console.log(generarNuemeroAleatorio());

// Función para obtener la longitud de un string

function obtenerLonitudString(texto) {
    return texto.length;
}

console.log(obtenerLonitudString("Hola Mundo"));

// Función para obtener el valor absoluto de un numero 

function valorAbsoluto(numero) {
    return Math.abs(numero);
}

console.log(valorAbsoluto(-5));

// Función para obtener el valor máximo entre dos numeros

function valorMaximo(num1, num2) {
    return Math.max(num1, num2);
}

console.log(valorMaximo(10, 20))

// Variable global

let varGlobal = 13

function sumar() {
    console.log("El resultado de la suma es:", varGlobal + 10)
}
sumar()

// Variable local

function resta() {
    let varLocal = 26
    console.log("El resultado de la resta es:", varLocal - varGlobal)
}

resta()

//Extra 

function ejercicio(text1, text2) {

    let count = 0;

    for (i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${text1}${text2}`)
        } else if (i % 5 === 0) {
            console.log(text2)
        } else if (i % 3 === 0) {
            console.log(text1)
        } else {
            console.log(i)
        }
        count++
    }
    return count
}
ejercicio("Team", "Seal")