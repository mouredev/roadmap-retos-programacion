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

// Definimos una función que intercambia los valores de dos parámetros por valor
function intercambiarValoresPorValor(a, b) {
    let temp = a;
    a = b;
    b = temp;
    return [a, b];
}
  
// Definimos dos variables
let x = 5;
let y = 10;

// Llamamos a la función y asignamos los nuevos valores a dos variables diferentes
let [xNuevo, yNuevo] = intercambiarValoresPorValor(x, y);

// Imprimimos los valores originales y los nuevos
console.log("Valores originales:", x, y);
console.log("Nuevos valores:", xNuevo, yNuevo);


// Definimos una función que intercambia los valores de dos parámetros por referencia
function intercambiarValoresPorReferencia(objeto) {
    let temp = objeto.a;
    objeto.a = objeto.b;
    objeto.b = temp;
    return objeto;
  }
  
  // Definimos un objeto con dos propiedades
  let objeto = { a: 5, b: 10 };
  
  // Llamamos a la función y asignamos los nuevos valores a un nuevo objeto
  let objetoNuevo = intercambiarValoresPorReferencia(objeto);
  
  // Imprimimos los valores originales y los nuevos
  console.log("Valores originales:", objeto.a, objeto.b);
  console.log("Nuevos valores:", objetoNuevo.a, objetoNuevo.b);
  