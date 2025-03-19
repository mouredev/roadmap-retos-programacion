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

/***************************************************************/
/***************************************************************/
/***************************************************************/
/************************ PRIMERA PARTE ************************/
/***************************************************************/
/***************************************************************/
/***************************************************************/

/* ASIGNACION POR VALOR PARA TIPOS PRIMITIVOS - Siempre se copia el valor, debido a que cada variable tiene su propio espacio de memoria */

let a = 500;
let b = a; // Asignación por valor

console.log(a); // Salida: 10 (valor original no cambia)
console.log(b); // Salida: 10

a = 501;

console.log(a); // Salida: 20
console.log(b); // Salida: 10

/* ASIGNACION POR REFERENCIA PARA OBJETOS - Siempre se copia la referencia al espacio de memoria, así que si se cambia el valor de una variable, el valor de la otra variable cambia también, pues hacen referencia al mismo espacio de memoria */

let personaA = { nombre: "Laura" };
let personaB = personaA; // Asignación por referencia

console.log(personaA); // Salida: { nombre: 'Laura' }
console.log(personaB); // Salida: { nombre: 'Laura' }

personaA.nombre = "Arthuro";

console.log(personaA); // Salida: { nombre: 'Arthuro' }
console.log(personaB); // Salida: { nombre: 'Arthuro' }

personaB.nombre = "Laura"; //No importa la variable que se cambie. La referencia al mismo espacio de memoria se va a cambiar

console.log(personaA); // Salida: { nombre: 'Laura' }
console.log(personaB); // Salida: { nombre: 'Laura' }

/* FUNCION CON VARIABLES POR VALOR */

function dividir(num) {
  num /= 2;
  return num;
}

function multiplicar(num) {
  num *= 2;
  console.log(num);
}

let original = 10;
let resultado = dividir(original);

console.log(original); // Salida: 10 (el valor original no cambia)
console.log(resultado); // Salida: 5

original = 20;
resultado = multiplicar(original);

multiplicar(original); // El valor de la variable original no cambia. Cambia el valor de la variable dentro de la función
console.log(original); // Salida: 20 (el valor original no cambia)

/* FUNCION CON VARIABLES POR REFERENCIA */

function marcarComoLeido(libro) {
  libro.leido = true;
}

let libroOriginal = {
  autor: "J.K. Rowling",
  titulo: "Harry Potter y la Piedra Filosofal",
  leido: false,
};

console.log(libroOriginal.leido);
marcarComoLeido(libroOriginal);
console.log(libroOriginal.leido); //El valor de la variable original cambia

let arrayOriginal = [1, 2, 3];
let arrayCopia = arrayOriginal;

console.log(arrayOriginal);
console.log(arrayCopia);

arrayOriginal.push(4);

console.log(arrayOriginal);
console.log(arrayCopia); //Los arrays se comportan como si fueran objetos, es decir, se pasan por referencia

/***************************************************************/
/***************************************************************/
/***************************************************************/
/************************ SEGUNDA PARTE ************************/
/***************************************************************/
/***************************************************************/
/***************************************************************/

//Invertir Valores con Variables por Valor

function invertirPorValor(a, b) {
  let temp = a;
  a = b;
  b = temp;
  return [a, b];
}

let porValor1 = 'a';
let porValor2 = 'b';

let porValorInvertido = invertirPorValor(porValor1, porValor2);

//Los valores solo cambian en la función debido a que no se pasan por referencia

console.log(porValor1);
console.log(porValor2);

//Sin embargo, podemos asignar los nuevos valores a las variables originales de la siguiente manera:

porValor1 = porValorInvertido[0];
porValor2 = porValorInvertido[1];

console.log(porValor1);
console.log(porValor2);

//Invertir Valores con Variables por Referencia

function invertirPorReferencia(obj1, obj2) {
  let aux = obj1.nombre;
  obj1.nombre = obj2.nombre;
  obj2.nombre = aux;
  return [obj1, obj2];
}

let objeto1 = {
  nombre: "Pelota"
}

let objeto2 = {
  nombre: "Bate"
}

let nuevosObjetos = invertirPorReferencia(objeto1, objeto2);

console.log(objeto1);
console.log(objeto2); //Al pasarse por referencia, los objetos cambian de valor debido a que lo que se pasa por referencia es el espacio de memoria, no el valor

//Si asignamos los nuevos valores a nuevas variables de la siguiente manera:

let obj1copia = nuevosObjetos[0];
let obj2copia = nuevosObjetos[1];

console.log(obj1copia);
console.log(obj2copia);

 //Ahora, si cambio el valor del objeto 1
 objeto1.nombre = "Guante";
 
console.log(objeto1);
console.log(obj1copia); //El valor del objeto 1 cambia, así que la copia también cambia, debido a que, de nuevo, hacen referencia al mismo espacio de memoria.
