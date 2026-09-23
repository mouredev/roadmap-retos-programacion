/* Operadores Aritméticos */

// Adición
let num1: number = 64;
let num2: number = 92;
let res1: number = num1 + num2;
console.log("Sumando 64 mas 92 da:", res1);

// Substracción
let num3: number = 180;
let num4: number = 77;
let res2: number = num3 - num4;
console.log("Restando 180 menos 77 da:", res2);

// División
let num5: number = 240;
let num6: number = 18;
let res3: number = num5 / num6;
console.log(
  "Dividiendo 240 entre 12 da:",
  res3,
  " y su residuo es: ",
  num5 % num6,
);

// Multiplicación
let num7: number = 623;
let num8: number = 0.5;
let res4: number = num7 * num8;
console.log("Multiplicando 623 por 0.5 da:", res4, "\n");

// Exponenciacion
console.log("3 al cubo da:", 3 ** 3, "y 3 al cuadrado da:", 3 ** 2, "\n");

/* Operadores de Comparación */

// Mayor que
if (3 > 2) {
  console.log("El 3 es mayor que el 2");
}
// Menor que
if (15 < 21) {
  console.log("El 15 es menor que el 21");
}
// Mayor que o igual
if (3 >= 3) {
  console.log("El 3 es mayor o igual que el 3");
}
// Menor que o igual
if (15 <= 21) {
  console.log("El 15 es menor o igual que el 21");
}
// Igual que no importando el tipo
console.log("5 == '5' ", (5 as any) == "5"); // Retornará verdadero

// Igual que estricto, tiene que sermismo tipo y valor)
console.log("5 === '5' ->", (5 as any) === "5"); // Retornará falso, tipos distintos
console.log("100 === 100 ->", 100 === 100); // Retornará verdadero porque tiene el ismo tipo y valor

// No es igual estricto
console.log("10 !== '10' ->", (10 as any) !== "10", "\n"); // Retornará verdadero porque son diferentes tipos

/* Operadores Lógicos */
console.log(
  "Operador AND &&: Sin son iguales dan true y si son diferentes da false. ->",
  2 + 1 == 3 && 3 + 2 == 5,
  3 + 5 == 4 && 5 + 5 == 10,
);
console.log(
  "Operador OR ||: Siempre será true si hay un true. ->",
  3 + 2 == 5 || 3 + 3 == 6,
);

console.log(
  "Operador NOT EQUAL !=: Indica true cuando no es igual. ->",
  7 + 9 != 4 + 1,
);

let si = true;
let no = false;
console.log(
  "Operador NOT !: Este invierte el valor booleano. -> si ahora es",
  !si,
  "\n",
);

/* Operadores de Asignación */
let n = 1;
console.log("Numero incial:", n);

n += 8;
console.log(`Asignación de Adición: n += 8. (1 + 8 = ${n})`);

n -= 2;
console.log(`Asignación de Sustracción: n -= 2. (9 - 2 = ${n})`);

n *= 2;
console.log(`Asignación de Multiplicación: n *= 2. (7 x 2 = ${n})`);

n /= 2;
console.log(`Asignación de División: n /= 2. (14 / 2 = ${n})`);

n **= 2;
console.log(`Asignación de Exponenciación: n **= 2. (7 ^ 2 = ${n})`);

n %= 3;
console.log(`Asignación de Residuo: n %= 2. (49 % 3 = ${n})`, "\n");

/* Operadores de identidad*/

let x = 8;
let y = "8";
let z = 5;
let k = z;

console.log((x as any) == y);
console.log((x as any) === y);
console.log(k === z);
console.log("");

/* Operadores de bits */

let a = 5;
let b = 3;

console.log("& Da 1 si ambos bits son 1. Ejemplo A & B 0001 =", a & b);
console.log("| Da 1 si al menos un bit es 1. Ejemplo A | B 0111 =", a | b);
console.log("^ Da 1 si los bits son diferentes. Ejemplo A ^ B 0110 =", a ^ b);
console.log("~ Invierte el valor de los bits. Ejemplo A ~ B =", ~a, ~b);
console.log(">> Desplazamiento a la derecha. 011 >> 001 =", b >> 1);
console.log("<< Desplazamiento a la izquierda. 0101 << 10100 =", a << 2);
console.log("");

// - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
//   que representen todos los tipos de estructuras de control que existan
//   en tu lenguaje:
//   Condicionales, iterativas, excepciones...

/* Estructura de Control: Condicionales */

let value1: number = 45;
let value2: number = 55;

if (value1 + value2 === 100) {
  ("El resultado da 100");
} else {
  ("El resultado NO da 100");
}

/* Estructura de Control: Iterativas */

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let i = 0;

for (i = 1; arr.length + 1 > i; i++) {
  console.log(i);
}

// Lo mismo pero con in WHILE LOOP //
let j = 0;

// FOREACH para iterar entre arrays //
let arrayName = ["Kevin", "Jose", "Daniel", "María", "Perla"];

arrayName.forEach((name, index) => {
  console.log(`Paciente número: ${index + 1}: ${name}`);
});

console.log("");

/* Estructura de Control: Excepciones */

try {
  const edad: number = 12;

  if (edad <= 21) {
    throw new Error("No puedes beber alcohol. Eres menor de edad");
  }

  console.log("Puedes entrar al bar y beber");
} catch (error: any) {
  console.log("Hay un problema");
  console.log(error.message);
}

console.log("");

/* Estructura de Control: Saltos */

for (let i = 1; i < 15; i++) {
  if (i === 1) continue;
  if (i === 3) continue;
  if (i === 5) continue;
  if (i === 7) continue;
  if (i === 9) continue;
  if (i === 11) break;
  console.log(i);
}

console.log(`Estos son los números pares antes del: ${i}`);

/* Estructura de Control: Variantes de Bucles */

const lista: string[] = ["a", "b", "c"];

// Obtiene los valores directamente
for (const valor of lista) {
  console.log(valor); // "a", "b", "c"
}

// Obtiene los índices o propiedades
for (const indice in lista) {
  console.log(indice); // "0", "1", "2"
}

/* Estructura de Control: Type Guards */

function procesar(dato: string | number) {
  if (typeof dato === "string") {
    // Aquí TypeScript sabe con certeza que 'dato' es string
    console.log(dato.toUpperCase());
  } else {
    // Aquí TypeScript sabe que es un number
    console.log(dato.toFixed(2));
  }
}

console.log("");

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

let index: number = 0;

for (index = 10; index < 55; index++) {
  if (index % 2 || index === 16 || index % 3 === 0) {
    continue;
  }

  console.log(index);
}

console.log(index);
