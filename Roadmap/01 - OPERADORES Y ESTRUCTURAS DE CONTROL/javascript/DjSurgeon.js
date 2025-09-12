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

/* == Operadores de asignación == */

/* Un operador de asignación asigna un valor a su operando izquierdo basándose 
en el valor de su operando derecho. El operador de asignación simple es igual (=), 
que asigna el valor de su operando derecho a su operando izquierdo. */

console.log(`=== Operadores de asignación ===`);
let x = 1;
let y = 1;
/* Asignación */
x = y;
x = y;
let asignacion = "Hola Mundo!";
let nuevaAsignacion = asignacion;
console.log(`Operador de asignacion: ${nuevaAsignacion}`);
let operando1 = 5;
let operando2 = 2;
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de adición */
x += y;
x = x + y;
console.log(`=> Suma: ${(operando1 += operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de resta */
x -= y;
x = x - y;
console.log(`=> Resta: ${(operando1 -= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de multiplicación */
x *= y;
x = x * y;
console.log(`=> Multiplicación: ${(operando1 *= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de división */
x /= y;
x = x / y;
console.log(`=> Division: ${(operando1 /= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de residuo */
x %= y;
x = x % y;
console.log(`=> Resto: ${(operando1 %= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de exponenciación */
x **= y;
x = x ** y;
console.log(`=> Exponenciación: ${(operando1 **= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de desplazamiento a la izquierda */
/* El operador << devuelve un número o BigInt cuya representación binaria 
es el primer operando desplazado el número especificado de bits hacia la izquierda. 
Los bits sobrantes desplazados hacia la izquierda se descartan 
y los bits cero se desplazan hacia la derecha. */
x <<= y;
x = x << y;
console.log(`=> Desplazamiento a la izquierda: ${(operando1 <<= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de desplazamiento a la derecha */
x >>= y;
x = x >> y;
console.log(`=> Desplazamiento a la derecha: ${(operando1 >>= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de desplazamiento a la derecha sin signo */
x >>>= y;
x = x >>> y;
console.log(
  `=> Desplazamiento a la derecha sin signo: ${(operando1 >>>= operando2)}`
);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación AND bit a bit */
/* El operador &= realiza AND en los dos operandos 
y asigna el resultado al operando izquierdo. */
x &= y;
x = x & y;
console.log(`=> AND bit a bit: ${(operando1 &= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación XOR bit a bit */
/* El operador ^= realiza XOR en los dos operandos 
y asigna el resultado al operando izquierdo.*/
x ^= y;
x = x ^ y;
console.log(`=> XOR bit a bit: ${(operando1 ^= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación OR bit a bit */
x |= y;
x = x | y;
console.log(`=> OR bit a bit: ${(operando1 |= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación AND lógico */
/* El operador &&= solo evalúa el operando derecho y 
lo asigna al izquierdo si el operando izquierdo es truthy. */
x &&= y;
x = x && y;
console.log(`=> AND lógico: ${(operando1 &&= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación OR lógico */
/* El operador ||= solo evalúa el operando derecho y 
lo asigna al izquierdo si el operando izquierdo es falsy. */
x ||= y;
x = x || y;
console.log(`=> OR lógico: ${(operando1 ||= operando2)}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Asignación de anulación lógica */
/* El operador de asignación de anulación lógica (??=), 
también conocido como operador de asignación nula lógica, 
solo evalúa el operando derecho y asigna al izquierdo 
si el operando izquierdo es nulo o indefinido. */
x ??= y;
x = x ?? y;
console.log(`=> Anulación lógica: ${(operando1 ??= operando2)}`);

/* == Operadores de comparación == */

/* Un operador de comparación compara sus operandos y 
devuelve un valor lógico en función de si la comparación 
es verdadera (true) o falsa (false). 
Los operandos pueden ser valores numéricos, de cadena, lógicos u objetos. 
Las cadenas se comparan según el orden lexicográfico estándar, 
utilizando valores Unicode. En la mayoría de los casos, 
si los dos operandos no son del mismo tipo, JavaScript 
intenta convertirlos a un tipo apropiado para la comparación. 
Este comportamiento generalmente resulta en comparar los operandos numéricamente. 
Las únicas excepciones a la conversión de tipos dentro de las comparaciones 
involucran a los operadores === y !==, que realizan comparaciones estrictas 
de igualdad y desigualdad. Estos operadores no intentan convertir los operandos 
a tipos compatibles antes de verificar la igualdad. */

console.log(`=== Operadores de comparación ===`);
operando1 = 8;
let texto1 = "tipo num.";
operando2 = 5;
let operando3 = "5";
let texto2 = "tipo string.";
console.log(
  `Operandos: ${operando1} y ${operando2} como números y ${operando3} como cadena de texto.`
);

/* Igual */
console.log(`${operando1} ${texto1} es igual a ${operando2} ${texto1}`);
console.log(operando1 == operando2);
console.log(`${operando1} ${texto1} es igual a ${operando1} ${texto1}`);
console.log(operando1 == operando1);
console.log(`${operando2} ${texto1} es igual a ${operando3} ${texto2}`);
console.log(operando2 == operando3);

/* No es igual */
console.log(`${operando1} ${texto1} no es igual a ${operando2} ${texto1}`);
console.log(operando1 != operando2);
console.log(`${operando1} ${texto1} no es igual a ${operando1} ${texto1}`);
console.log(operando1 != operando1);
console.log(`${operando2} ${texto1} no es igual a ${operando3} ${texto2}`);
console.log(operando2 != operando3);

/* Estrictamente igual */
console.log(
  `${operando1} ${texto1} es estrictamente igual a ${operando2} ${texto1}`
);
console.log(operando1 === operando2);
console.log(
  `${operando1} ${texto1} es estrictamente igual a ${operando1} ${texto1}`
);
console.log(operando1 === operando1);
console.log(
  `${operando2} ${texto1} es estrictamente igual a ${operando3} ${texto2}`
);
console.log(operando2 === operando3);

/* Desigualdad estricta */
console.log(
  `${operando1} ${texto1} no es estrictamente igual a ${operando2} ${texto1}`
);
console.log(operando1 !== operando2);
console.log(
  `${operando1} ${texto1} no es estrictamente igual a ${operando1} ${texto1}`
);
console.log(operando1 !== operando1);
console.log(
  `${operando2} ${texto1} no es estrictamente igual a ${operando3} ${texto2}`
);
console.log(operando2 !== operando3);

/* Mayor que */
console.log(`${operando1} ${texto1} es mayor que ${operando2} ${texto1}`);
console.log(operando1 > operando2);
console.log(`${operando1} ${texto1} es mayor que ${operando1} ${texto1}`);
console.log(operando1 > operando1);
console.log(`${operando1} ${texto1} es mayor que ${operando3} ${texto2}`);
console.log(operando1 > operando3);

/* Mayor o igual que */
console.log(
  `${operando1} ${texto1} es mayor o igual que ${operando2} ${texto1}`
);
console.log(operando1 >= operando2);
console.log(
  `${operando1} ${texto1} es mayor o igual que ${operando1} ${texto1}`
);
console.log(operando1 >= operando1);
console.log(
  `${operando1} ${texto1} es mayor o igual que ${operando3} ${texto2}`
);
console.log(operando1 >= operando3);

/* Menor que */
console.log(`${operando1} ${texto1} es menor que ${operando2} ${texto1}`);
console.log(operando1 < operando2);
console.log(`${operando1} ${texto1} es menor que ${operando1} ${texto1}`);
console.log(operando1 < operando1);
console.log(`${operando1} ${texto1} es menor que ${operando3} ${texto2}`);
console.log(operando1 < operando3);

/* Menor o igual */
console.log(
  `${operando1} ${texto1} es menor o igual que ${operando2} ${texto1}`
);
console.log(operando1 <= operando2);
console.log(
  `${operando1} ${texto1} es menor o igual que ${operando1} ${texto1}`
);
console.log(operando1 <= operando1);
console.log(
  `${operando1} ${texto1} es menor o igual que ${operando3} ${texto2}`
);
console.log(operando1 <= operando3);

/* == Operadores de aritméticos == */
/* Un operador aritmético toma valores numéricos (ya sean literales o variables) 
como sus operandos y devuelve un solo valor numérico. 
Los operadores aritméticos estándar son suma (+), resta (-), multiplicación (*) y división (/). 
Estos operadores funcionan como lo hacen en la mayoría de los otros lenguajes de programación 
cuando se usan con números de punto flotante. */
console.log(`=== Operadores de comparación ===`);
operando1 = 10;
operando2 = 3;
console.log(`Operandos: ${operando1} y ${operando2}`);
/* Suma */
console.log(`=> Suma: ${operando1 + operando2}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Resta */
console.log(`=> Resta: ${operando1 - operando2}`);
console.log(`Operandos: ${operando1} y ${operando2}`);

/* Multiplicación */
console.log(`=> Multiplicación: ${operando1 * operando2}`);
console.log(`Operandos: ${operando1} y ${operando2}`);
/* División */
console.log(`=> División: ${operando1 / operando2}`);
console.log(`Operandos: ${operando1} y ${operando2}`);
/* Resto */
console.log(`=> Resto: ${operando1 % operando2}`);
console.log(`Operandos: ${operando1}`);
/* Incremento */
console.log(`=> Incremento: ${++operando1}`);
console.log(`Operandos: ${operando1}`);
/* Decremento */
console.log(`=> Decremento: ${--operando1}`);
console.log(`Operandos: ${operando1}`);
/* Negación unaria */
console.log(`=> Negación unaria: ${-operando1}`);
console.log(`Operandos: ${operando1}`);
/* Positivo unario */
console.log(`=> Positivo unario: ${+operando1}`);
console.log(`Operandos: ${operando1} y ${operando2}`);
/* Operador de exponenciación */
console.log(`=> Exponenciación: ${operando1 ** operando2}`);

/* == Operadores bit a bit == */
/* Un operador bit a bit trata a sus operandos como un conjunto de 32 bits 
(ceros y unos), en lugar de números decimales, hexadecimales u octales. 
Por ejemplo, el número decimal nueve tiene una representación binaria de 1001. 
Los operadores bit a bit realizan sus operaciones en tales representaciones binarias, 
pero devuelven valores numéricos estándar de JavaScript. */

console.log(`=== Operadores bit a bit ===`);
operando1 = 15;
operando2 = 9;
console.log(`Operandos en formato decimal: ${operando1} y ${operando2}`);
console.log(
  `Operandos en formato binario: ${operando1.toString(
    2
  )} y ${operando2.toString(2)}`
);
let resultado;

/* AND a nivel de bits */
/* Devuelve un uno en cada posición del bit para los que los bits correspondientes de ambos operandos son unos. */
resultado = operando1 & operando2;
console.log(`=> AND: ${resultado.toString(2)}`);

/* OR a nivel de bits*/
/* Devuelve un cero en cada posición de bit para el cual los bits correspondientes de ambos operandos son ceros.*/
console.log(
  `Operandos en formato binario: ${operando1.toString(
    2
  )} y ${operando2.toString(2)}`
);
resultado = operando1 | operando2;
console.log(`=> OR: ${resultado.toString(2)}`);

/* XOR a nivel de bits*/
/* Devuelve un cero en cada posición de bit para la que los bits correspondientes son iguales. 
[Devuelve uno en cada posición de bit para la que los bits correspondientes son diferentes]. */
console.log(
  `Operandos en formato binario: ${operando1.toString(
    2
  )} y ${operando2.toString(2)}`
);
resultado = operando1 ^ operando2;
console.log(`=> XOR: ${resultado.toString(2)}`);

/* NOT a nivel de bits */
/* Invierte los bits de su operando. */
console.log(`Operando en formato binario: ${operando1.toString(2)}`);
resultado = ~operando1;
console.log(`=> NOT: ${resultado.toString(2)}`);

/* Desplazamiento a la izquierda */
/* Desplaza a en representación binaria b bits hacia la izquierda, desplazándose en ceros desde la derecha. */
console.log(
  `Operandos en formato binario: ${operando1.toString(
    2
  )} y ${operando2.toString(2)}`
);
resultado = operando1 << operando2;
console.log(`=> Desplazamiento a la izquierda: ${resultado.toString(2)}`);

/* Desplazamiento a la derecha de propagación de signo */
/* Desplaza a en representación binaria b bits a la derecha, descartando los bits desplazados. */
console.log(
  `Operandos en formato binario: ${operando1.toString(
    2
  )} y ${operando2.toString(2)}`
);
resultado = operando1 >> operando2;
console.log(`=> Desplazamiento a la derecha: ${resultado.toString(2)}`);

/* Desplazamiento a la derecha de relleno cero */
/* Desplaza a en representación binaria b bits hacia la derecha, 
descartando los bits desplazados y desplazándose en ceros desde la izquierda.*/
console.log(
  `Operandos en formato binario: ${operando1.toString(
    2
  )} y ${operando2.toString(2)}`
);
resultado = operando1 >>> operando2;
console.log(
  `=> Desplazamiento a la derecha de relleno cero: ${resultado.toString(2)}`
);

/* == Operadores lógicos == */
/* Los operadores lógicos se utilizan normalmente con valores booleanos (lógicos); 
cuando lo son, devuelven un valor booleano. 
Sin embargo, los operadores && y || en realidad devuelven el valor 
de uno de los operandos especificados, por lo que si estos operadores se utilizan 
con valores no booleanos, pueden devolver un valor no booleano. */
console.log(`=== Operadores lógicos ===`);
operando1 = true;
operando2 = false;
operando3 = true;

/* AND lógico */
console.log("AND");
console.log(`Operandos booleanos: ${operando1} y ${operando2}.`);
console.log(operando1 && operando2);
console.log(`Operandos booleanos: ${operando1} y ${operando3}.`);
console.log(operando1 && operando3);
/* OR lógico */
console.log("OR");
console.log(`Operandos booleanos: ${operando1} y ${operando2}.`);
console.log(operando1 || operando2);
console.log(`Operandos booleanos: ${operando1} y ${operando3}.`);
console.log(operando1 || operando3);

/* NOT lógico */
console.log("NOT");
console.log(`Operandos booleanos: ${operando1}.`);
console.log(!operando1);
console.log(`Operandos booleanos: ${operando2}.`);
console.log(!operando2);

/* == Operadores de concatenación == */
/* Además de los operadores de comparación, que se pueden usar en valores de cadena, 
el operador de concatenación (+) concatena dos valores de cadena, 
devolviendo otra cadena que es la unión de los dos operandos de cadena. */
console.log(`=== Operadores de concatenación ===`);
let str1 = "Hola";
let str2 = "Javascript";
console.log(str1);
console.log(str2);
console.log("Concatenado: " + str1 + " " + str2);

/* == Operador condicional o ternario == */
/* El operador condicional es el único operador de JavaScript que toma tres operandos. 
El operador puede tener uno de dos valores según una condición. */
console.log(`=== Operador ternario ===`);
let edad = 20;
console.log(`Si tengo ${edad} años.`);
let estado = edad >= 18 ? "adulto" : "menor";
console.log(`Soy ${estado}.`);

edad = 5;
console.log(`Si tengo ${edad} años.`);
estado = edad >= 18 ? "adulto" : "menor";
console.log(`Soy ${estado}.`);

/* === Control de flujo y manejo de errores === */
/* == Expresiones condicionales == */
/* If ... else */
/* Utiliza la expresión if para ejecutar una instrucción si una condición lógica es true. 
Utiliza la cláusula opcional else para ejecutar una instrucción si la condición es false. */
console.log(`=== Control de flujo y manejo de errores ===`);
console.log(`== If...else ==`);

edad = 40;

if (edad === 40) {
  console.log("Estas en la flor de la vida.");
} else {
  console.log("O te has pasado o no llegas ;).");
}
// Imprime la primera declaración ya que la condicion es true.

edad = 50;

if (edad === 40) {
  console.log("Estas en la flor de la vida.");
} else if (edad < 40) {
  console.log("Necesitas madurar.");
} else if (edad > 40) {
  console.log("Disfruta de la vida.");
}
// Imprime la ultima declaración ya que es la condición true.

/* Switch */
/* Una instrucción switch permite que un programa evalúe una expresión 
e intente hacer coincidir el valor de la expresión con una etiqueta case. 
Si la encuentra, el programa ejecuta la declaración asociada. */
console.log(`== Switch ==`);
edad = 65;
switch (edad) {
  case 18:
    console.log("Has alcanzado la mayoría de edad.");
    break;
  case 40:
    console.log("Estas en la flor de la vida.");
    break;
  case 65:
    console.log("Vamos a ver si nos podemos jubilar."); //Estas es la condición a imprimir.
}

/* == Bucles e iteración == */
/* Los bucles ofrecen una forma rápida y sencilla de hacer algo repetidamente. */
/* Declaración for */
console.log(`== Bucles e iteración ==`);
console.log(`== for ==`);

for (let i = 0; i < 10; i++) {
  console.log(i);
}

console.log(`== do...while ==`);
let i = 5;
do {
  console.log(i);
  i++;
} while (i < 10);

console.log(`== while ==`);
i = 5;
while(i < 10) {
  i++
  console.log(i);
}

/* == Manejo de excepciones == */
console.log(`== Manejo de excepciones ==`);
console.log(`== Try-cath ==`);
const errNum = 1;

try {
  if (errNum === 1) {
    throw new Error('número 1.');
  }
  else {
    console.log("El error no es el número 1.");
  } 
} catch (error) {
  console.log(`El problema proviene del error: ${error.message}`);
}


/* Ejercicio Extra */
console.log(`== Ejercicio extra ==`);

for (i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i !== 16 && i % 3 === 0) {
    console.log(i);
  }
}
