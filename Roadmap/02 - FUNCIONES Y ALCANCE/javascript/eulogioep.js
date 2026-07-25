// Variables globales
let contadorGlobal = 0;

// 1. Función sin parámetros ni retorno
function saludar() {
    console.log("¡Hola, mundo!");
}

// 2. Función con un parámetro y sin retorno
function saludarPersona(nombre) {
    console.log(`¡Hola, ${nombre}!`);
}

// 3. Función con múltiples parámetros y retorno
function sumar(a, b) {
    return a + b;
}

// 4. Función dentro de otra función
function operacionMatematica(a, b) {
    function multiplicar(x, y) {
        return x * y;
    }
    return multiplicar(a, b) + 10;
}

// 5. Uso de una función incorporada en JavaScript
function obtenerFechaActual() {
    return new Date().toLocaleDateString();
}

// 6. Demostración de variable local vs global
function incrementarContador() {
    let contadorLocal = 0;
    contadorLocal++;
    contadorGlobal++;
    console.log(`Contador local: ${contadorLocal}, Contador global: ${contadorGlobal}`);
}

// Llamadas a las funciones y impresión de resultados
console.log("1. Función sin parámetros ni retorno:");
saludar();

console.log("\n2. Función con un parámetro y sin retorno:");
saludarPersona("Alice");

console.log("\n3. Función con múltiples parámetros y retorno:");
console.log(`Suma de 5 y 3: ${sumar(5, 3)}`);

console.log("\n4. Función dentro de otra función:");
console.log(`Resultado de operación matemática: ${operacionMatematica(4, 5)}`);

console.log("\n5. Uso de una función incorporada en JavaScript:");
console.log(`Fecha actual: ${obtenerFechaActual()}`);

console.log("\n6. Demostración de variable local vs global:");
incrementarContador();
incrementarContador();

// DIFICULTAD EXTRA
function imprimirYContar(texto1, texto2) {
    let contadorNumeros = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(texto1 + texto2);
        } else if (i % 3 === 0) {
            console.log(texto1);
        } else if (i % 5 === 0) {
            console.log(texto2);
        } else {
            console.log(i);
            contadorNumeros++;
        }
    }

    return contadorNumeros;
}

console.log("\nDIFICULTAD EXTRA:");
const numerosPuros = imprimirYContar("Fizz", "Buzz");
console.log(`Números impresos sin ser reemplazados por texto: ${numerosPuros}`);