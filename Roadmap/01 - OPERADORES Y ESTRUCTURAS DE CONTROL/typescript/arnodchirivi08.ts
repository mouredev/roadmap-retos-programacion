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

// Operadores de asignación
let a: number = 22; // Operador de asignación (=)
let b: number = 5;
let c: number = 8;
let d: number = 8;
let trutty: boolean = true;
let falsy: boolean = false;

c += a; // Operador de asignación compuesto suma (+=)
c -= a // Operador de asignación compuesto resta (-=)
c *= a // Operador de asignación compuesto multiplicación (*=)
c /= a // Operador de asignación compuesto división (/=)
c %= a // Operador de asignación compuesto módulo (%=)

// operadores de asignación compuestos bit a bit
c **=a // Operador de asignación compuesto exponenciación (**=)
c <<=a // Operador de asignación compuesto corrimiento a la izquierda (<<=)
c >>=a // Operador de asignación compuesto corrimiento a la derecha (>>=)
c &=a // Operador de asignación compuesto AND a nivel de bits (&=)
c ^=a // Operador de asignación compuesto XOR a nivel de bits (^=)
c |=a // Operador de asignación compuesto OR a nivel de bits (|=)

// Operadores de asignación logicos
trutty &&= falsy// Operador de asignación AND lógico (&&=)

let f: string = "";
let g: string = "pepo";
f ||=g // Operador de asignación OR lógico (||=)

//Asignación de anulación lógica (??=)
let elementNull : null | {} =  null
let elementUndefined : undefined | {} = undefined
let element= { name: "PEDRO" };

elementNull ??= element;
elementUndefined ??= element

console.log(elementNull);
console.log(elementUndefined);



// Destructuración de arrays
var foo = ["one", "two", "three"];
var [one, two] = foo;
console.log(one);


// Operadores de comparacion
const numerosIguales= c == d;
const numerosDiferentes = c !=a
const numerosEstrictamenteIguales = c===d;
const numerosEstrictamenteDiferentes = c!==d;
const numeroMayorQue = a > b;
const numeroMayorIgualQue = c >= d;
const numeroMenorQue = a < b;
const numeroMenorIgualQue = a < b;

console.log(numerosIguales);
console.log(numerosDiferentes);
console.log(numerosEstrictamenteIguales);
console.log(numerosEstrictamenteDiferentes);
console.log(numeroMayorQue);
console.log(numeroMayorIgualQue);
console.log(numeroMenorQue);
console.log(numeroMayorIgualQue);


// Operadores aritméticos
const residuo = a%b;
const preIncremento = ++a;
const postIncremento = a++
const preDecremento = --b;
const postDecremento = b--;
const negacionUnaria = -c;
const exponenciacion = a**b;

console.log(residuo);
console.log(preIncremento);
console.log(postIncremento);

// operadores logicos;
var a1 = true && true; // t && t devuelve true
var a2 = true && false; // t && f devuelve false
var a3 = false && true; // f && t devuelve false
var a6 = false && "Cat"; // f && t devuelve false

var o1 = true || true; // t || t devuelve true
var o2 = false || true; // f || t devuelve true
var o3 = true || false; // t || f devuelve true
var o6 = false || "Cat"; // f || t devuelve Cat


var n1 = !true; // !t devuelve false
var n2 = !false; // !f devuelve true

// Operadores de cadena
console.log("es " + "typescript"); // la consola registra la cadena "mi cadena".
var mystring = "alpha";
mystring += "bet"; // se evalúa como "alphabet" y asigna este valor a mystring.

// Operado condicional (ternario)
const age: number = 20;
var estado = age >= 18 ? "adult" : "minor";
console.log(estado); // "adult"


// operadores unarios

var myFun = new Function("5 + 2");
var shape = "round";
var size = 1;
var foo = ["Apple", "Mango", "Orange"];
var today = new Date();

console.log(typeof myFun); // devuelve "function"
console.log(typeof shape); // devuelve "string"
console.log(typeof size); // devuelve "number"
console.log(typeof foo); // devuelve "object"
console.log(typeof today); // devuelve "object"

// Operadores relacionales

//Operador in
// Arreglos
var trees = ['redwood', 'bay', 'cedar', 'oak', 'maple'];
console.log(0 in trees);        // devuelve true
console.log(3 in trees);        // devuelve true
console.log(6 in trees);        // devuelve false



// objetos integrados
'PI' in Math;          // devuelve true
var myString = new String('coral');
'length' in myString;  // devuelve true

// Objetos personalizados
var mycar = { make: 'Honda', model: 'Accord', year: 1998 };
console.log('make' in mycar);  // devuelve true
console.log('model' in mycar); // devuelve true

//instanceof
var theDay = new Date(1995, 12, 17);
if (theDay instanceof Date) {
  console.log('es fecha');
}



//////// Estructuras de control
// Estructura condicional if...else
let number: number = 10;
if (number > 0) {
  console.log("El número es positivo");
} else if (number < 0) {
  console.log("El número es negativo");
}


// Estructura condicional switch
let fruit:string = "Mangos";
switch(fruit){
  case "Naranjas":
    console.log("El kilogramo de naranjas cuesta $0.59.");
    break;
  case "Mangos":
  case "Mandarinas":
    console.log(`El kilogramo de ${fruit} cuesta $0.48.`);
    break;
  default:
    console.log("Lo lamentamos, por el momento no disponemos de " + fruit + ".");
}

// Estructura iterativa for
for(let i: number = 0; i < 5; i++){
  console.log(`Iteración número ${i}`);
}


// Estructura iterativa while
let n= 0;
let x= 0;

while(n < 3){
  n++;
  x +=n;
  console.log(n);
  console.log(x)
}

// Estructura iterativa do...while
let result = "";
let i = 0;

do {
  i = i +1;
  result = result + i;
} while(i < 5)

console.log(result);

// Estructura iterativa for...of
const array1 = ["a", "z", "b", "y", "c"];

for (const element of array1){
 console.log(element)
}

const iterable = "typescript";
for(const value of iterable){
  console.log(value)
}

const iterableDos = new Map([
  ["a", 1],
  ["b", 2],
  ["c", 3],
]);

for (const entry of iterableDos) {
  console.log(entry);
}

for (const [key, value] of iterableDos) {
  console.log(value);
}

// Estructura iterativa for...in
let persona = {
    nombre: "carla",
    edad: 30
}

for(const propiedad in persona){
    console.log(`${propiedad}: ${persona[propiedad]}`)
}

// Estructura de control de excepciones try...catch
function analizarUsuario(jsonString: string) {
  try {
    console.log("Intentando analizar el JSON...");
    const usuario = JSON.parse(jsonString); // Esto puede lanzar un error.
    
    console.log("¡Análisis exitoso! ✅");
    console.log("Nombre:", usuario.nombre);
    console.log("Edad:", usuario.edad);

  } catch (error) {
    // 2. Si JSON.parse falla, el código salta directamente aquí.
    console.error("🔴 ¡Ocurrió un error al analizar el JSON!");
    // 'error' es un objeto que contiene los detalles del fallo.
    // 'error.message' suele tener el mensaje más útil.
    console.error("Detalle del error:", error.message);

  } finally {
    // 3. Este bloque se ejecuta siempre, con o sin error.
    console.log("--- Proceso de análisis finalizado ---");
  }
}


console.log("Probando con un JSON válido:");
const jsonValido = '{"nombre": "Ana", "edad": 30}';
analizarUsuario(jsonValido);


console.log("\n=============================\n");

console.log("Probando con un JSON inválido:");
const jsonInvalido = '{"nombre": "Luis", "edad":}'; // Falta el valor de la edad
analizarUsuario(jsonInvalido);


// DIFICULTAD EXTRA (opcional):
for(let i: number= 10; i< 57; i++)
{
  if(i%2 ==0 && i%3 !==0 && i !==16){
      console.log(i)
  }
}