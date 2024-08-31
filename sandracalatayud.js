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


/* 
    PUNTO 1
    Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/

//          TIPOS DE OPERADORES 

//------- OPERADORES DE ASIGNACIÓN -------

let a = 1;

console.log( a = 2 );
console.log( a += 2 );
console.log( a -= 2 );
console.log( a *= 2 );
console.log( a /= 2 );
console.log( a %= 4 );
console.log( a **= 2 );

//------- OPERADORES DE COMPARACIÓN -------

let b = 1;
let c = 4;

console.log( b == c );
console.log( b != c );
console.log( b === c );
console.log( b !== c );
console.log( b > c );
console.log( b < c );
console.log( b >= c );
console.log( b <= c );

//------- OPERADORES ARITMÉTICOS -------

let d = 5;

console.log( d % 3 );
console.log( d + 3 );
console.log( d - 3 );
console.log( d++ );
console.log( d-- );
console.log( ++d );
console.log( --d );
console.log( d ** 3 );

//------- OPERADORES LOGICOS -------

let e = 5;
let f = 3;

console.log( e && f);
console.log( e || f);
console.log( e ?? f);
console.log( !e );

//------- OPERADORES DE STRING -------

let string  = "cama";
string += "stro";
console.log(string)

console.log("Podemos unir texto con un +" + " y eso hará que salga junto");

//------- OPERADORES CONDICIONAL -------

let adulto = 18;
let edad = 1;

console.log( edad < adulto ? "Es un niño" : "Es un adulto");

//------- OPERADOR COMA -------

//Puede ser útil para usarlo en el bucle "for" de la siguiente forma:

for (let i = 0, j = 9; i <= j; i++, j--) {
    
  }

//------- OPERADORES UNARIOS -------

//  DELETE

//Permite eliminar variables (si no están declaradas como "var" y propiedades de objetos).

const objeto = {
  name: "Sandra"
}

console.log(objeto.name);

delete objeto.name;

console.log(objeto.name);

//  TYPEOF

//Permite saber el tipo de dato

let type_string = "Esto es un string";
let type_number = 5;
let type_boolean = true;

console.log( typeof(type_string) );
console.log( typeof(type_number) );
console.log( typeof(type_boolean) );

//------- OPERADORES DE RELACIÓN -------

//  IN  

//Sirve para saber si es una propiedad de un objeto. Se puede aplicar tanto a objetos como arrays

const colores = ["azul", "blanco", "amarillo"];
const persona = {
  nombre:"Sandra"
}

console.log(1 in colores);           //Para arrays
console.log(7 in colores);           //Para arrays
console.log("length" in colores);    //
console.log("nombre" in persona);    //Para objetos

//   INSTANCE OF

//Sirve para saber si es un tipo de dato concreto

let numero = new Number(4);

console.log(numero instanceof Number);

/*
  PUNTO 2
    - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
*/
let animales = ["perro", "gato", "cuervo", "serpiente", "delfin"];
let perro = "perro"

//------- IF ELSE -------

if ( animales.length <= 6 ){
  console.log("Hay menos de 6 animales en el array")
} else if (animales.length >=6){
  console.log("Hay más de 6 animales en el array")
}else {
  console.log("Hay más de 6 animales en el array")
}

//------- SWITCH -------

switch (perro){
  case "perro": 
    console.log("Es un perro");
    break;
  case "gato": 
    console.log("No es un perro");
    break;
  default:
    console.log("No está definido o es otro animal")
}

//------- FOR -------

for (let i = 0; i < animales.length; i++) {
  console.log("\n" +animales[i])  
};

//------- FOR IN -------

for (let i in animales){
  console.log(animales[i]);
  console.log(i);
}

//------- FOR OF -------

for (let i of animales){
  console.log(i);
}


//------- DO WHILE -------

let num1 = 0;

do {
  console.log(animales[num1]); 
  num1++
}
while (num1 < animales.length);

//------- WHILE -------

num1 = 0; 

while (num1 < animales.length){
  console.log(animales[num1]); 
  num1++;
}

//------- CONTROL DE EXCEPCIONES -------

perro = "gato";

//    THROW

if (perro !== "perro"){
  //  throw "Esto es un error";    //Comentado para que no bloquee la ejecución
}

//    TRY CATCH

try {
  if (perro !== "perro"){
    throw "Esto es un error";
  }
} catch (err){
  console.log(perro);
  console.log(err);
} finally{
  perro = "perro";
}

/*
  PUNTO 3
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for (let i = 10; i <= 55; i++) {
  if( i % 2 == 0 && i != 16 && i % 3 != 0 ){
    console.log(i);
  }
}

