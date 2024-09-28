// Función sin parámetros ni retorno
function saludar() {
    console.log("¡Hola, mundo!");
}

saludar();

// Función con un parámetro y retorno
function cuadrado(numero) {
    return numero * numero;
}

let resultadoCuadrado = cuadrado(5);
console.log("Cuadrado de 5:", resultadoCuadrado);

// Función con varios parámetros y retorno
function suma(a, b) {
    return a + b;
}

let x = 3
let y = 7
let resultadoSuma = suma(x, y);
console.log(`Suma de ${x} y ${y}:`, resultadoSuma);

// Función dentro de una función
function operacionMatematica(x, y) {
    function cuadruple(num) {
        return num * 4;
    }

    let resultado1 = cuadruple(x);
    let resultado2 = cuadruple(y);

    return resultado1 + resultado2;
}

let resultadoOperacion = operacionMatematica(2, 3);
console.log("Resultado de operación compleja:", resultadoOperacion);

// Variable local y global
let variableGlobal = 10;

function funcionConVariables() {
    let variableLocal = 5;
    console.log("Variable local dentro de la función:", variableLocal);
    console.log("Variable global dentro de la función:", variableGlobal);
}

funcionConVariables();
console.log("Variable global fuera de la función:", variableGlobal);

// DIFICULTAD EXTRA
function imprimirNumerosConTexto(texto1, texto2) {
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(texto1 + texto2);
        } else if (i % 3 === 0) {
            console.log(texto1);
        } else if (i % 5 === 0) {
            console.log(texto2);
        } else {
            console.log(i);
            contador++;
        }

    }

    return contador;
}

let vecesImpreso = imprimirNumerosConTexto("Fizz", "Buzz");
console.log("Número de veces impreso:", vecesImpreso);
