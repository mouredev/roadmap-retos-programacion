/*Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: 
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
(Ten en cuenta que cada lenguaje puede poseer unos diferentes)

JavaScript : Operadores - https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_operators
*/

// Operadores ariméticos 
let suma = 2001+24;
console.log(`Suma: 2001 + 24 =${suma}`) // `${}` interpolacion en cadena de texto, logra incorporar codigo en medio de cadenas de texto
let resta = 2025-2001;
let multiplicacion = suma * resta; 
let division = multiplicacion / suma;
let exponenciacion= 10**2;
let modulo = multiplicacion % suma;
suma++; //incremento
suma--; //decremento 

//Operadores de asignación 
let numeroRandom = 123;
//operadores de asignacion arimetico
numeroRandom += 2; 
numeroRandom -=4;
numeroRandom *= 5;
numeroRandom /=3;
numeroRandom %=1;
numeroRandom **= 3;
//operadores de asignacion logicos 

//operadores de asignacion bit a bit 
// trabaja con los valores pasados en bit o con bit   
let a = 10  // 1010 valor del 10 en bit
let b = 3 //0010 valor del 3 en bit 

`AND : 10 & 3 = ${ 10 & 3 }` //output 0010
`OR : 10 | 3 = ${ 10 |  3 } ` // output 1011
`XOR : 10 ^ 3 = ${ 10 ^3} ` //output 1001
`NOT : ~10 = ${ ~10 }`

let nullish = "dato ??= dato"

//Operadores de comparacion 
let mayorQue = 2 > 1;
let menorQue = 1 < 2;
let mayorIgual = 2 >= 2;
let menorIgual = 3 <= 3;
let diferente = "4" != 4;
let igualdad = 1 == "1";
let estrictamenteIgual = 1 === 1;
let estrictamenteDesigual = "hola" !== true;

//operadores lógicos
let conjuncion = true && true; // and 
let disyuncion = true || false ; // or
let negacion = !true; 

//operadores bit a bit 
//AND a nivel de bits (&),
//OR a nivel de bits (|), 
//XOR a nivel de bits (^), 
//NOT a nivel de bits (~), 
//desplazamiento a la izquierda (<<), 
//desplazamiento a la derecha de propagación de signo (>>) 
//desplazamiento a la derecha de relleno cero (>>>)
 
//Operador terneario (condicional)
//condition ? val1 : val2


/* 
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que exista en tu lenguaje:
Condicionales, iterativas, excepciones...
Debes hacer print por consola del resultado de todos los ejemplos.
*/
//estrucutras de iteracion 
//https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Loops_and_iteration

/*for (let index = 0; index < array.length; index++) {
    const element = array[index];
    
}

array.forEach(element => {
    for await (const element of object) {
        
    }
});

for (const key in object) {
}

for (const element of object) {  
}
*/

//estructuas condicionales 
/*
if (condition) {
}

if (condition) {
    
} else {
    
}

switch case : 
let day = 3;
let dayName;
switch (day) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    case 3:
        dayName = "Wednesday";
        break;
    case 4:
        dayName = "Thursday";
        break;
    case 5:
        dayName = "Friday";
        break;
    case 6:
        dayName = "Saturday";
        break;
    case 7:
        dayName = "Sunday";
        break;
    default:
        dayName = "Invalid day";
}
*/

/* 
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

let contador  = 10; // inicio del contador en 10

for (contador; contador < 56; contador++) {

    let restoDivDos = contador % 2; // Resto de la division para conocer cual es par

    let restoDivTres = contador % 3; // Resto de la division para conocer cual es multiplo de tres

 //Condicional: resto es cero es par, si el resto es diferente a cero no es multiplo de tres y que no sea el 16
    if(restoDivDos == 0 && restoDivTres != 0 && contador != 16){
        console.log(contador)
    }
}

