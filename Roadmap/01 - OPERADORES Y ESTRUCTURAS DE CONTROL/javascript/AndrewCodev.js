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

//Operadores aritmeticos
let a = 10;
let b = 3;

console.log(a + b); // 13  (suma)
console.log(a - b); // 7   (resta)
console.log(a * b); // 30  (multiplicación)
console.log(a / b); // 3.333... (división)
console.log(a % b); // 1   (módulo o residuo)
console.log(a ** b); // 1000 (exponente: 10^3)

// Operadores de asignación
let x = 5;
x += 2; // x = x + 2
x -= 1; // x = x - 1
x *= 3; // x = x * 3
x /= 2;
x %= 3;
x **= 2;

//Operadores de comparación
console.log(5 == "5"); // true (igualdad débil)
console.log(5 === "5"); // false (igualdad estricta)
console.log(5 != "5"); // false
console.log(5 !== "5"); // true
console.log(3 < 5); // true
console.log(3 <= 3); // true
console.log(6 > 4); // true
console.log(6 >= 7); // false

//Operadores lógicos
let p = true;
let q = false;

console.log(p && q); // false (AND)
console.log(p || q); // true (OR)
console.log(!p); // false (NOT)

//Operadores de identidad
let obj1 = { nombre: "Ana" };
let obj2 = { nombre: "Ana" };
let obj3 = obj1;

console.log(obj1 === obj2); // false (contenido igual, pero diferentes referencias)
console.log(obj1 === obj3); // true  (misma referencia en memoria)

//Operadores de pertenencia
let persona = { nombre: "Luis", edad: 30 };

console.log("nombre" in persona); // true
console.log(persona.hasOwnProperty("edad")); // true

//Operadores Bits
let m = 5; // 0101
let n = 3; // 0011

console.log(m & n); // 1 (AND)
console.log(m | n); // 7 (OR)
console.log(m ^ n); // 6 (XOR)
console.log(~m); // -6 (NOT)
console.log(m << 1); // 10 (desplazamiento a la izquierda)
console.log(m >> 1); // 2  (desplazamiento a la derecha)

//Estructuras de control

//Condicionales
//if - else if -else
let edad = 20;

if (edad < 18) {
  console.log("Menor de edad");
} else if (edad < 65) {
  console.log("Adulto");
} else {
  console.log("Adulto mayor");
}

//switch
let dia = "lunes";

switch (dia) {
  case "lunes":
    console.log("Inicio de semana");
    break;
  case "viernes":
    console.log("¡Por fin viernes!");
    break;
  default:
    console.log("Día normal");
}

//Bucles
//for
for (let i = 0; i < 5; i++) {
  console.log("Iteración:", i);
}

//while
let i = 0;
while (i < 3) {
  console.log("i:", i);
  i++;
}

//do while
let j = 0;
do {
  console.log("j:", j);
  j++;
} while (j < 2);

//Bucles para arrays
//for of
const FRUTAS = ["manzana", "pera", "uva"];
for (const fruta of FRUTAS) {
  console.log(fruta);
}

//for in
const PERSONA = { nombre: "Ana", edad: 25 };
for (const clave in PERSONA) {
  console.log(clave, ":", PERSONA[clave]);
}

//Operador ternario
let miEdad = 17;
let mensaje = miEdad >= 18 ? "Adulto" : "Menor";
console.log(mensaje);

//Manejo de excepciones
//try catch
try {
  let resultado = 10 / 0;
  console.log("Resultado:", resultado);
} catch (error) {
  console.log("Ocurrió un error:", error.message);
}

//try catch finally
try {
  // código que puede fallar
} catch (e) {
  console.log("Error capturado");
} finally {
  console.log("Esto se ejecuta siempre");
}

//Dificultad extra Ejercicio
const miFuncion = () => {
  for (let i = 10; i <= 55; i++) {
    const esPar = i % 2 === 0;
    const noEs16 = i !== 16;
    const noEsMultiploDe3 = i % 3 !== 0;

    if (esPar && noEs16 && noEsMultiploDe3) {
      console.log(i);
    }
  }
};

miFuncion();
