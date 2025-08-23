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

// operadores aritmeticos JavaScript
let suma = 5 + 5;
let resta = 5 - 5;  
let multiplicacion = 5 * 5;
let division = 5 / 5;
let modulo = 5 % 5;
let incremento = 5;
incremento++;   
let decremento = 5;
decremento--;
let exponenciacion = 5 ** 2;
let asignacion = 5;
asignacion += 4;
console.log(suma, resta, multiplicacion, division, modulo, incremento, decremento, exponenciacion, asignacion);

// estructuras de control JavaScript

// condicional if: Ejecuta un bloque de código si una condición es verdadera.
const edad = 18;

if (edad>=18) {
  console.log('Eres mayor de edad');
}
// condicional else: Ejecuta un bloque de código si la condicion if es falsa.
const mayorDeEdad = 16;
if (mayorDeEdad>=18) {
  console.log('Puedes conducir');
}
else {
console.log('No puedes conducir');
}
// condicional else if: permite evaluar múltiples condiciones.
if (mayorDeEdad>=18) {
  console.log('Eres mayor de edad');
}
else if (mayorDeEdad>=16) {
  console.log('Eres adolescente');
}
else { 
    console.log('Eres un niño');
}
// switch: Evalúa una expresión, comparando el valor de esa expresión con una instancia case, y ejecuta declaraciones asociadas a ese case.
let canalesDeTv = 2;
switch (canalesDeTv) {
  case 1:
    console.log("canal2");
    break;
  case 2:
    console.log("tvNoticias");
    break;
  default:
    console.log("televisor apagado");
}
//estructura de bucles.
// bucle for: ejecuta un bloque de código un numero determinado de veces.
for (let i = 0; i < 6; i++) {
  console.log(i);
}
// bucle while: ejecuta un bloque de código mientras la condición especificada sea verdadera.
let i = 6;
while (i < 5) {
  console.log(i);
  i++;
}
console.log(i);
// do while: ejecuta un bloque de código al menos uma vez, y luego repite el bucle mientras la condición especificada sea verdadera.
let a = 0;
do {
  console.log(a);
  a++;
} while (a < 5);
//for in: recorre las propiedades de un objeto.
const persona = {nombre: 'Eli', edad: 40};
for(let edad in persona) {
  console.log(edad, persona[edad]);
}
//for of: crea un bucle que itera sobre objetos iterables.
const colores = ['rojo', 'azul', 'verde'];  
for (let color of colores) 
  console.log(color);
//try catch: permite manejar errores.
try {
  console.log('Hola');
  console.log(x);
  console.log('Mundo');
}
catch(err) {
  console.log('Ha ocurrido un error');
}
/*DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números
comprendidos entre 10 y 55 (incluidos), pares,
y que no son ni el 16 ni múltiplos de 3.
Seguro que al revisar detenidamente las posibilidades
has descubierto algo nuevo.*/
for (let i = 10; i <= 55; i++) {
   if (i%2===0 && i != 16 && i%3 !== 0) {
     console.log(i)
        }
}
