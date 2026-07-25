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
//Operador de asiganción
let a = 1;
let b = 2;
//Operadores de comparación
let igual = a == b;
let diferente = a != b;
let mayorQue = a > b;
let menorQue = a < b;
let mayorIgualQue = a >= b; // igual para <=
let estrictamenteIgual = a === b; //Compara valor y tipo
let estrictamenteDiferente = a !== b; //Compara valor y tipo
//Operadores aritmeticos
let suma = a + b;
let resta = a - b;
let multiplicacion = a * b;
let division = a / b;
let moudlo = a % b; //Devuelve el resto de la división
let exponete = a ** b;
let incremento = a++;
let decremento = a--;
//Operadores lógicos
let and = a && b;
let or = a || b;
let negacion = a != b;
//Operador ternario (condicional)
let ternario = a >= b ? "es mayor" : "es menor";
//Existen operadores unarios, que operan con un solo operandor. Ademas de los de incremento y decremento y el de asiganción hay algunos especiales:
/*Operadores unarios especiales:
    - delete (elimina una propiedad de un objeto)
    - typeof (devuelve el tipo de dato)
    - void (ejecuta la expresion pero no devuelve nada, se usa para ejecutar funciones que devuelven algo y no queremos ese valor)
    - in (devuelve true si el operando es propiedad del objeto)
    - instanceof (devuelve true si el operando es instancia de la clase o constructor)
*/
//Ejemplos de tipos de estructuras de control de JavaScript
//Condicionales
if (a === b) {
  console.log("a y b son iguales");
} else if (a > b) {
  console.log("a es mayor que b");
} else {
  console.log("b es mayor que a");
}

switch (a) {
  case "uno":
    console.log("a es uno");
    break;
  case 1:
    console.log("a es 1");
    break;
  case b:
    console.log("a es igual q b");
    break;
}

//Bucles
for (let i = 0; i < 2; i++) {
  console.log("el valor de i en este bucle for es = " + i);
}

while (a < 3) {
  console.log("el valor de a en este bucle while es = " + a);
  a++;
}

do {
  console.log("el valor de b en este do while es = " + b);
  b++;
} while (b < 5);

//Función que imprime en consola todos los numeros entre 10 y 55 que no son multiplos de 3 ni el numero 16

let impDel10Al55 = function(){
    for (let i = 10; i <= 55; i++){
        if (i % 3 !== 0 && i !== 16){
            console.log(i);
        }
    }
}
impDel10Al55();