/*   - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
   Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
   Debes hacer print por consola del resultado de todos los ejemplos.
 
  DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo. */

// aritmeticos

let x = 5;
let y = 3;

console.log(x + y); //suma
console.log(x - y); //resta
console.log(x / y); //division
console.log(x * y); //multiplicacion
console.log(x % y); //modulo

// asignacion

let a = 10;
a += 5; //equivale a: a = a = + 5
console.log(a);

//comparacion

let b = 20;
let c = 10;

console.log(b == c); // igualdad
console.log(b === c); // igualdad estricta
console.log(b != c); // desigualdad
console.log(b !== c); // desigualdad estricta
console.log(b > c); // mayor
console.log(b < c); // menor
console.log(b >= c); // mayor igual
console.log(b <= c); // menor igual

//logicos

let frio = true;
let calor = true;

console.log(frio && calor);
console.log(frio || calor);
console.log(! calor);

//incremento y decremento 

let contador = 5;

contador++; //incrementar en 1
console.log(contador);

//concatenacion

let nombre = "Edgar";
let apellido = "Medrano";

console.log(nombre + " " + apellido);

// ternario

let edad = 38;
let permitido = (edad >= 18) ? "si" : "no";

console.log("esta permitido? " + permitido);

//tipo de dato

let variable = 20;

console.log(typeof variable); //tipo int

variable = "Hola mundo";

console.log(typeof variable); //tipo string

/*   DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3. */

for (let i = 10; i <= 55; i++) {
    if(numero !== 16 && numero % 2 === 0 && numero % 3 !== 0) {
        console.log(i);
    }
}
