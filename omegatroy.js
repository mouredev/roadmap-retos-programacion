/*
 * EJERCICIO:
 * -  Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */


// Operadores Aritméticos:

let numero1 = 23;
let numero2 = 21;

// Operador de Asignación -> =
numero1 = numero2;
console.log(numero1)// --> esto aria que numero1 sea 21


// Operador de Asignación de adición -> +=
numero1 += numero2;
console.log(numero1) // --> esto aria que adición sea igual ala suma de numero1 y numero2 o sea 42


// Operador de Asignación de resta -> -=
numero1 -= numero2;
console.log(numero1) // --> esto Equivale a: la resta de numero1: 42 y numero2: 21 o sea (42 - 21) = 21


// Operador de Asignación de multiplicación -> *=
numero1 *= numero2;
console.log(numero1) // --> esto Equivale a: la multiplicación de numero1: 21 y numero2: 21 o sea (21 * 21) = 441



// Operador de Asignación de división -> /=
numero1 /= numero2;
console.log(numero1) // --> esto Equivale a: la divisió de numero1: 441 y numero2: 21 o sea (441 / 21) = 21


// Operador de Asignación de residuo -> %=
numero1 %= numero2;
console.log(numero1) // --> esto Equivale a: el residuo de la división de su valor original (numero1) por numero2, que es 0.
numero1 = 2;


// Operador de Asignación de exponenciación
numero1 **= numero2;
console.log(numero1) // --> esto Equivale a: eleva numero1 a la potencia de un exponente numero2 que es 2097152


//Asignación de desplazamiento a la izquierda -> <<=
numero1 <<= numero2;
console.log(numero1) // --> esto Equivale a: Realiza un desplazamiento de bits a la izquierda en 'numero1' por numero2: 21 posiciones y asigna el resultado que es 0
numero1 = 23


//Asignación de desplazamiento a la derecha -> >>=
numero1 >>= numero2;
console.log(numero1) // --> esto Equivale a: Realiza un desplazamiento de bits a la derecha en 'numero1' por numero2: 21 posiciones y asigna el resultado que es 0
numero1 = -23

numero1 >>>= 1
console.log(numero1) // --> esto Equivale a:  Realiza un desplazamiento de bits a la derecha sin signo en 'numero1' por 1 posición y asigna el resultado que es 2147483636


// Operador de Asignación AND bit a bit -> &=
numero1 = 10 // Representación binaria: 1010
numero1 &= 5; // Representación binaria de 5: 0101
console.log(numero1) // --> esto Equivale a: Resultado: 0 (1010 & 0101 = 0000)


// Operador de Asignación XOR bit a bit -> ^=
numero1 = 10;  // Representación binaria: 1010
// Realiza una operación XOR bit a bit con 6 y asigna el resultado
numero1 ^= 6;  // Representación binaria de 6: 0110
console.log(numero1) // --> esto Equivale a: Resultado: 12 (1010 ^ 0110 = 1100)


// Operdor de Asignación OR bit a bit -> |=
let numero = 10;  // Representación binaria: 1010
// Realiza una operación OR bit a bit con 5 y asigna el resultado
numero |= 5;  // Representación binaria de 5: 0101
console.log(numero) //  --> esto Equivale a: Resultado: 15 (1010 | 0101 = 1111)


// Operador de Asignación AND lógico -> &&=
let variable1 = true;
let variable2 = false;
// Si variable1 es verdadera, asigna el valor de variable2 a variable1
variable1 &&= variable2;
console.log(variable1);  // Resultado: false

// Operadores de Asignación OR lógico -> ||=
// Si variable1 es falsa, asigna el valor de variable2 a variable1
variable1 ||= variable2;
console.log(variable1);  // Resultado: true


// Operador de Asignación de anulación lógica 
let variable3 = null;
let variable4 = "Valor de respaldo";
// Asigna el valor de variable2 a variable1 si variable1 es nulo o indefinido
variable1 = variable3 ?? variable4;
console.log(variable1);  // Resultado: "Valor de respaldo"


// Operadores de Comparación:

let num1 = 10;
let num2 = "10";

let igualdad = num1 == num2;          // Igualdad (compara valores)
let igualdadEstricta = num1 === num2; // Igualdad estricta (compara valores y tipos)
let desigualdad = num1 != num2;       // Desigualdad (compara valores)
let desigualdadEstricta = num1 !== num2; // Desigualdad estricta (compara valores y tipos)
let mayorQue = num1 > 5;              // Mayor que
let menorQue = num1 < 15;             // Menor que

console.log(igualdad, igualdadEstricta, desigualdad, desigualdadEstricta, mayorQue, menorQue);

// Operadores Lógicos:
let condicion1 = true;
let condicion2 = false;

let and = condicion1 && condicion2; // AND lógico
let or = condicion1 || condicion2;  // OR lógico
let not = !condicion1;              // NOT lógico

console.log(and, or, not);

// Operadores Ternarios:
let edad = 20;

let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";

console.log(mensaje)


/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
*/


let nombre = 'omega';

if(nombre !== 'omegatroy'){
  console.log('no sos omega no podes pasar')
}else if(nombre === 'troy'){
  console.log('sos troy podes pasar')
} else{
  console.log('si sos omegatroy')
}

let contador = 0;

while(contador < 10){
  console.log(contador)
  contador++
}


do {
  console.log(contador);
  contador++;
} while (contador < 10);


let arreglo = [1, 2, 3];

for (let elemento in arreglo) {
    console.log(elemento);  // Imprime los índices: 0, 1, 2
}

for (let valor of arreglo) {
    console.log(valor);  // Imprime los valores: 1, 2, 3
}

let diaSemana = "lunes";

switch (diaSemana) {
    case "lunes":
        console.log("Comienzo de la semana");
        break;
    case "viernes":
        console.log("Fin de la semana");
        break;
    default:
        console.log("Día intermedio");
}

try {
  // Intenta ejecutar este bloque de código
  let resultado = 10 / 0;  // Esto lanzará una excepción de división por cero
  console.log(resultado);  // Esta línea no se ejecutará si se produce una excepción
} catch (error) {
  // Maneja la excepción aquí
  console.error("Se produjo un error:", error.message);
} finally {
  // Este bloque siempre se ejecutará, incluso si hay una excepción
  console.log("Bloque 'finally' ejecutado");
}

// El flujo del programa continúa aquí después de manejar la excepción
console.log("Programa continúa...");


/*

 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 * 
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

*/


  for(let i = 10; i <= 55; i++){
    if(i % 2 == 0 && i != 16 && i % 3 != 0){
      console.log(`Numero: ${i}`)
    }
  }


// es un poco largo lo se =)