// # #01 OPERADORES Y ESTRUCTURAS DE CONTROL
// > #### Dificultad: Fácil | Publicación: 02/01/24 | Corrección: 08/01/24

// ## Ejercicio

```
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
```;
/* #### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**. */

/* OPERADORES ARITMETICOS. */
let resultado = 5 + 3;
let diferencia = 13 - 7;
let producto = 9 * 9;
let cociente = 27 / 7;
let residuo = 9 % 3;
let aumento = 1;
aumento++;
let decremento = 20;
decremento--;
let potencia = 2 ** 3;

/* ESTRUCTURAS DE CONTROL */

// Sentencia if:
if (edad >= 18) {
  console.log("Eres mayor de edad");
}

// Sentencia else
if (edad >= 18) {
  console.log("Eres mayor de edad");
} else {
  console.log("Eres menor de edad");
}

// Sentencia else if
if (edad >= 18) {
  console.log("Eres mayor de edad");
} else if (edad >= 13) {
  console.log("Eres adolecente");
} else {
  console.log("Eres un niño");
}

// Bucle for
for (let i = 0; i < 5; i++) {
  console.log("Number: ", i);
}

// Bucle while
let numero = 10;
while (numero > 0) {
  console.log(numero);
  numero--;
}

// Sentencia break
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}

// Sentencia continue
for (let i = 0; i < 10; i++) {
  if (i % 2 === 0) {
    continue;
  }
  console.log(i);
}

// Sentencia switch
let dia = "Lunes";
switch (dia) {
  case "Lunes":
    console.log("Hoy es Lunes");
    break;

  case "Martes":
    console.log("Hoy es Martes");
    break;

  case "Miercoles":
    console.log("Hoy es Miercoles");
    break;

  default:
    console.log("No conozco ese dia");
}

// Sentencia do...while
let num = 0;
do {
  console.log(num);
  num++;
} while (num < 10);

// Sentenci for...in
let persona = { nombre: "Juan", edad: 30 };
for (let propiedad in persona) {
  console.log(propiedad + ": " + persona[propiedad]);
}

// for...of
let num2 = [1, 2, 3, 4, 5];
for (let num2 of num2) {
  console.log(num2);
}
