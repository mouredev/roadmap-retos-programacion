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


// OPERADORES ARITMETICOS
let a, b, c;

a = 5;
b = 3;
c = 2;

let suma = a + b;

let resta = b - c;

let multiplicacion = a * b *c;

let division = b / c;

let modulo = b % c;


console.log( `\nSuma de a + b = ${suma}\nResta de b - c = ${resta}\nMulplicación de a * b * c = ${multiplicacion}\n...etc.\n`, )


// OPERADORES DE INCREMENTO Y DECREMENTO
console.log(a,`\n`);

++a;
console.log(a,` incrementa de 1\n`);

--a;
console.log(a,` decrementa de 1\n`);

// * Recuerda que que el navegador devuelve el valor actual y luego incrementa la variable. 
// * Puedes ver que se ha incrementado si devuelves el valor variable nuevamente
a++;
console.log(a,` incrementa de 1\n`);

a--;
console.log(a,` decrementa de 1\n`);


// OPERADORES DE ASIGNACION

a = 1; // Asigna o reasigna un valor

// --> toma el valor de la variable y ejecuta la operación y asigna el resultado a la misma variable.
console.log(a += 3); // Adición asignación
console.log(a -= 2); // Resta asignación   
console.log(a *= 4); // Mulitplicación asignación
console.log(a /= 2); // División asignación
console.log(a %= 3); // Modulo asiganción



// OPERADORES DE COMPARACION

// --> Los resultados de estos pueden ser true o false.

console.log(a == b);    // Compruebas valores pero no el tipo de dato
console.log( a === b);  // Comprueba si los valores izquierdo y derecho son idénticos entre sí
console.log( a !== b);  // Comprueba si los valores izquierdo y derecho NO son idénticos entre sí
console.log( a < b);    // Comprueba si el valor izquierdo es menor que el derecho
console.log( a > b);    // Comprueba si el valor izquierdo es mayor que el derecho
console.log( a <= b);   // Comprueba si el valor izquierdo es mayor que el derecho
console.log( a >= b);   // Comprueba si el valor izquierdo es mayor o igual que el derecho


// OPERDADORES LOGICOS

// Operador lógico AND &&
console.log(true && true);   // → true
console.log(true && false);  // → false
console.log(false && false); // → false

//Operador lógico OR ||
console.log(true || true);   // → true
console.log(true || false);  // → true
console.log(false || false); // → false

//Operador lógico NOT !
console.log(!true);  // → false
console.log(!false); // → true


// ESTRUCTURAS DE CONTROL DE FLUJO

/*
‌Las estructuras de control de flujo, son intrucciones que nos permiten evaluar si se puede 
cumplir una condición o no, incluso nos puede ayudar a evaluarla n cantidad de veces.
*/



// Condicional if

/*
    ===> if (condición) {

        Si condicón verdadera
        ejecuta este código.

    }
*/
let edad = 19;

if (edad < 18) {
    console.log("Es menor de edad")
};


// Condicional if...else

/*
    ===> if (condición) {

        Si condicón verdadera
        ejecuta este código.

    } else {

        Si condicón falsa
        ejecuta este código.
    }
*/
if (edad >= 18) {
    console.log("Tiene 18 o más")
} else {
    console.log("Es menor de edad")
};


// Condicional else if

/*
    ===> if (condición) {

        Si condicón verdadera ejecuta este código
        caso contrario evalua siguiente condición.

    } else if (condición2) {

        Si condicón verdadera
        ejecuta este código.

    } else {
        Si no cumple con niguna condición
        anterior ejecuta este código.
    }
*/

if (edad >= 25) {
    console.log("Tiene mas de 25")
} else if ( edad > 18 && edad < 25) {
    console.log("Entre 18 y 25, no incluidos")
} else {
    console.log("Tiene menos de 18")
};


// LOOPS, CICLOS O BUCLES

// Sirven para evaluar una condición repetidamente hasta que se cumpla.

/*  ===> for (expresiónInicial; expresiónCondicional; expresiónDeActualización) {
             instrucción o código a ejecutar
            }
*/

for (let numero = 1; numero <= 10; numero++) {
    console.log(numero)
};


for (let x = 1, y = 5; x < 5; x++, y--) {
    console.log(x, y)
};

// for...of recorre los valores de un objeto iterable.

/*  ===> for (variable of iterable) {
            Codigo a ser ejecutado
        }
*/

const autos = ["BMW", "Volvo", "Mercedez", "Toyota", "Nissan"];

for (let auto of autos) {
    console.log(auto)
};

// for...in recorre las propiedades de un objeto.

/*

    for (propiedad in objeto) {
    // codigo a ejecutar 
    }

*/

const persona = {
    nombre: "Raul",
    apellido: "Cruz",
    edad: 45
};

for (propiedad in persona) {
    console.log(propiedad, persona[propiedad])
};


//  WHILE
//  Ejecuta un bloque de código siempre que una condición especificada sea verdadera.

/*

while (condition) {
  // code block to be executed
}
*/

let i = 3;

// mientras i sea menor de 10, se segurirá ejecutando el códgo entre llaves.
while (i < 10) {
    i++;
    console.log("El numero es " + i);
};

console.log("Fin de bucle while.")

// DO WHILE
// Si la condición no se cumple el código se ejecuta una sola vez.

do {
    console.log('El número es ' + i);
    i--;
}
while (i > 0);


// Switch 

let palabra = 'Python';

switch (palabra) {
    case 'Python':
        console.log(`Me gusta ${palabra}`);
        break;
    case 'Java':
        console.log(`Me gusta ${palabra}`);
        break;
    case 'Código':
        console.log(`Me gusta el ${palabra}`);
        break;
    default:
        console.log('No sé programar.');
        break;
};


// BREAK y CONTINUE

// Delcaración de Ruptura BREAK, se usa para salir de un bucle.


let num2 = 0;

while (num2 < 10) {

    num2++;
    if (num2 === 5) continue;  // Cuando num sea igual a 5 no ejcutara esa iteracion y continuara con el resto 
    
    console.log(num2);
};


let num = 0;

while (num < 10) {

    num++;
    if (num === 5) break;  // Cuando num sea igual a 5 el bucle dejara de ejecutarse. 
    console.log(num);
};


/*
DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/


for(let number = 10; number <= 55; number++) {
    
    if(number%2==0 && number%3!==0 && number!==16){
    console.log(number);
    }
};



