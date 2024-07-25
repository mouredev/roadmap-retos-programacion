// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23
"use strict";

/*
 * EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
 */


// Crear un conjunto de datos utilizando un array en JavaScript
console.log("Conjunto de datos antes de realizar los cambios: ");
let conjunto = ["a", "b", "c", "d"];
console.log(conjunto);

// Añadir un elemento al final del conjunto
conjunto.push("e");
console.log(`*Agregando el elemento <<e>> al final del conjunto\n ${ conjunto }`)

// Añadir un elemento al principio del conjunto
conjunto.unshift("z");
console.log(`*Agregando el elemento <<z>> al principio del conjunto\n ${ conjunto }`)

// Añadir varios elementos al final del conjunto
conjunto.push("f", "g");
console.log(`*Agregando los elementos <<f,g>> al final del conjunto\n ${ conjunto }`)

// Añadir varios elementos en una posición concreta del conjunto
conjunto.splice(3, 0, "x", "y");
console.log(`*Agregando los elementos <<x, y>> en una posición en concreta del conjunto\n ${ conjunto }`)

// Eliminar un elemento en una posición concreta del conjunto
conjunto.splice(2, 1);
console.log(`*Eliminando elementos en posicion concreta\n ${ conjunto }`)

// Actualizar el valor de un elemento en una posición concreta del conjunto
conjunto[1] = "updated";
console.log(`*Actualizar el valor de los elementos en una posicion concreta\n ${ conjunto }`)

// Comprobar si un elemento está en el conjunto
const elementoBuscado = "c";
const estaEnConjunto = conjunto.includes(elementoBuscado);
console.log(`*El elemento "${elementoBuscado}" ${estaEnConjunto ? "sí" : "no"} está en el conjunto.`);

// Eliminar todo el contenido del conjunto
conjunto.length = 0;

/*
 * DIFICULTAD EXTRA (opcional):
 * Operaciones adicionales sobre conjuntos: Unión, Intersección, Diferencia, Diferencia simétrica
 */

// Crear dos conjuntos adicionales
let conjunto1 = ["a", "b", "c", "d"];
let conjunto2 = ["c", "d", "e", "f"];

// Unión de conjuntos
const union = [...new Set([...conjunto1, ...conjunto2])];
console.log("*Unión:", union);

// Intersección de conjuntos
const interseccion = conjunto1.filter(elemento => conjunto2.includes(elemento));
console.log("*Intersección:", interseccion);

// Diferencia de conjuntos (elementos en conjunto1 que no están en conjunto2)
const diferencia = conjunto1.filter(elemento => !conjunto2.includes(elemento));
console.log("*Diferencia:", diferencia);

// Diferencia simétrica de conjuntos (elementos que están en un conjunto u otro, pero no en ambos)
const diferenciaSimetrica = [...new Set([...conjunto1.filter(elemento => !conjunto2.includes(elemento)), ...conjunto2.filter(elemento => !conjunto1.includes(elemento))])];
console.log("*Diferencia simétrica:", diferenciaSimetrica);

