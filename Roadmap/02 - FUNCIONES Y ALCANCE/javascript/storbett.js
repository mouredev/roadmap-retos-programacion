// Funciones simples

function saludo() {
    console.log("hola JavaScript");
}

saludo();

// Función con retorno

function returnSaludo() {
    return "hola, JavaScript";
}

console.log(returnSaludo());

// Función con argumento, argumentos, argumentos predeterminados

function returnArgumento(nombre) {
    console.log(`hola, ${nombre}`);
}

returnArgumento("simon");

function returnArgumentoConSaludo(saludo, nombre) {
    console.log(`${saludo}, ${nombre}`);
}

returnArgumentoConSaludo("hi", "simon");

function defaultReturnArgumento(nombre = "JavaScript") {
    console.log(`hola, ${nombre}!`);
}

defaultReturnArgumento("simon");
defaultReturnArgumento();

// Función con retorno de varios valores

function multipleReturnArguments() {
    return ["hola", "JavaScript"];
}

const [saludoMultiple, nombreMultiple] = multipleReturnArguments();
console.log(saludoMultiple);
console.log(nombreMultiple);

// Funciones con número variable de argumentos

function variableArgSaludo(...nombres) {
    for (let nombre of nombres) {
        console.log(`hola, ${nombre}`);
    }
}

variableArgSaludo("JavaScript", "simon", "storbett");

// Función con número variable de argumentos con palabra clave

function variableKeyArgSaludo(nombres) {
    for (let key in nombres) {
        console.log(`${nombres[key]} (${key})`);
    }
}

variableKeyArgSaludo({
    lenguaje: "JavaScript",
    nombre: "simon",
    alias: "storbett",
    edad: 33
});

// Función dentro de una función

function otraFuncion() {
    function innerFuncion() {
        console.log("hola, JavaScript");
    }
    innerFuncion();
}

otraFuncion();

// Funciones dentro del lenguaje

console.log("storbett".length);
console.log(typeof "storbett");
console.log("storbett".toUpperCase());

// Variables locales y globales

let globalVariable = "JavaScript";

console.log(globalVariable);

function helloJavaScript() {
    let localVariable = "hola";
    console.log(`${localVariable}, ${globalVariable}`);
}

helloJavaScript();

// Extra

function prueba(tex1, text2) {
    let count = 0;
    for (let number = 1; number <= 100; number++) {
        if (number % 3 === 0 && number % 5 === 0) {
            console.log(tex1 + text2);
        } else if (number % 3 === 0) {
            console.log(tex1);
        } else if (number % 5 === 0) {
            console.log(text2);
        } else {
            console.log(number);
            count += 1;
        }
    }
    return count;
}

console.log(prueba("fizz", "buzz"));
