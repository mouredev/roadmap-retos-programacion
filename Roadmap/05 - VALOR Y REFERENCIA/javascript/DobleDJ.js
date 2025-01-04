/** #05 - javaScript VALOR Y REFERENCIA
 * Date: 03/01/2025
 * Author: Yoandy Doble Herrera
 */

/*
EJERCICIO:
- Muestra ejemplos de asignación de variables "por valor" y "por referencia" según su tipo de dato.
- Muestra ejemplos de funciones con variables que se les pasan "por valor" y "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas. (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)

DIFICULTAD EXTRA (opcional):
Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
Comprueba también que se ha conservado el valor original en las primeras.
*/

/* Asignación por valor */
let usuario = "codebydoble"
const distancia = 10000
let userCopy = "@" + usuario

console.log(usuario)
console.log(distancia)
console.log(userCopy)

/* Asignación de variables por referencia */

const librosTech = ["De 0 a Experto", "Github ++", "100 Horas de código", "Javascript Eloquent"]
const personalBook = librosTech

librosTech.push("Mouredev la guía definitiva") // se actualiza en ambos array
console.log(librosTech)
console.log(personalBook)
