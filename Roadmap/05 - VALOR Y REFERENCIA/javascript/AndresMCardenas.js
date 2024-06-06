/*
* EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como
* variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime
*   el valor de las variables originales y las nuevas, comprobando que se ha invertido
*   su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*/

// Asignación de variables por valor y por referencia

let a = 5;
let b = a; // Asignación por valor
console.log(b); // imprime 5
a = 10;
console.log(a); // imprime 10
console.log(b); // imprime 5

let c = { nombre: "Andrés" };
let d = c; // Asignación por referencia (en este caso, se copia la dirección de memoria) y si se modifica c, también se modifica d
console.log(d.nombre); // imprime "Andrés"
c.nombre = "Juan";
console.log(c.nombre); // imprime "Juan"
console.log(d.nombre); // imprime "Juan"

// Funciones con parámetros por valor y por referencia

function cambiarValor(a) {
  a = 20;
  console.log(a); // imprime 20

}

let e = 10;
cambiarValor(e);
console.log(e); // imprime 10 por que se pasó por valor no la referencia

function cambiarValorObjeto(c) {
  c.nombre = "Pedro";
  console.log(c.nombre); // imprime "Pedro"
}

let f = { nombre: "Andrés" };
cambiarValorObjeto(f);
console.log(f.nombre); // imprime "Pedro" por que se pasó por referencia

// DIFICULTAD EXTRA (opcional)

function intercambiarValoresPorValor(a, b) {
  let aux = a;
  a = b;
  b = aux;
  return [a, b];
}

let g = 5;
let h = 10;
let resultado = intercambiarValoresPorValor(g, h);
console.log(g); // imprime 5
console.log(h); // imprime 10
console.log(resultado[0]); // imprime 10
console.log(resultado[1]); // imprime 5

function intercambiarValoresPorReferencia(c, d) {
  let aux = c.nombre;
  c.nombre = d.nombre;
  d.nombre = aux;
  return [c, d];
}

let i = { nombre: "Andrés" };
let j = { nombre: "Juan" };
let resultado2 = intercambiarValoresPorReferencia(i, j);
console.log(i.nombre); // imprime "Juan"
console.log(j.nombre); // imprime "Andrés"
console.log(resultado2[0].nombre); // imprime "Juan"
console.log(resultado2[1].nombre); // imprime "Andrés"



