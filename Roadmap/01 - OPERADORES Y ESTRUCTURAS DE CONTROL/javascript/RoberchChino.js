/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//tipos de operadores
console.log(5 + 5)
console.log(5 * 5)
console.log(5 - 4)
console.log(5 % 5)
console.log(5 > 10)
console.log(5 < 10)
console.log(5 >= 5)
console.log(5 !== 5)
console.log(5 !== 10 && 5 == 10 )
console.log(5 !== 10 || 5 == 10 )
console.log(5 & 5)
console.log(5 | 6)

let puntuacion = 10;
puntuacion += 5; 
console.log(puntuacion);

// actividad extra 

for (let i = 10; i<=55; i++ ) {
    try {
        if (i % 2 === 0 && i !== 16 && i % 3!==0){
            console.log(i)
        } 
        } catch (error) {
            console.log("error" + error.message)

        }      
    }
