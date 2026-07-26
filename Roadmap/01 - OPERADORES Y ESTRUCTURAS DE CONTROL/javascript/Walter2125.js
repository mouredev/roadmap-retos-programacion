// #01 - JavaScript
 /* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes) */
 console.log("-----Operadores de asignación-----");
 let num = 20;

 console.log(`El numero inicial es: ${num}`);
 console.log(`Asignacion: ${num = 23}`); // 23
 console.log(`Asignacion de suma: ${num = num + 5}`); //tambien puede ser num += 5
 console.log(`Asignacion de resta: ${num -= 10}`);// num = num - 10.
 console.log(`Asignacion de multiplicación: ${num *= 5}`);// num = num * 5.
 console.log(`Asignacion de división: ${num /= 4}`); //num = num / 4.            
 console.log(`Asignación de residuo: ${num %= 4}`);//num = num % 4.
 console.log(`Asignación de exponenciación: ${num **= 2}`);//num = num ** 2. 
 console.log(`Asignación de desplazamiento a la izquierda: ${num <<= 4}`);// num = num << 4
 console.log(`Asignación de desplazamiento a la derecha: ${num >>= 4}`);// num = num >> 4
 console.log(`Asignación de desplazamiento sin signo: ${num >>>= 3}`);// num = num >>> 3
 console.log(`Asignación AND bit a bit: ${num &= 9}`);// num = num & 9
 console.log(`Asignación XOR bit a bit: ${num ^= 2}`);// num = num ^ 2
 console.log(`Asignación OR bit a bit: ${num | 40}`);//num = num | 40
 console.log(`Asignación AND logico ${num &&= 78}`);//num = num && 78 
 console.log(`Asignación OR logico ${num ||= 30}`);//num = num || 30  
 console.log(`Asignación de anulación lógica ${num ??= 50}`);//num = num ?? 50  
 console.log('');

/*
 -----Operadores de asignación-----
El numero inicial es: 2 Asignacion: 23
Asignacion de suma: 28
Asignacion de resta: 18
Asignacion de multiplicación: 90
Asignacion de división: 22.5
Asignación de residuo: 2.5
Asignación de exponenciación: 6.25
Asignación de desplazamiento a la izquierda: 96
Asignación de desplazamiento a la derecha: 6
Asignación de desplazamiento sin signo: 0
Asignación AND bit a bit: 0
Asignación XOR bit a bit: 2
Asignación OR bit a bit: 42
Asignación AND logico 78
Asignación OR logico 78
Asignación de anulación lógica 78
*/


 console.log('-----Operadores de Comparación-----');
let var1 = 12;
let var2 = 10;
 
 console.log(`Operador Igual: ${var1 == var2}`); 
 console.log(`No es igual: ${var1 != var2}`);
 console.log(`Estrictamente igual: ${var1 === 12}`);
 console.log(`Desigualdad estricta: ${var1 !== '12'}`);
 console.log(`Mayor que: ${var2 > 9}`);
 console.log(`Mayor o igual que: ${var2 >= 15}`);
 console.log(`Menor que: ${var2 < var1}`);
 console.log(`Menor o igual que: ${var2 <= 5}`);

/*
-----Operadores de Comparación-----
Operador Igual: false
No es igual: true
Estrictamente igual: true
Desigualdad estricta: true
Mayor que: true
Mayor o igual que: false
Menor que: true
Menor o igual que: false
*/

console.log('-----Operadores Aritméticos-----');
let n = 8;
let b = 8;
let x = -2
 console.log(`Suma: ${n + 2}`);
 console.log(`Resta: ${n - 3}`);
 console.log(`Multiplicacion: ${n * 2}`);//16
 console.log(`Division: ${n / 4}`);//2
 console.log(`Residuo: ${12 % 5}`);// devuelve 2
 console.log(`Incremento: n=${++n}, b=${b++}`);
 console.log(`Decremento: ${--n}`);
 console.log(`Negación unaria: n=${-n}, x=${-x}`);//devuelve la negacion de su operando
 console.log(`Positivo unario: ${+"3"}, ${+true}, ${+-3}`);//Intenta convertir el operando en un número, si aún no lo es.
 console.log(`Operador de exponenciación: ${2 ** 3}`);//devuelve un 8

/*
-----Operadores Aritméticos-----
Suma: 10
Resta: 5
Multiplicacion: 16
Division: 2
Residuo: 2
Incremento: n=9, b=8
Decremento: 8
Negación unaria: n=-8, x=2
Positivo unario: 3, 1, -3
Operador de exponenciación: 8
*/

console.log(`-----operadores bit a bit-----`);

x = 10;
y = 23;

console.log(`valores iniciales ${x} y ${y}\n`);
console.log(`Desplazamiento a la izquierda:\n x << y = ${x << y}`);
console.log(`Desplazamiento a la derecha:\n x >> y = ${x >> y}\n`);
console.log(`Desplazamiento a derecha de relleno cero ${19>>>2}`);

console.log('-----Operadores logicos-----');
console.log('Operador && (AND lógico)');
var a1 = true && true; // t && t devuelve true
var a2 = true && false; // t && f devuelve false
var a3 = false && true; // f && t devuelve false
var a4 = false && 3 == 4; // f && f devuelve false
var a5 = "Cat" && "Dog"; // t && t devuelve Dog
var a6 = false && "Cat"; // f && t devuelve false
var a7 = "Cat" && false; // t && f devuelve false

console.log('Operador || (OR lógico)');
var o1 = true || true; // t || t devuelve true
var o2 = false || true; // f || t devuelve true
var o3 = true || false; // t || f devuelve true
var o4 = false || 3 == 4; // f || f devuelve false
var o5 = "Cat" || "Dog"; // t || t devuelve Cat
var o6 = false || "Cat"; // f || t devuelve Cat
var o7 = "Cat" || false; // t || f devuelve Cat

console.log('Operador ! (NOT lógico)');
var not1 = !true; // t devuelve false
var not2 = !false; // f devuelve true
var not3 = !"Cat"; // t devuelve false


console.log('-----Operadores de Cadena-----');
let primerNombre = 'walter';
let segundoNombre = 'andres';

console.log('Mi nombre es:'+''+ primerNombre + '' + segundoNombre);

console.log('-----Operador Condicional (ternario)-----');
let val = 3;
let val1 = 5;

const resultado = (val1 > val) ? val1 : val
console.log(`${resultado}\n`);

console.log('-----Operador Coma-----');
var z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
var w = [x, x, x, x, x];

console.log(`${z}\n`);
console.log(`${x}\n`);

console.log('-----Operador IN-----');
const usuario = {
    id: 1,
    nombre: 'Juan',
    rol: 'admin'
};

console.log('nombre' in usuario); // true
console.log('edad' in usuario);   // false

/*
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje: Condicionales, iterativas, excepciones...
*/


console.log('---Declaraciones if ... else---');
let mayor = 20;
let menor = 10;
if (mayor > menor) {
  console.log(`el numero: ${mayor} es mayor que ${menor}`);
} else {
  console.log(`el numero: ${menor} es menor que ${mayor}`);
}

console.log('---Declaraciones if ... else if---');
let n1 = 20;
let n2 = 10;

if (n1 > n2) {
  console.log(`El número ${n1} es mayor que ${n2}`);
} else if (n2 > n1) {
  console.log(`El número ${n2} es mayor que ${n1}`);
} else {
  console.log("Ambos números son iguales");
}


console.log('---Declaraciones con switch---');
let id = 3;
switch (id) {
  case 3:
    console.log('el id es 3');
    break;

  case 2:
    console.log('El id es 2');
    break;

   case 1:
    console.log('El id es 1');
    break;

   default:
      console.log('Numero no reconocido.');
}

console.log('---Ternario---');
let greeting = isBirthday
  ? "Feliz cumpleaños Sra. Smith. ¡Esperamos que tenga un gran día!"
  : "Buenos días señora Smith.";

//loops
console.log('---Bucle estándar for---');
for (let i = 0; i < 10; i++) {
  console.log("Hola a todosss (loop for)");
}

console.log('---while y do...while---');
//while
let e = 1;
while(e < 10) {
  console.log("Hola a todosss en un bucle while");

  e++;
};

//do while
let a = 5;
do {
  console.log("Hola a todosss (bucle do while)");

  --e;
} while (e > 0)


console.log('---Estructuras de control: Excepciones---');
try {
    let resultado = 10 / 0;
    if (resultado === Infinity) {
        throw new Error("No se puede dividir por cero en este contexto.");
    }
} catch (error) {
    console.log(`Error capturado: ${error.message}`);
} finally {
    console.log("Este bloque siempre se ejecuta, haya error o no.");
}


console.log('---Iteraciones adicionales---');
const frutas = ["manzana", "pera", "uva"];
const persona = { nombre: "Juan", edad: 30 };

// for...of (para iterables como arreglos)
console.log("Bucle for...of:");
for (const fruta of frutas) {
    console.log(fruta);
}

// for...in (para propiedades de objetos)
console.log("Bucle for...in:");
for (const clave in persona) {
    console.log(`${clave}: ${persona[clave]}`);
}

/*
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for (let f = 10; f <= 55; f++) {
   if (f % 2 === 0 && f !== 16 && f % 3 !== 0) {
      console.log(f);
   };
};