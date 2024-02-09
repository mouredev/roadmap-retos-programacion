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


// Asignación de variables por valor y por referencia
var a = 1;
var b = a; // Asignación por valor
a = 2;
console.log(b); // 1

var c = { value: 1 };
var d = c; // Asignación por referencia
c.value = 2;
console.log(d.value); // 2

// Funciones con variables por valor y por referencia
function changeValue(val) {
    val = 2;
}
var e = 1;
changeValue(e);
console.log(e); // 1

function changeObjectValue(obj) {
    obj.value = 2;
}
var f = { value: 1 };
changeObjectValue(f);
console.log(f.value); // 2

// DIFICULTAD EXTRA
function swapValuesByValue(a, b) {
    var temp = a;
    a = b;
    b = temp;
    return [a, b];
}
var g = 1;
var h = 2;
var swappedValues = swapValuesByValue(g, h);
console.log(g); // 1
console.log(h); // 2
console.log(swappedValues[0]); // 2
console.log(swappedValues[1]); // 1

function swapValuesByReference(a, b) {
    var temp = a.value;
    a.value = b.value;
    b.value = temp;
    return [a, b];
}
var i = { value: 1 };
var j = { value: 2 };
var swappedObjects = swapValuesByReference(i, j);
console.log(i.value); // 2
console.log(j.value); // 1
console.log(swappedObjects[0].value); // 2
console.log(swappedObjects[1].value); // 1
