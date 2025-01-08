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

// +++++++++ OPERADORES DE ASIGNACIÓN +++++++++
x = y; // Asignación.
x += y; // Asignación de adición: x = x + y
x -= y; // Asinación de resta: x = x - y
x *= y; // Asignación de multiplicación: x = x * y
x /= y; // Asignación de multiplicación: x = x / y
x %= y; // Asignación de residuo: x = x % y
x **= y; // Asignación de exponenciación: x = x ** y
x <<= y; // Asignación de desplazamiento a la izquierda: x = x << y
x >>= y; // Asignación de desplazamiento a la derecha: x = x >> y
x >>>= y; // Asignación de desplazamiento a la derecha sin signo: x = x >>> y
x &= y; // Asignación AND bit a bit: x = x & y
x ^= y; // Asignación XOR bit a bit
x |= y; // Asignación OR bit a bit: x = x | y
x && y; // Asignación AND lógico: x && (x = y)
x ||= y; // Asignación OR lógico: x || (x = y)
x ??= y; // Asignación de anulación lógica: x ?? (x = y)

// +++++++++ OPERADORES DE COMPARACIÓN +++++++++
x == y; // Igual
x != y; // No es igual
x === y; // Estrictamente igual
x !== y; // Desigualdad estricta
x > y; // Mayor que
x >= y; // Mayor o igual que
x < y; // Menor que
x <= y; // Menor o igual que

// +++++++++ OPERADORES ARITMÉTICOS +++++++++
x + y; // Suma
x - y; // Resta
x * y; // Multiplicación
x / y; // División
x % y; // Residuo
x++; // Incremento
x--; // Decremento
-x; // Negación unario
+"3"; // Positivo unario
x ** y; // Operador de exponenciación

// +++++++++ OPERADORES BIT A BIT +++++++++
a & b; // AND a nivel de bits
a | b; // OR a nivel de bits
a ^ b; // XOR a nivel de bits
~ a; // NOT a nivel de bits
a << b; // Desplazamiento a la izquierda
a >> b; // Desplazamiento a la derecha de propagación de signo
a >>> b; // Desplazamiento a la derecha de relleno de cero

// +++++++++ OPERADORES LÓGICOS +++++++++
true && x == x; // AND lógico
true || x == y; // OR lógico
!true; // NOT lógico

// +++++++++ OPERADORES DE CADENA +++++++++
var myString = "Ra";
myString + "úl"; // Concatenación
myString += "úl"; // Concatenación por asignación abreviada

// +++++++++ OPERADOR CONDICIONAL (TERNARIO) +++++++++
var status = age >= 18 ? "Adult" : "Minor";

// +++++++++ OPERADOR COMA +++++++++
var x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
var a = [x, x, x, x, x];

for (var i = 0, j = 9; i <= j; i++, j--) {
  console.log("a[" + i + "][" + j + "]= " + a[i][j]);
}

// +++++++++ OPERADORES UNARIOS +++++++++
z = 33;
delete z; // Devuelve true si z se crea implícitamente
typeof myString; // Devuelve "string"
void (2 === "2"); // Devuelve undefined

//  +++++++++ OPERADORES RELACIONALES +++++++++
"PI" in Math; // Operador in
var theDay = new Date(1995, 12, 17);
if (theDay instanceof Date) { // Operador intanceof
  console.log("Si theDay es un objeto Date, las instrucciones de la expresión if se ejecutan.");
}

// +++++++++ ESTRUCTURAS DE CONTROL +++++++++

// if / else if / else
var firstName = "Samus";

if (firstName == "Samus") {
  console.log("Su nombre es Samus Aran.");
} else if (firstName == "Adam") {
  console.log("Su nombre es Adam Malkovich.")
} else {
  console.log("No hay registro del nombre.");
}

// switch
switch (2 + 2 === 4) {
  case true:
    console.log("La suma es correcta.");
    break;

  case false:
    console.log("La suma es incorrecta.");

  default:
    console.log("Error en la operación.");
    break;
}

// while
var iterationCount = 0;

while(iterationCount < 5) {
  iterationCount++;
  console.log("Número " + iterationCount);
}

// do...while
var iterationCount = 0;

do {
  iterationCount++;
  console.log("Número " + iterationCount);
} while (iterationCount < 10);

// for
for (let index = 0; index < 7; index++) {
  console.log("Número " + index);
}


// DIFICULTAD EXTRA
for(index = 10; index <= 55; index++) {
	if (index !== 55) {
  	if (index  === 16 || index % 3 === 0 || index % 2 !== 0) {
      continue;
    }
  }

	console.log("Número " + index);
}
