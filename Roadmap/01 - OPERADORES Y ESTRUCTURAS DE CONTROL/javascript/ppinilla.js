//01 OPERADORES Y ESTRUCTURAS DE CONTROL

/*
EJERCICIO:
 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
 Condicionales, iterativas, excepciones...
 - Debes hacer print por consola del resultado de todos los ejemplos.

 DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

 Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

//- Tipos de operadores
//Operadores de asignación
let x = 10, y = 5;
console.log('Operadores de asignación x =', x, 'y =', y);
console.log("Asignación: x = y =", x = y);
console.log('x =', x, 'y =', y);
console.log("Asignación de suma: x += y =", x += y);
console.log('x =', x, 'y =', y);
console.log("Asignación de resta: x -= y =", x -= y);
console.log('x =', x, 'y =', y);
console.log("Asignación de multiplicación: x *= y =", x *= y);
console.log('x =', x, 'y =', y);
console.log("Asignación de división: x /= y =", x /= y);
console.log('x =', x, 'y =', y);
console.log("Asignación de resto: x %= y =", x %= y);
console.log('x =', x, 'y =', y);
console.log("Asignación de exponenciación: y **= x =", y **= x);
console.log('x =', x, 'y =', y);
x = 10, y = 5
console.log("Asignación de desplazamiento a la izquierda: x <<= 2 =", x <<= 2);
console.log('x =', x);
console.log("Asignación de desplazamiento a la derecha: x >>= 2 =", x >>= 2);
console.log('x =', x);
console.log("Asignación de desplazamiento a la derecha sin signo: x >>>= 2 =", x >>>= 2);
console.log('x =', x);
x = 9, y = 14
console.log("Asignación AND bit a bit: 9 &= 14 =", x &= y)
console.log('x =', x);
console.log("Asignación XOR bit a bit: x ^= 14 =", x ^= y);
console.log('x =', x);
console.log("Asignación OR bit a bit: x |= 14 =", x |= y);
console.log('x =', x);
console.log("Asignación AND lógico: x &&= 14 =", x &&= y);
console.log('x =', x);
console.log("Asignación OR lógico: x ||= 14 =", x ||= y);
console.log('x =', x);
console.log("Asignación de anulación lógica: x ??= 14 =", x ??= y);
console.log('x =', x);

//Operadores Aritméticos
x = 10, y = 5;
console.log('Operadores aritméticos: x =', x, 'y =', y);
console.log("Suma:", x + y );
console.log("Resta:", x - y );
console.log("Multiplicación:", x * y );
console.log("División:", x / y );
console.log("Residuo:", x % y );
console.log("Exponenciación:", x ** y );
console.log("Incremento:", ++x );
console.log("Decremento:", --y );
console.log("Positivo unario:", +x );
console.log("Negativo unario:", -x );

//Operadores bit a bit
x = 9, y = 14;
console.log('Operadores bit a bit: x =', x, 'y =', y);
console.log("AND a nivel de bits: x & y =", x & y)
console.log("XOR a nivel de bits: x ^ 14 =", x ^ y);
console.log("OR a nivel de bits:: x | 14 =", x | y);
console.log("NOT a nivel de bits: ~ x =", ~ x);
console.log("Desplazamiento a la izquierda: y << 2 =", y << 2);
console.log("Desplazamiento a la derecha de propagación de signo: y >> 2 =", y >> 2);
console.log("Desplazamiento a la derecha de relleno cero: x >>> 2 =", y >>> 2);

//Operadores de comparación
console.log('Operadores de comparación: x =', x, 'y =', y);
console.log(x, '>', y, "'Mayor que': ", x > y);
console.log(x, '<', y, "'Menor que': ", x < y);
console.log(x, '>=', y, "'Mayor o igual que': ", x >= y);
console.log(x, '<=', y, "'Menor o igual que': ", x <= y);
console.log(x, '==', y, "'Igual': ", x == y);
console.log(x, '===', y, "'Estrictamente igual': ", x === y);
console.log(x, '!=', y, "'Distinto': ", x != y);
console.log(x, '!==', y, "'Estrictamente distinto': ", x !== y);

//Operandos lógicos
console.log('Operandos lógicos: x =', x, 'y =', y); 
console.log("AND: x && y =", x && y); //Devuelve y si ambos operandos son true; de lo contrario, devuelve x.
console.log("OR: x || y =", x || y); //Devuelve x si el operando x es true, devuelve y si el operando x es false; si ambos son falsos, devuelve y.
console.log("NOT: !x =", !x); //Devuelve false si su operando es true; de lo contrario, devuelve true.

//Operador de cadena
let a = 'Operador', b = 'cadena';
console.log(a + ' de ' + b, 'a + b');

//Operador condicional (ternario)
console.log('Operador condicional');
let age = 24;
let estado = age >= 18 ? "adulto" : "menor";
console.log("condition ? val1 : val2 ¿Es adulto o menor?", estado);

//Operador coma
console.log('Operador coma');
var n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
var m = [x, x, x, x, x];

for (var i = 0, j = 9; i <= j; i++, j--)
    console.log("m[" + i + "][" + j + "]= " + i + j);

//Operandores unarios
console.log('Operadores unarios');
z = 10; //implicitamente crea window.z
var h = 24;
let myObj = { x: 10 };
let diaSem = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sábado', 'domingo'];
let theDay = new Date(2025, 1, 28);
console.log('delete object.property:')
console.log('delete myObj:', delete myObj.x);
console.log('delete.z:', delete z);
console.log('delete.nameVar:', delete h); //No se puede borrar si se declara con var
console.log('typeof operand');
console.log('typeof object:', typeof myObj);
console.log('typeof true:', typeof true);
console.log('void (expression)');
console.log('propNameorNumber in objectName');
console.log('2 in diaSem:', 2 in diaSem);
console.log('8 in diaSem:', 8 in diaSem);
console.log('objectName instanceOf objectType');
if (theDay instanceof Date){
    console.log('the Day instanceof Date: true');
    
}

//- Tipos de estructuras de control
//Condicionales
console.log('Expresión if...else: if (condition) { statement_1; } else { statement_2; }');
let deuda = 300001
if (deuda > 300000) {
    console.log("Bienvenido al juego del calamar");
} else {
    console.log("No puedes entrar al juego del calamar. Deuda menor a $300000");
}

//Bucles
console.log('Expresión switch: switch (expression) { case label_1: statements_1 [break;]  case label_2: statements_2 [break] ... default: statements_def [break;] }');
let juego = 'Luz roja, luz verde'
switch (juego) {
    case 'Luz roja, luz verde':
        console.log('Jugaremos, muevete luz verde');
        break;
    case 'Pentatlon de seis piernas':
        console.log('ddakji, biseokchigi, gong-gi, jegi y peonza');
        break;
    case 'Mingle':
        console.log('Formen grupos de 5');
        break;
    default:
        console.log('Ese juego no existe');
        break;
}

console.log('Expresión for: for (begin; condition; step) { loopBody }');
const juegos = 6;
for (let juego = 1; juego <= juegos; juego++){
    console.log("Bienvenidos al juego: ", juego);
}

console.log('Expresión while: while (condition) { loopBody }');
i = 0;
while (i < 6) {
    console.log('Felicitaciones, pasas al siguiente juego');
    i++
}

console.log('Expresión do...while: do { } while (condition);');
i = 0
do {
    console.log('Felicitaciones, pasas al siguiente juego');
    i++;
} while (i < 6);

//- Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.


for (let i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 !== 0) {
        console.log(i);
    }
}

  







