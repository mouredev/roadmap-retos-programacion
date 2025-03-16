/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 */

// Tipos de dato por valor (primitivos)

let a = 5;

console.log(a); // 5

let b = a;

console.log(b); // 5

b = 10;

console.log(a); // 5

console.log(b); // 10

// Tipos de dato por referencia (objetos)

let objeto1 = {
    nombre: "Ralph"
};

console.log(objeto1); // { nombre: "Ralph" }

let objeto2 = objeto1;

console.log(objeto2); // { nombre: "Ralph" }

objeto2.nombre = "Ralph McRalph";

console.log(objeto1); // { nombre: "Ralph McRalph" }

console.log(objeto2); // { nombre: "Ralph McRalph" }

// Funciones con parámetros por valor

function duplicar(numero) {
    return numero *= 2;
}

let numero = 5;

console.log(duplicar(numero));

console.log(numero); // 5

// Funciones con parámetros por referencia

function cambiarNombre(objeto) {
    objeto.nombre = "Ralph McRalph";
}

let persona = {
    nombre: "Ralph"
};

console.log(persona);

cambiarNombre(persona);

console.log(persona); // { nombre: "Ralph McRalph" }

let my_list_a = [1, 2, 3];
let my_list_b = my_list_a;

my_list_b.push(4);

console.log(my_list_a); // [1, 2, 3, 4]



/* DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

// Por valor

let my_int_a = 10;
let my_int_b = 20;

function intercambioValor(int1, int2) {

    var my_temp = int1;

    int1 = int2;

    int2 = my_temp

    return [int1, int2]

}

[my_new_int_a, my_new_int_b] = intercambioValor(my_int_a, my_int_b);

console.log(my_int_a + "," + my_int_b);

console.log(my_new_int_a + "," + my_new_int_b);

// Por referencia

let persona_a = {
    nombre: "Ralph"
}

let persona_b = {
    nombre: "McRalph"
}

function intercambiarReferencia(persona1, persona2) {

    var persona_temp = persona1;

    persona1 = persona2;

    persona2 = persona_temp;

    return [persona1, persona2]

}


[new_persona_a, new_persona_b] = intercambioValor(persona_a, persona_b);

console.log(persona_a.nombre + "," + persona_b.nombre);

console.log(new_persona_a.nombre + "," + new_persona_b.nombre);



