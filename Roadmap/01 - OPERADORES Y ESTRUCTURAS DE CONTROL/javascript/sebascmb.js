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


// ! Ejercicio 1 - aritmeticos

// ---- OPERADORES ARITMETICOS ---- //

let suma           = 5 + 5;               // SUMA
let resta          = 2 - 1;               // RESTA
let multiplicacion = 3 * 2;               // MULTIPLICACION
let division       = 10 / 2;              // DIVISION
let modulo         = 4 % 2;               // MODULO
let exponencia     = 2 ** 3;              // EXPONENCIA

let s = 1
console.log(s );
s++                                       // SUMA 1 AL VALO de s Y RETORNA 1
console.log( s );
s--                                       // RESTA 1 AL VALOR DE s Y RETORNA 1
console.log( s );
++s                                       // SUMA 1 AL VALOR DE s RETORNA EL RESULTADO DE LA OPERACION POSTERIOR
console.log( s );
--s                                       // RESTA 1 A AL VALOR DE s Y RETORNA EL RESULTADO DE LA OPERACION POSTERIOR
console.log( s );

console.log( suma, resta, multiplicacion, division, modulo, exponencia,);


// ------------ OPERADORES LOGICOS ------------ //

let valueFalse = false;
let valueTrue  = true;

//     AND    //

console.log( valueTrue  && valueTrue  );  // DEVUELVE TRUE SI AMBOS VALORES SON VERDADEROS
console.log( valueTrue  && valueFalse );  // DEVUELVE FALSE
console.log( valueFalse && valueTrue  );  // DEVUELVE FALSE
console.log( valueFalse && valueFalse );  // DEVUELVE FALSE


//    OR    //

console.log( valueFalse || valueFalse );  // DEVUELVE FALSE
console.log( valueFalse || valueTrue  );  // DEVUELVE TRUE
console.log( valueTrue  || valueTrue  );  // DEVUELVE TRUE
console.log( valueTrue  || valueFalse );  // DEVUELVE TRUE


 //     NOT    //

 console.log( !valueFalse ); // DEVUELVE TRUE
 console.log( !valueTrue  ); // DEVUELVE FALSE



// ------------ OPERADORES COMPARACION E IDENTIDAD ------------ //

let a = 5;
let b = 10

console.log( a ==  b  ); // ES FALSE - DEVUELVE TRUE SI LOS VALORES FUERAN IGUALES
console.log( a !=  b  ); // ES TRUE  - DEVUELVE TRUE SI LOS VALORES SON DIFRENTENS
console.log( a === b  ); // ES FALSE - DEVUELVE TRUE SI LOS VALORES SON IGUAL Y DEL MISMO TIPO
console.log( a !== b  ); // ES TRUE  - DEVUELVE TRUE SI LOS VALORES SON DIFERENTES Y DEL MISMO TIPO
console.log( a >   b  ); // ES FALSE - DEVUELVE TRUE SI EL VALOR DE A ES MAYOR QUE B
console.log( a >=  b  ); // ES FALSE - DEVUELVE TRUE SI EL VALOR DE A ES MAYOR O IGUAL QUE B
console.log( a <   b  ); // ES TRUE  - DEVUELVE TRUE SI EL VALOR DE A ES MENOR QUE B
console.log( a <=  b  ); // ES TRUE  - DEVUELVE TRUE SI EL VALOR DE A ES MENOR O IGUAL QUE B



// ------------ OPERADORES DE ASIGNACION ------------ //

let x = 2;
let y = 3;

let asignacion1 = x +=  y; // ES IGUAL A X = X +  Y
let asignacion2 = x -=  y; // ES IGUAL A X = X -  Y
let asignacion3 = x *=  y; // ES IGUAL A X = X *  Y
let asignacion4 = x /=  y; // ES IGUAL A X = X /  Y
let asignacion5 = x %=  y; // ES IGUAL A X = X %  Y
let asignacion6 = x **= y; // ES IGUAL A X = X ** Y
let asignacion7 = x &&  y; // ES IGUAL A X = X &  Y
let asignacion8 = x ||  y; // ES IGUAL A X = X || Y


// ------------ OPERADORES DE PERTENENCIA ------------ //

let arr1 = [1,3,5,7,8,9,];

const RESA = 5  in arr1; // DEVUELVE TRUE SI EL VALOR DE 5 ESTA EN EL ARRAY
const RESB = 10 in arr1; // DEVUELVE FALSE SI EL VALOR DE 10 NO ESTA EN EL ARRAY


// ------------ OPERADORES DE BITS ------------ //

let o = 9;
let p = 5;

console.log( o & p );



// ------------ OPERADORES DE TIPO DE DATO ------------ //


let saludo   = 'Hola';
let numero   = 20;
let booleano = true;
let soyUndefined;

console.log( typeof saludo      ); // String
console.log( typeof numero      ); // Number
console.log( typeof booleano    ); // Boolean
console.log( typeof soyUndefined); // Undefined


// ------------ OPERADOR CONCATENACION ------------ //


let nombre    = 'Sebastian';
let apelllido = 'Marquez';

console.log(nombre + ' ' + apelllido);



// ------------ ESTRUCTRUAS DE CONTROL ------------ //


// * IF

let edad = 18;

if ( edad == 25) {
  console.log('Tienes muchas cosas por experimentare aun');
}

// * If - else

if ( edad >= 25) {
  console.log('Puedes entrar a la discoteca');
} else {
  console.log('No puedes entrar a la discoteca');
}

// * iF - else if

if ( edad >= 25 ) {
  console.log('Puedes entrar a la discoteca y fumar');
} else if ( edad <= 18 ) {
  console.log('No puedes entrar en discotecas, mejor ve a hacer ejercio');
} else {
  console.log('Puedes pasar y solo tomar alcohol');
}

// * ternario

let num1 = 2
let num2 = 4

num1 > num2 ? console.log('Soy mayor') : console.log('Soy menor');


// * Switch

let dia = 5;

switch ( dia ) {
  case 0:
    console.log('Domingo');
    break;
  case 1:
    console.log('Lunes');
    break;
  case 2:
    console.log('Martes');
    break;
  case 3:
    console.log('Miercoles');
    break;
  case 4:
    console.log('Jueves');
    break;
  case 5:
    console.log('Viernes');
    break;
  case 6:
    console.log('Sabado');
    break;

  default:
    console.log('Dia no valido');
    break;
}

// * For

for (let i = 0; i <= 5; i++) {
  console.log([i]);
}

// * For in

let heroes = ['Superman', 'Batman', 'Aquaman', 'Spiderman', 'Deadpool',];

for ( let i in heroes ) {
  console.log( heroes[i] );
}

// * For of

for ( let heroe of heroes ) {
  console.log(heroe);
}

// * While

let carros = ['Mazda', 'Hyundai', 'Toyota', 'Cevrolet']
let i = 0;

while ( i < carros.length ) {
  console.log(carros[i]);
  i++
}

let j = 0;

do {
  console.log(carros[j]);
  j++;
} while (carros[j]);


// DIFICULTAD EXTRA (opcional):
//  * Crea un programa que imprima por consola todos los números comprendidos
//  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
//  *
//  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


for (let m = 10; m <= 55; m++) {
  if ( m % 2 === 0 && m !== 16 && m % 3 !==0 ) {
    console.log(m);
  }
}











