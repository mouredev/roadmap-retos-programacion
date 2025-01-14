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

// declaracion de variables 
let a = 1;
let b = 2;
let c = '2';
let d = 3;

// Operadores Arítméticos 
let incremento = a++
let decremento = b--
let suma = a + b;
let resta = b - a;
let multiplicacion = a * b;
let division = d / a;
let resto = d % a;
let potencia = d**b
console.log('----- Operadores Arítméticos -----');
console.log('incremento:', incremento);
console.log('decremento: ', decremento);
console.log('suma: ', suma);
console.log('resta: ', resta);
console.log('multiplicacion: ', multiplicacion);
console.log('division: ', division);
console.log('resto: ', resto);
console.log('potencia: ', potencia);

//Operadores Comparación y Lógicos
console.log('----- Operadores Comparación y Lógicos ------');
let mayorQ = 6 > 4
let menorQ = 6 < 7
let mayorIgualQ = 10 >= 25  
let menorIgualQ = 30 <= 200  
let and = 2 < 3 && 3 > 1;
let or = 2 < 2 || 3 < 7;
let negación = 5 != '5';
let negaciónEstricta = 5 !== '5';
let igualdad = 6 == '6';
let igualdadEstricta = 6 === '6';


console.log('Operadores Lógicos y Comparación: ');
console.log('mayorQ: ', mayorQ);
console.log('menorQ: ', menorQ);
console.log('mayorIgualQ: ', mayorIgualQ);
console.log('menorIgualQ: ', menorIgualQ);
console.log('and: ', and);
console.log('or: ', or);
console.log('negación: ', negación);
console.log('negación Estricta: ', negaciónEstricta);
console.log('negación2: ', !mayorQ);
console.log('igualdad: ', igualdad);
console.log('igualdad estricta: ', igualdadEstricta);


//DIFICULTAD EXTRA
console.log('----- DIFICULTAD EXTRA -----');
for (let i = 10; i <= 55; i++) {

    if (i !== 16 && !(i % 3 == 0) && i % 2 == 0 ) {
    console.log(i);
}
};



