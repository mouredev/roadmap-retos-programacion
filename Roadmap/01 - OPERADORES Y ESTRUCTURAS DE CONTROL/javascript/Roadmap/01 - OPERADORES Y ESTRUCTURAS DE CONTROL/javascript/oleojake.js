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

// OPERADORES ARITMÉTICOS
let suma = 1 + 1;
let resta = 2 - 1;
let multiplicación = 2 * 3;
let división = 6 / 2;
let residuo = 12 & 5; // En este  caso devolvería 2;
let exponenciacion = 2 ** 3 // 2 elevado a 3

// OPERADORES ASIGNACIÓN
let x = 2; // Asicnación
x += 1; // x = x + 1
x -= 1; // x = x - 1
x *= 1; // x = x * 1
x /= 1; // x = x / 1
x %= 2; // x = x % 2
x **= 2; // x = x ** 2

// OPERADORES DE COMPARACIÓN
let y = 3;
console.log(y == '3'); // Comprueba igualdad de valores pero no el tipo. TRUE
console.log(y != '4'); // Comprueba diferencia de valores pero no el tipo. TRUE
console.log(y === 3); // Comprueba igualdad de valores y tipo. TRUE
console.log(y !== 4); // Comprueba igualdad de valores y tipo. TRUE
console.log(y > 1); // Comprueba si es mayor. TRUE
console.log(y >=3 ) // Comprueba is es mayor o igual. TRUE
console.log(y < 5); // Comprueba si es menor. TRUE
console.log(y <=3 ) // Comprueba is es menor o igual. TRUE

// OPERADORES DE CADENA
let nombreCompleto = "Pablo" + " " +"Marzal";
console.log(nombreCompleto); // Pablo Marzal

// OPERADORES LÓGICOS

// Operador ternario (es el único con tres operandos) Si es TRUE, coge el primer valor, si es FALSE el segundo
let edad = 18
let edadStatus = edad >= 18 ? "Mayor de edad" : "Menor de edad";
console.log(edadStatus); // Mayor de edad

// AND &&
// Devuelve expr1 si se puede convertir a false; de lo contrario, devuelve expr2. 
// Por lo tanto, cuando se usa con valores booleanos, && devuelve true
// si ambos operandos son true; de lo contrario, devuelve false.
console.log(true && true); // t && t devuelve true
console.log(true && false); // t && f devuelve false
console.log(false && true); // f && t devuelve false
console.log(false && false); // f && f devuelve false
console.log(false && 3 == 4); // f && f devuelve false
console.log("Cat" && "Dog"); // t && t devuelve Dog
console.log(false && "Cat"); // f && t devuelve false
console.log("Cat" && false); // t && f devuelve false

// OR ||
// Devuelve expr1 si se puede convertir a true; de lo contrario, devuelve expr2.
// Por lo tanto, cuando se usa con valores booleanos, || devuelve true
// si alguno de los operandos es true; si ambos son falsos, devuelve false.
console.log(true || true); // t || t devuelve true
console.log(true || false); // t || f devuelve false
console.log(false || true); // f || t devuelve false
console.log(false || false); // f || f devuelve false
console.log(false || 3 == 4); // f || f devuelve false
console.log("Cat" || "Dog"); // t || t devuelve Cat
console.log(false || "Cat"); // f || t devuelve Cat
console.log("Cat" || false); // t || f devuelve Cat

// NOT Lógico !
//Devuelve false si su único operando se puede convertir a true;
//de lo contrario, devuelve true.
console.log(n1 = !true); // !t devuelve false
console.log(n2 = !false); // !f devuelve true
console.log(n3 = !"Cat"); // !t devuelve false

// Operador Anulación Lógica
// Para cambiar valor de una variable null o undefined
let myNull = null;
myNull ??= 10;
console.log(myNull);

let myUndefined = undefined;
myUndefined ??= 20;
console.log(myUndefined);

// OPERADORES DE BITS 
// a & b	Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos son unos.
// a | b	Devuelve un cero en cada posición de bit para el cual los bits correspondientes de ambos operandos son ceros.
// a ^ b	Devuelve un cero en cada posición de bit para la que los bits correspondientes son iguales.
// ~ a	Invierte los bits de su operando.
// a << b	Desplaza a en representación binaria b bits hacia la izquierda, desplazándose en ceros desde la derecha.
// a >> b	Desplaza a en representación binaria b bits a la derecha, descartando los bits desplazados.
// a >>> b	Desplaza a en representación binaria b bits hacia la derecha, descartando los bits desplazados y desplazándose en ceros desde la izquierda.

let a = 9; // en bits: 1001
let b = 14; // en bits: 1110

console.log(a & b); // 1000 (8)
console.log(a | b); // 1111 (15)
console.log(a ^ b); // 0111 (7)

console.log(a << 1); // Devuelve 00010010 (18)
console.log(a << 2); // Devuelve 00100100 (36)
console.log(a << 3); // Devuelve 01001000 (72)
console.log(a << 4); // Devuelve 10010000 (144)


// ESTRUCTURAS DE CONTROL

// IF/ELSE
let notaExamen = 7.5;
if (notaExamen < 5){
    console.log ("He suspendido con un " +notaExamen);
} else if (notaExamen >= 5 && notaExamen < 7){
    console.log ("He aprobado un suficiente");
} else if (notaExamen >= 7 && notaExamen < 9){
    console.log ("He aprobado un notable");
} else{
    console.log ("He aprobado un sobresaliente");
}

// SWITCH
let provincia = "Alicante"
switch (provincia) {
    case 'Alicante':
        console.log('Soy de la provincia de ' + provincia);
        break;
    case 'Valencia':
        console.log('Soy de la provincia de ' + provincia);
        break;
    case 'Castellón':
        console.log('Soy de la provincia de ' + provincia);
        break;
    default:
        console.log('No soy de la Comunidad Valenciana');
        break;
}

//FOR
for (var i = 0; i < 3; i++ ){
    console.log ("Este es el paso del bucle for número: " + i)
}

//FOR of
let myArray = ["Pablo", "Marzal", 30];
for (const value of myArray) {
    console.log(value);
}

// WHILE

var i = 0;
while (i <= 3){
    console.log ("Paso bucle while número: " + i);
    i++;
}

// do WHILE
var i = 3;
do{
    console.log ("Esto es una cuenta atrás, tic, tac: " + i);
    i--;
} while (i > 0);
console.log("BOOM");

// MANEJO DE EXCEPCIONESS
try {
    const PI = 3.14
    PI = 0;
} catch (e) {
    console.log(e.message); //TypeError: Assignment to constant variable
} finally{
        console.log ("Finalizando el try catch");
}       

// EJERCICIO EXTRA
//Crea un programa que imprima por consola todos los números comprendidos
//entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for (var i = 10; i <= 55; i++) {
    if((i % 2 == 0) && (i != 16) && (i % 3 != 0)){
        console.log (i);
    }
}