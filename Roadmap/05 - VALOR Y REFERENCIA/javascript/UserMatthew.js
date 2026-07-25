/*#05 VALOR Y REFERENCIA
  ## Ejercicio
 */
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
*/

/* 
 * En Javascript la asignacion de variales "por valor" se le asigna a los datos de tipo primitivo
  Number, String, Boolean, Undefined, Null, Symbol, y BitInt... Y no modifica la variable original
*/

let a = 10 // Variable original
let b = a  // Se le asigna el valor de la original, se vuelve una copia
b = 30    // Se cambia la copia 

console.log('a:', a) //Sigue siendo la original
console.log('b:', b) // Cambio el valor de la copia 

/* 
 * En Javascript la asignacion de variales "por referencia" se le asigna a los datos de tipo
  Object, array , funtion, y modifica la variable original 
*/
let persona = {Nombre: "Juan"}
let persona2 = persona 

persona2.nombre = "Michael"
console.log(persona.nombre)
console.log(persona2.nombre)

/*
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 * 
 */

// Funcion variable asignada por valor 

let numero = 5
function incrementar(numero) {
  numero *= 5
  console.log(`El valor dentro de la funcion de la copia es ${numero}`)
}
incrementar(numero)
console.log(`El valor fuera de la funcion de la original es ${numero}`)

// Funcion variable asignada por referencia 
let usuario = { nombre: "Juan" };
function cambiarNombre(persona) {
  persona.nombre = "Pedro"; // 
}
cambiarNombre(usuario);
console.log(usuario.nombre); 

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


let valor1 = 20
let valor2 = 100
function parametrosPorValor(parametro1, parametro2) {
let temporal = parametro1
    parametro1 = parametro2
    parametro2 = temporal
  return   {parametro1 , parametro2}
}
console.log(parametrosPorValor(valor1, valor2))  
const resultados = parametrosPorValor(valor1,  valor2)
const resultado1 = resultados.parametro1
const resultado2 = resultados.parametro2

console.log(`Parametro 1 Original: ${valor1}, Nuevo: ${resultado1}`);
console.log(`Parametro 2 Original: ${valor2}, Nuevo: ${resultado2}`);

let list1 = [10, 20];
let list2 = [30, 40];
function parametrosPorReferencias(referencia1, referencia2) { 
    let temp = referencia1;
    referencia1 = referencia2;
    referencia2 = temp;
    return [  referencia1, referencia2 ];
  }
  
  const resultados2 = parametrosPorReferencias(list1, list2);
  
  const resultadoList1 = resultados2[0]
  const resultadoList2 = resultados2[1]
  
  console.log(`Parametro 1 Original: ${list1}, Nuevo: ${resultadoList1}`);
  console.log(`Parametro 2 Original: ${list2}, Nuevo: ${resultadoList2}`);