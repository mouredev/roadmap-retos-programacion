/*
----------
OPERADORES
----------
*/

// Operadores Aritméticos (+,-,*,/,%)
let num1 = 15;
let num2 = 5;

let suma = num1 + num2;
let resta = num1 - num2;
let multiplicacion = num1 * num2;
let division = num1 / num2;
let resto = num1 % num2;
let exponencial = num1 ** num2;

console.log(`Operadores Aritméticos:
  Suma: ${num1} + ${num2} = ${suma}
  Resta: ${num1} - ${num2} = ${resta}
  Multiplicación: ${num1} * ${num2} = ${multiplicacion}
  División: ${num1} / ${num2} = ${division}
  Resto de ${num1} dividido ${num2} es ${resto}
  Exponencial: ${num1} ** ${num2} = ${exponencial}
  `);
// Operadores Lógicos (||, &&, !)
let x = true;
let y = false;
let z = true;

let logico1 = x && y && z;
let logico2 = x || y || z;
let logico3 = ((x || !y) && z) || (!x && z);

console.log(`Operadores Lógicos:
  Ejemplo 1: ${x} AND ${y} AND ${z} = ${logico1}
  Ejemplo 2: ${x} OR ${y} OR ${z} = ${logico2}
  Ejemplo 3: (${x} OR NOT ${y}) AND ${z} OR (NOT ${x} AND ${z}) = ${logico3}
  `);

// Operadores de Comparación (<, <=, >=, >, ==, ===, !=, !==)
let n1 = 16;
let n2 = 8;
let n3 = "16";

let comparacion1 = n1 > n2;
let comparacion2 = n1 < n2;
let comparacion3 = n1 >= n2;
let comparacion4 = n1 <= n2;
let comparacion5 = n1 == n3;
let comparacion6 = n1 != n3;
let comparacion7 = n1 === n3;
let comparacion8 = n1 !== n3;

console.log(`Operadores de comparación:
  ${n1} > ${n2} → ${comparacion1}
  ${n1} < ${n2} → ${comparacion2}
  ${n1} >= ${n2} → ${comparacion3}
  ${n1} <= ${n2} → ${comparacion4}
  ${n1} == "${n3}" → ${comparacion5}
  ${n1} != "${n3}" → ${comparacion6}
  ${n1} === "${n3}" → ${comparacion7}
  ${n1} !== "${n3}" → ${comparacion8}
  `);

// Operadores de Asignación (=, +=, -=, *=, /=, %=, **=)
console.log("Operadores de asignación: ");
let mi_asignacion = 11; // = → asignación
console.log(`  Asignación '=' => ${mi_asignacion}`);

mi_asignacion += 1; // += → suma y asiganción
console.log(`  Suma y Asignación '+=' => ${mi_asignacion}`);

mi_asignacion -= 5; // -= → resta y asignación
console.log(`  Resta y asignación '-=' => ${mi_asignacion}`);

mi_asignacion *= 2; // *= → multiplicación y asignación
console.log(`  Multiplicación y asignación '*=' => ${mi_asignacion}`);

mi_asignacion /= 2; // /= → división y asignación
console.log(`  División y asignación '/=' => ${mi_asignacion}`);

mi_asignacion %= 2; // %= → módulo y asignación
console.log(`  Módulo y asignación '%=' => ${mi_asignacion}`);

mi_asignacion **= 2; // **= → exponente y asignación
console.log(`  Exponente y asignación '**=' => ${mi_asignacion}`);

console.log(" ");

// Operadores bit a bit
let var1 = 10; // 1010
let var2 = 3; // 0011

let opeacionBit1 = var1 & var2; // 0010 - Si ambos son 1
let opeacionBit2 = var1 | var2; // 1011 - Si almenos 1 es 1
let opeacionBit3 = var1 ^ var2; // 1001 -  Si los bits son diferentes 0 si son iguales 1
let opeacionBit4 = ~var1; // 0101 -  Invierte el valor bit a bit
let opeacionBit5 = var1 >> 2; // 1010 → 0101 → 0010
let opeacionBit6 = var1 << 2; // 1010 → 101000

console.log(`Operadores bit a bit
  AND: ${var1} & ${var2} = ${opeacionBit1}
  OR: ${var1} | ${var2} = ${opeacionBit2}
  XOR: ${var1} ^ ${var2} = ${opeacionBit3}
  NOT: ~${var1} = ${opeacionBit4}
  Desplazamiento a la derecha: ${var1} >> 2= ${opeacionBit5}
  Desplazamiento a la izquierda: ${var1} << 2 = ${opeacionBit6}
  `);

/*
----------------------
ESTRUCTURAS DE CONTROL
----------------------
*/

//Estructuras de control: condicionales (if - if/else - if/else if/else), bucles (for - while - do while, switch)

//Condicionales
console.log("Condicionales If - Else If - Else");
const MAYORIA_EDAD = 18;
let edad_persona = 23;

if (edad_persona < 0 || edad_persona > 120) {
  console.log(`Edad inexistene, ingrese un valor correcto`);
} else if (edad_persona < MAYORIA_EDAD) {
  console.log(`Con ${edad_persona} años sos menor de edad`);
} else {
  console.log(`Con ${edad_persona} años sos mayor de edad`);
}

//Switch
console.log(" ");
console.log("Switch");

let opcion = 2;

switch (opcion) {
  case 1:
    console.log("Opción 1");
    break;
  case 2:
    console.log("Opción 2");
    break;
  case 3:
    console.log("Opción 3");
    break;

  default:
    console.log("Debes ingresar una de las 3 opciones");
    break;
}

//Bucle For
console.log(" ");
console.log("Bucle For");
for (let i = 0; i < 10; i++) {
  console.log(`i = ${i}`);
}

//Bucle While
console.log(" ");
console.log("Bucle While");
let j = 10;
while (j > 5) {
  console.log(`j = ${j}`);
  j--;
}

//Bucle Do-while
console.log(" ");
console.log("Bucle Do-While");
let tiene_permiso = false;

do {
  console.log("No tienes permiso");
  //Usando variables anteriormente creadas
  if (edad_persona > MAYORIA_EDAD) {
    tiene_permiso = true;
    console.log("Ahora si tienes permiso");
  }
} while ((tiene_permiso = false));

// DIFICULTAD EXTRA
console.log(" ");
console.log("EJERCICIO EXTRA:");
for (let i = 10; i <= 55; i++) {
  if (i % 2 === 0 && i != 16 && i % 3 !== 0) {
    console.log(i);
  }
}
