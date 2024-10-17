/**
 * Demostración de diferentes mecanismos de iteración en JavaScript
 * 
 * JavaScript, como lenguaje moderno y versátil, ofrece múltiples formas
 * de realizar iteraciones. Cada método tiene sus propias características
 * y casos de uso óptimos.
 */

console.log("=== Demostración de Mecanismos de Iteración en JavaScript ===\n");

// 1. Bucle for tradicional
console.log("1. Usando bucle for tradicional:");
/*
 * El bucle for es uno de los más básicos y ampliamente utilizados.
 * Sintaxis: for (inicialización; condición; incremento)
 * Es muy similar a otros lenguajes como Java o C++
 */
for (let i = 1; i <= 10; i++) {
    process.stdout.write(i + " ");
}
console.log("\n");

// 2. Bucle while
console.log("2. Usando bucle while:");
/*
 * El bucle while ejecuta un bloque de código mientras
 * una condición específica sea verdadera.
 */
let contador = 1;
while (contador <= 10) {
    process.stdout.write(contador + " ");
    contador++;
}
console.log("\n");

// 3. Bucle do...while
console.log("3. Usando bucle do...while:");
/*
 * Similar al while, pero garantiza que el código se ejecute
 * al menos una vez, ya que la condición se evalúa al final.
 */
let num = 1;
do {
    process.stdout.write(num + " ");
    num++;
} while (num <= 10);
console.log("\n");

// 4. forEach con array
console.log("4. Usando forEach con array:");
/*
 * El método forEach es una forma más funcional de iterar
 * sobre elementos de un array.
 */
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
numeros.forEach(numero => process.stdout.write(numero + " "));
console.log("\n");

// 5. for...of loop
console.log("5. Usando for...of:");
/*
 * Introducido en ES6, for...of proporciona una forma más concisa
 * de iterar sobre elementos iterables (arrays, strings, etc.)
 */
for (const numero of numeros) {
    process.stdout.write(numero + " ");
}
console.log("\n");

// 6. Array.from con mapeo
console.log("6. Usando Array.from con mapeo:");
/*
 * Array.from puede crear un array a partir de un objeto iterable
 * y permite mapear valores durante la creación
 */
Array.from({length: 10}, (_, i) => i + 1)
    .forEach(num => process.stdout.write(num + " "));
console.log("\n");

// 7. Recursión
console.log("7. Usando recursión:");
/*
 * Aunque técnicamente no es un loop, la recursión es otra forma
 * de realizar iteraciones mediante una función que se llama a sí misma
 */
function contarHasta10(n = 1) {
    process.stdout.write(n + " ");
    if (n < 10) contarHasta10(n + 1);
}
contarHasta10();
console.log("\n");

// 8. Map
console.log("8. Usando Map:");
/*
 * Similar a forEach, pero crea un nuevo array con los resultados
 * de llamar a una función para cada elemento
 */
console.log(Array(10).fill().map((_, index) => index + 1).join(" "));

// 9. Generator function
console.log("9. Usando Generator function:");
/*
 * Las funciones generadoras permiten definir un algoritmo iterativo
 * escribiendo una función que puede mantener su propio estado
 */
function* generarNumeros() {
    for (let i = 1; i <= 10; i++) {
        yield i;
    }
}

for (const num of generarNumeros()) {
    process.stdout.write(num + " ");
}
console.log("\n");

// 10. Reduce
console.log("10. Usando Reduce (aunque no es su uso típico):");
/*
 * Reduce normalmente se usa para acumular valores, pero también
 * puede usarse para iterar realizando una acción en cada paso
 */
Array(10).fill().reduce((_, __, i) => {
    process.stdout.write((i + 1) + " ");
    return null;
}, null);
console.log("\n");

console.log("\n=== Fin de la demostración ===");