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

let x = 0
let y = 0
/* Asignación */	
    x = y
    x = y 

/* Asignación de adición */	
    x += y
    x = x + y

/* Asignación de resta */
	x -= y
	x = x - y

/* Asignación de multiplicación */
	x *= y
	x = x * y

/* Asignación de división */	
    x /= y	
    x = x / y

/* Asignación de residuo */
    x %= y	
    x = x % y

/* Asignación de exponenciación */
    x **= y
    x = x ** y

/* Asignación de desplazamiento a la izquierda */
    x <<= y	
    x = x << y

/* Asignación de desplazamiento a la derecha */
    x >>= y	
    x = x >> y

/* Asignación de desplazamiento a la derecha sin signo */
	x >>>= y	
    x = x >>> y

/* Asignación AND bit a bit */
	x &= y	
    x = x & y

/* Asignación XOR bit a bit */
	x ^= y	
    x = x ^ y

/* Asignación OR bit a bit */
	x |= y	
    x = x | y

/* Asignación AND lógico */
	x &&= y	
    x && (x = y)
    
/* Asignación OR lógico */
	x ||= y	
    x || (x = y)

/* Asignación de anulación lógica */	
    x ??= y	
    x ?? (x = y);

console.log ("Probando consola con NodeJs")


// * DIFICULTAD EXTRA (opcional):
//* Crea un programa que imprima por consola todos los números comprendidos
//* entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//*
//* Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


for (let a = 10; a <= 55 ;a ++){
// Evaluar si el valor de a es un numero par
if (a % 2 === 0){
    console.log(a + "par")
    //Evaluar si el valor es igual a 16 o multiplo de 3
    if (a === 16 && a % 3 !== 0) {
    // Mostrar el valor en la consola. 
    console.log(a + "**")
    }
}
console.log(a);
} ;