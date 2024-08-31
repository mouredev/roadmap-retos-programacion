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
 */

// Operadores de asignación
let x = 1;      // Asignación
console.log("El valor de la variable x es: " + x);

x += 1;         // Asignación de adición
console.log("Si a x le sumamos 1 su valor es: " + x);

x -= 1;         // Asignación de resta
console.log("Si a x le restamos 1 su valor es: " + x);

x *= 2;         // Asignación de multiplicación
console.log("Si x lo multiplicamos por 2 su valor es: " + x);

x /= 2;         // Asignación de división
console.log("Si x lo dividimos entre 2 su valor es: " + x);

x = 7;         
x %= 2;         // Asignación de residuo
console.log("Le hemos dado a x el valor 7. Si ahora le asignamos el residuo de la división entre 2 su valor es: " + x);

x = 4;
x **= 2;        // Asignación de exponenciación
console.log("Ahora le hemos asignado a x el valor 4. Si elevamos a 2 el valor de x, ahora su valor es: " + x);

x = 16;
x <<= 2;        // Asignación de desplazamiento a la izq.
console.log("Ahora x vale 16. Si deplazamos dos bits a la izquierda obtenemos el valor: " + x);

x = 16;
x >>= 2;        // Asignación de desplazamiento a la der.
console.log("Ahora x vale 16. Si desplazamos 2 bits a la derecha obtenemos el valor: " + x);

x = 10;
x &= 2;         // Asignación AND bit a bit
console.log("Ahora x vale 10. Si hacemos una operación AND bit a bit con 2 obtenemos el valor: " + x);

x = 10;
x ^= 12;         // Asignación XOR bit a bit
console.log("Ahora x vale 10. Si hacemos una operación XOR bit a bit con 12 obtenemos el valor: " + x);

x = 10;
x |= 2;         // Asignación OR bit a bit
console.log("Ahora x vale 10. Si hacemos la operación OR bit a bit con 2 obtenemos el valor: " + x);

x = 5;
x &&= 2;        // Asignación AND lógico (es equivalente a "if(x){x=2}")
console.log("Ahora x vale 5. Si hacemos la operación AND lógico con 2 obtenemos el valor: " + x);

x = 0;
x ||= 2;        // Asignación OR lógico (es equivalente a "x=x||y")
console.log("Ahora x vale 0. Si hacemos la operación OR lógico con 2 obtenemos el valor: " + x);

x = null;
x ??= 5;        // Asignaciónde anulación lógica
console.log("Ahora x vale NULL. Si hacemos la opereación de anulación lógica con 5 obtenemos el valor: "+ x);

// Operadores de comparación
x = 1;     
let y = x == 1;  // Igual
console.log("Ahora x vale 1. Si hacemos una comparación de igualdad con 1 obtenemos el valor: " + y);
let k = x == 4;
console.log("Mientras que si lo comparamos con 4 obtenemos: " + k);

x = 4
y = x != 3;     // Distinto de
console.log("Ahora x vale 4. Si hacemos una comparación de desigualdad con 3 obtenemos que: " + y);
k = x != 4;
console.log("Mientras que si lo comparamos con 4 obtenemos que: " + k)

x = 1;
y = x === 1;    // Estrictamente igual
console.log("Ahora x vale 1. Si hacemos una comparación de estricta igualdad con 1 entero obtenemos que: " + y);
k = x === "1";
console.log("Mientras que si lo comparamos con 1 en string obtenemos que: " + k);

x = 3;
y = x !== 4;    // Desigualdad estricta
console.log("Ahora x vale 3. Si hacemos una comparación de desigualdad con 4 obtenemos que: " + y);
k = x !== 3;
console.log("Mientras que si lo comparamos con 3 obtenemos: " + k);


x = 1;
y = x > 0;      // Mayor que
console.log("Ahora x vale 1. Si hacemos una comparación de mayor que 0 obtenemos: " + y);
k = x > 1;
console.log("Mientras que si lo comparamos con 1 obtenemos: " + k);


x = 0;
y = x >= 0;     // Mayor o igual que
console.log("Ahora x vale 0. Si hacemos una comparación de mayor o igual que 0 obtenemos: " + y);
k = x >= -1;
console.log("Mientras que si lo comparamos con -1")

x = 1;
y = x < 2;      // Menor que
console.log("Ahora x vale 1. Si hacemos una comparación de menor que 2 obtenemos: " + y);
k = x < 1;
console.log("Mientras que si lo comparamos con 1: " + k);

x = 1;
y = x <= 1;     // Menor o igual que
console.log("Ahora x vale 1. Si hacemos una comparación de menor que 2 obtenemos: " + y);
k = x <= 2;
console.log("Mientras que si lo comparamos con 2: " + k);


// Operadores aritméticos
x = 12 % 5;     // Residuo
console.log("El residuo de 12 entre 5 es: " + x);

++x;        // Incremento
console.log("Tras ejecutar el incremento de x obtenemos: " + x);

--x;        // Decremento
console.log("Tras ejecutar el decremento de x obtenemos: " + x);

x = -x;         // Negación unaria
console.log("Tras ejecutar la negación unaria de x obtenemos: " + x);

x = +x;         // Positivo unario
console.log("Tras ejecutar el positivo unario de x obtenemos: " + x);

x = 2;
x = x ** 4;     // Exponenciación
console.log("Ahora x vale 2. Si lo elevamos a 4 obtenemos: " + x);

// Operadores bit a bit
x = 5 & 3
console.log("El operador AND a nivel de bits entre 5 y 3 retorna un valor de: " + x);      // AND a nivel de bits 

x = 5 | 3;      // OR a nivel de bits
console.log("El operador OR a nivel de bits entre 5 y 3 retorna un valor de: " + x);

5 ^ 3;      // XOR a nivel de bits
console.log("El operador XOR a nivel de bits entre 5 y 3 retorna un valor de " + x);

x = ~5;        // NOT a nivel de bits
console.log("El operador NOT a nivel de bits de 5 retorna un valor de: " + x);

x = 5 << 1;     // Desplazamiento a la izquierda
console.log("Con el desplazamiento de bits a la izquierda entre 5 y 1 obtenemos un valor: " + x);

x = 10 >> 1;     // Desplazamiento a la derecha
console.log("Con el desplazamiento de bits a la derecha entre 10 y 1 obtenemos un valor: " + x);

x = -10 >>> 1;    // Desplazamiento a la derecha de relleno cero
console.log("Con el desplazamiento de bits a la derecha de relleno 0 entre -10 y 1 obtenemos un valor: " + x);


// Operadores lógicos
let a = true;
let b = true;
if(a && b) {    // AND lógico
    console.log("Este mensaje se muestra dado que hemos hecho una comparación de AND lógico entre 'a' y 'b' siendo ambos true");
}

b = false;
if(a || b) {     // OR lógico
    console.log("Este mensaje se muestra a pesar de 'b' ser false y 'a' true, dado que se ha hecho una operación de OR lógico");
}

if(!b) {        // NOT lógico
    console.log("Este mensaje se muestra dado que hemos hecho una operación de NOT lógico con 'b' siendo este false")
}         

// Operadores de cadena
let myString = "Esto son";
console.log(myString + " dos cadenas de texto");

// Operador condicional (ternario) (condition ? val1: val2)
let age = 19
let statusFromAge = age >= 18 ? "adult" : "minor";
console.log("Mediante un operador ternario, si la edad vale 19 su categoría es: " + statusFromAge);


// Operador coma
x = 2;
let array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
let bidimensionalArray = [x, x, x, x, x]
for (let i = 0, j = 9; i <= j; i++, j--) {                          // Coma
    console.log("array[" + i + "][" + j + "] = " + array[i][j]);
}

// Operadores unarios (operadores con un solo operando)
let myObject = {h : 4}          // Delete
delete myObject.h;

console.log("La variable 'myObject' es de tipo: " + (typeof myObject));    // Typeof

// void expression; -> Operador tipo void (retorna vacío)

// Operadores relacionales
let person = {
    name: "r4kso",
    age: 22
}
console.log("¿Existe la propiedad 'age' en la variable 'person'?: " + ("age" in person)); // In

let colors = ["red", "blue", "green"]
console.log("¿Es la variable colors una instancia de array?: " + (colors instanceof Array));   // Instance Of

// ESTRUCTURAS DE CONTROL:
// If -> Ya la hemos usado anteriormente
// Switch
let day = "Monday";
switch (day) {
  case "Monday":
    console.log("It's Monday!");
    break;

  case "Tuesday":
    console.log("It's Tuesday!");
    break;

  case "Wednesday":
    console.log("It's Wednesday!");
    break;

  case "Thursday":
    console.log("It's Thursday!");
    break;

  case "Friday":
    console.log("It's Friday!");
    break;

  default:
    console.log("It's the weekend!");
    break;
}

// For -> Ya lo hemos usado anteriormento
// While
let contador = 1;
while (contador <= 5) {
  console.log("Iteración número " + contador);
  contador++;
}

// Do while
contador = 1;
do {
  console.log("Iteración número " + contador);
  contador++;
} while (contador <= 5);


// EJERCICIO EXTRA
/* Programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos),
 pares, y que no son ni el 16 ni múltiplos de 3.*/

for(let i = 10; i <= 55; i++) {
    if ((i % 2 == 0) && (i != 16) && (i % 3 != 0)) {
        console.log(i)
    }
}