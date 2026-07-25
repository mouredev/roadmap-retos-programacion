// Variable global
let contadorGlobal: number = 0;

// 1. Función sin parámetros ni retorno
function saludar(): void {
    console.log("¡Hola, mundo!");
}

// 2. Función con un parámetro y sin retorno
function saludarPersona(nombre: string): void {
    console.log(`¡Hola, ${nombre}!`);
}

// 3. Función con múltiples parámetros y retorno
function sumar(a: number, b: number): number {
    return a + b;
}

// 4. Función que demuestra una "función" dentro de otra
function operacionMatematica(a: number, b: number): number {
    const multiplicar = (x: number, y: number): number => x * y;
    return multiplicar(a, b) + 10;
}

// 5. Uso de una función incorporada en TypeScript/JavaScript
function obtenerFechaActual(): string {
    return new Date().toISOString().split('T')[0];
}

// 6. Demostración de variable local vs global
function incrementarContador(): void {
    let contadorLocal: number = 0;
    contadorLocal++;
    contadorGlobal++;
    console.log(`Contador local: ${contadorLocal}, Contador global: ${contadorGlobal}`);
}

// DIFICULTAD EXTRA
function imprimirYContar(texto1: string, texto2: string): number {
    let contadorNumeros: number = 0;

    for (let i: number = 1; i <= 100; i++) {
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

// Llamadas a las funciones y impresión de resultados
console.log("1. Función sin parámetros ni retorno:");
saludar();

console.log("\n2. Función con un parámetro y sin retorno:");
saludarPersona("Alice");

console.log("\n3. Función con múltiples parámetros y retorno:");
console.log(`Suma de 5 y 3: ${sumar(5, 3)}`);

console.log("\n4. Función que demuestra una \"función\" dentro de otra:");
console.log(`Resultado de operación matemática: ${operacionMatematica(4, 5)}`);

console.log("\n5. Uso de una función incorporada en TypeScript/JavaScript:");
console.log(`Fecha actual: ${obtenerFechaActual()}`);

console.log("\n6. Demostración de variable local vs global:");
incrementarContador();
incrementarContador();

console.log("\nDIFICULTAD EXTRA:");
const numerosPuros: number = imprimirYContar("Fizz", "Buzz");
console.log(`Números impresos sin ser reemplazados por texto: ${numerosPuros}`);