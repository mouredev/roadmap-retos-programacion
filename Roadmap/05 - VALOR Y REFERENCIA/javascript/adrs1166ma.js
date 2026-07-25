/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

// 🔥 Asignación por valor (tipos primitivos)
let numero1 = 5;
let numero2 = numero1; // Copia el valor de numero1
numero2 = 10;

console.log("Número 1:", numero1); // 5
console.log("Número 2:", numero2); // 10

// 🔥 Asignación por referencia (tipos compuestos)
let array1 = [1, 2, 3];
let array2 = array1; // Ambas variables apuntan al mismo objeto en memoria
array2.push(4);

console.log("Array 1:", array1); // [1, 2, 3, 4]
console.log("Array 2:", array2); // [1, 2, 3, 4]


// 🔥 Función con parámetro por valor
function modificarValor(valor) {
    valor = 100;
}

let num = 5;
modificarValor(num);
console.log("Número después de la función:", num); // 5 (no cambia)

// 🔥 Función con parámetro por referencia
function modificarReferencia(objeto) {
    objeto.propiedad = "Modificado";
}

let miObjeto = { propiedad: "Original" };
modificarReferencia(miObjeto);
console.log("Objeto después de la función:", miObjeto); // { propiedad: "Modificado" }

// 🔥 Programa 1: Intercambio "por valor"
// Intercambio de valores por valor
function intercambiarPorValor(valor1, valor2) {
    let temp = valor1;
    valor1 = valor2;
    valor2 = temp;
    return [valor1, valor2]; // Retornamos los valores intercambiados
}

// Variables originales
let original1 = 5;
let original2 = 10;

// Llamada a la función
let [nuevo1, nuevo2] = intercambiarPorValor(original1, original2);

// Resultados
console.log("Originales:", original1, original2); // 5, 10
console.log("Nuevos:", nuevo1, nuevo2); // 10, 5


// 🔥  Programa 2: Intercambio "por referencia"
// Intercambio de valores por referencia
function intercambiarPorReferencia(objeto1, objeto2) {
    let temp = objeto1.valor;
    objeto1.valor = objeto2.valor;
    objeto2.valor = temp;
    return [objeto1, objeto2]; // Retornamos los objetos modificados
}

// Variables originales
let objetoA = { valor: "A" };
let objetoB = { valor: "B" };

// Llamada a la función
let [nuevoObjetoA, nuevoObjetoB] = intercambiarPorReferencia(objetoA, objetoB);

// Resultados
console.log("Originales:", objetoA.valor, objetoB.valor); // B, A (modificados)
console.log("Nuevos:", nuevoObjetoA.valor, nuevoObjetoB.valor); // B, A