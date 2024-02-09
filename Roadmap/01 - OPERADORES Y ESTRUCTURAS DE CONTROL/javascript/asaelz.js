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

/********************************
 ** TIPOS DE OPERADORES EN JS
 * 1. Operadores de asignación
 * 2. Operadores de comparación
 * 3. Operadores aritméticos 
 * 4. Operadores lógicos 
 * 5. Operadores de cadena
 * 6. Operador condicional ternario
 * 7. Operadores coma 
 * 8. Operadores unitarios 
 * 9. Operadores relacionales 
 *********************************/

/* 1. Operadores de asignación */
/**
 *  Es utilizado para asignar un valor a su operando izquierdo basándose en el valor de 
 *  su operando derecho.
 *  Ejemplo: x=y, x ahora tiene el valor de y asignado.
 *  Existen algunas variantes tales como: 
 *  Asignación de adición: x += y esto se refiere a x = x + y
 *  Asignación de resta: x -= y esto se refiere a x = x - y
 */
let x = 1, y = 2
x += 1
y -= 2

/* 2. Operadores de comparación */
/**
 * Compara sus operandos y devuelve un valor lógico en función de su la comparación es verdadera (true) 
 * o falsa (false).
 */
let ItemsSolicitados = 1, Stock = "1"
/**
 * Igual (=) -> Devuelve true si los operadores son iguales, sin importar el tipo, como vemos en el ejemplo:
 * ItemsSolicitados es Number y Stock es String pero ambos contienen el numero 1
 */
let resultado = ItemsSolicitados == Stock // true 
/**
 * No es igual (!=) Devuelve true si los operadores no son iguales
 */
resultado = ItemsSolicitados != stock // false
/**
 * Estrictamente igual (===) Devuelve true si los operadores y tipos son iguales
 */
resultado = ItemsSolicitados === stock
/**
 * Mayor que (>)
 * Menor que (<)
 * Mayor o igual que (>=)
 * Menor o igual que (<=)
 */
Stock = 5
console.log(ItemsSolicitados > Stock) //false 
console.log(ItemsSolicitados < Stock) //true
console.log(ItemsSolicitados >= Stock) // false 
console.log(ItemsSolicitados <= Stock) // true

/**
 * 3. OPERADORES ARITMETICOS
 * Residuo %
 * Incremento ++
 * Decremento --
 * Negación Unitaria -
 * Positivo Unitario +
 * Exponenciación **
 */
console.log(12 % 5) // 2
++Stock // 6
--Stock // 5
-Stock // -5
+Stock // 5
console.log(2 ** 3) // 8  

/**
 * 4. OPERADORES LOGICOS
 * && AND
 * || OR
 * -! NOT
*/
console.log(true && true) //true 
console.log(true || true) //true 
console.log(!true) //false 

/**
 *  5. OPERADORES DE CADENA
 */
console.log("esto" + "es un ejemplo")
/**
 * 6. OPERADOR TERNARIO 
 */
let edad = 15
console.log(edad >= 18 ? "puede votar": "no puede votar xd")
/**
 * 7. OPERADOR COMA
 */
for (let i=0, j=2; i<=j; i++, j--){
    console.log(i, j)
}
/**
 * 8.OPERADORES UNITARIOS
 * delete
 * typeof
 */
console.log(typeof true)
/**
 * 9.OPERADORES RELACIONES
 * IN 
 */
let prueba = ['prueba', 'de', 'operador', 'in']
console.log(0 in prueba) // true porque el indice 0 si esta contenido
/**
 * ESTRUCTURAS DE CONTROL
 */
if (edad >=18)
{
    console.log("Sos mayor de edad xd")
} 
else {
    console.log("Sorry, todavia estas peque")
}

/** BUCLE FOR*/
const etapa = 2
for (let index = 0; index < etapa; index++) {
    console.log("Etapa: " +etapa) 
}
/**WHILE */
let etapas = 1
while (etapas <= 2) {
    etapas++
}
console.log("Etapa actual: " +etapas)
/*SWITCH*/
switch ("Lunes") {
    case "Lunes":
        console.log("Es Lunes, te toca levantarte antes")
        break;

    default:
        console.log("No es Lunes, puedes dormir más")
        break;
}

/* DIFICULTAD EXTRA */
for (let index = 10; index <= 55; index++) {
    
    if (index%2===0 && index != 16 && index%3!=0){
        console.log(index)
    }
    
}

