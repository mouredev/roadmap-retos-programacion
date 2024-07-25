// Funciones y Alcance
// Funcion sin parametro ni retorno
function saludar() {
    console.log("Hola, Javascript!")
}

saludar();

// Funcion con un parametro y sin retorno
function saludarPersona(nombre) {
    console.log(`Hola, ${nombre} bienvenido!`);
}

saludarPersona("Matias");

// Funcion con varios parametros y con retorno
function sumar(a, b) {
    return a + b;
}

let resultado = sumar(5, 10);
console.log("El resultado es:", resultado);

// Uso de una funcion ya creada en el lenguaje
function usarFuncionExistente() {
    let numeros = [1, 2, 3, 4, 5];
    console.log(Math.max(...numeros));
}

usarFuncionExistente();

// Funciones dentro de funciones
function operacionMatematica(a, b) {
    function multiplicar(x, y) {
        return x * y;
    }
    return multiplicar(a, b) + 10;
}

console.log(operacionMatematica(5, 10));

// Variable local y global
let variableGlobal = "Soy una variable global";

function ejemploVariables() {
    let variableLocal = "Soy una variable local";
    console.log(variableLocal);
    console.log(variableGlobal);
}

ejemploVariables();

// Dificultad extra
console.log("------------Dificultad extra-----------");
function fizzBuzz(text1, text2) {
    let contador = 0;
    for (let i= 1; i <= 100; i++) {
        if (i % 3 === 0) {
            console.log(text1);
        } else if (i % 5 === 0) {
            console.log(text2);
        } else if (i % 3 === 0 && i % 5 === 0) {
            console.log(text1 + text2);
        } else {
            console.log(i);
            contador++;
        }
    }
    return contador;
}

console.log(fizzBuzz("Fizz", "Buzz"));