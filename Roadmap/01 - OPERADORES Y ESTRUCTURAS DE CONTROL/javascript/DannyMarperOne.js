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



/* OPERADORES */

// Operadores de asignación
let x = 3; //Asignación
x += 2; //Suma y asignación
console.log(x);
x *= 2; //Multiplicación y asignación
console.log(x);
x -= 2; //Resta y asignación
console.log(x);
x /= 2; //División y asignación
console.log(x);
x %= 2; //Residuo y asignación
console.log(x);
x **= 2; //Exponenciación y asignación
console.log(x);

// Operadores de comparación

let var1 = 3,
    var2 = 4;

// Los siguientes ejemplos siempre retornarn true
3 == var1; //Igual
"3" == var1; //Igual
3 == '3'; //Igual
var1 != 4; //No es igual
var2 != '3'; //No es igual
3 === var1; //Estrictamente igual
var1 !== "3"; //Estrictamente desigual
3 !== '3'; //Estrictamente desigual
var2 > var1; //Mayor que
"12" > 2; //Mayor que
var2 >= var1; //Mayor o igual que
var1 >= 1; //Mayor o igual que 
var1 < var2; //Menor que
"2" < 12; //Menor que
var1 <= var2; //Menor o igual que
var2 <= "5"; //Menor o igual que


// Operadores aritmeticos

12 % 5; //Residuo
++3; //Incremento prefijo
3++; //Incremento sufijo
--3; //Decremento prefijo
3--; //Decremento sufijo
-
3; //Negación unaria
+
4; //Positivo unario (Intenta convertir al operando en un número si aún no lo es)
2 ** 3; //Operador de exponenciación


// Operadores Bit

a & b; //AND a nivel bits
a | b; //OR a nivel bits
a ^ b; //XOR a nivel bits
~a //NOT a nivel bits


//Operadores Logicos

// AND
var a1 = true && true; // t && t devuelve true
var a2 = true && false; // t && f devuelve false
var a3 = false && true; // f && t devuelve false
var a4 = false && 3 == 4; // f && f devuelve false
var a5 = "Cat" && "Dog"; // t && t devuelve Dog
var a6 = false && "Cat"; // f && t devuelve false
var a7 = "Cat" && false; // t && f devuelve false

// OR
var o1 = true || true; // t || t devuelve true
var o2 = false || true; // f || t devuelve true
var o3 = true || false; // t || f devuelve true
var o4 = false || 3 == 4; // f || f devuelve false
var o5 = "Cat" || "Dog"; // t || t devuelve Cat
var o6 = false || "Cat"; // f || t devuelve Cat
var o7 = "Cat" || false; // t || f devuelve Cat

// NOT
var n1 = !true; // !t devuelve false
var n2 = !false; // !f devuelve true
var n3 = !"Cat"; // !t devuelve false

// Operadores de cadena

console.log("Hola" + "Javascript"); //Devuelve la concatenación de la cadena "Hola Javascript"

// Operador condicional (Ternario)
let status = edad >= 18 ? "adulto" : "joven"; //Devuelve el valor de la condición

//Operador coma
for (var i = 0, j = 9; i <= j; i++, j--); //Permite que se evaluen múltiples variable a la vez





/* ESTRUCTURAS DE CONTROL */

// IF - ELSE
const mayorEdad = 18;
if (mayorEdad >= 18) {
    console.log(`La persona tiene ${mayorEdad} años y puede conducir beber alcohol`);
} else {
    console.log(`Esta persona aún tiene ${mayorEdad} años y no tiene permitido beber alcohol`);
}

// Operador ternario
let hi = "Hola a todos";
let hola = hi === "Hola a todos" ? console.log("Saludo de bienvenida") : console.log("Cualquier otra cosa");

let domir = true ? console.log("A mimir") : console.log("Aún es temprano");

// Switch
number = 10;
switch (number) {
    case 25:
        console.log("FIRST CASE");
        break;
    case 11:
        console.log("SECOND CASE");
        break;
    default:
        console.log("NONE");
        break;
}

// While
let i = 0;
while (i < 20) {
    if (i % 2 == 0) {
        console.log(i)
    }
    i++
}

// Do-While
let o = 40;
do {
    console.log("Hola Javascript");
    o++
} while (o <= 45);


// For
for (i = 1; i < 10; i++) {
    console.log(`El valor de i es ${i}`)
}

// Try - Catch
try {
    console.log('Inicio de ejecuciones try'); // (1) <--
    lalala; // error, variable no está definida!
    console.log('Fin de try (nunca alcanzado)'); // (2)
} catch (err) {
    console.log(`¡Un error ha ocurrido!`); // (3) <--
}


// Ejercicio extra
/* 
Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

let i = 10;
for (i; i <= 55; i++) {
    if (i % 3 !== 0 && i !== 16) {
        console.log(`${i}`);
    }
}