// #01 - OPERADORES Y ESTRUCTURAS DE CONTROL
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
*/

// Inicialización de variables:
let numA = 10;
let numB = 5;
let x = 1;
let result;

// Operadores aritméticos:
console.log("Suma: numA + numB ",  numA + numB  );
console.log("Resta: numA - numB", numA - numB  );
console.log("Multiplicación: numA * numB ", numA * numB  );
console.log("Divisón: numA / numB", numA / numB  );
console.log("Módulo: numA % numB",  numA % numB  );
console.log("Autoincrementable: result = x++: (Comunmente lo usamos con un for/while)", x = x++);
console.log("Autoincrementable: result = ++x:", x = ++x);

// Operadores Lógicos:
let isActive    = true;
let isNotActive = false;

// Operadores and(&&) y or(||)
console.log("Operador AND (&&): isActive && isNotActive", isActive && isNotActive);
console.log("Operador OR (||): isActive || isNotActive",  isActive || isNotActive);

// Operadores de comparación:
console.log( "Mayor que: 5 > 1", 5 > 1 );
console.log( "Menor que: 10 < 35", 10 < 35 );
console.log( "Mayor o igual que: 10 >= 10", 10 >= 10 );
console.log( "Menor o igual que: 10 <= 35", 10 <= 35 );

// Operadores de asignación o identidad:
 let nombre = "Omar" // Asignación e identidad

 console.log("Comparación o igualdad estricta: 5 === 5", 5 === 5);
 console.log("Comparación o igualdad estricta: 5 === 4", 5 === 4);
 console.log("Comparación o desigualdad estricta: 5 !== 4", 5 !== 5);
 console.log("Comparación o desigualdad estricta: 5 !== 4", 5 !== 4);

// Estructuras condicionales simple y doble:
// Simple
let edadA = 15;
let edadB = 18;

if(edadA < 18){
    console.log("Estructura condicional Simple");
    console.log("Eres menor de edad");
}

// Condicional Doble:
if( edadB > 18 ){
    console.log("Estructura condicional Doble");
    console.log("Es menor de edad");
} else {
    console.log("Estructura condicional Doble");
    console.log( "Es Mayor de edad");
}

// Condicional multiple ( Switch )
let opcion = 1;
switch (opcion) {
    case 1:
        console.log("Has elegido la opción 1");
        break;
    case 2:
        console.log("Has elegido la opción 2");
        break;
    case 3:
        console.log("Has elegido la opción 3");
        break;
    default:
        console.log("No ha seleccionado una opción válida");;
}

// Estructuras iterativas:
// for
let repetir = 5;
for( let i = 0; i <= repetir; i++ ){
    console.log("Repitiendo FOR desde: i = 0", i);
}

// While y manejo de excepciones
try {
    while (repetir <= 10) {
        console.log("Recorriendo While: ", +repetir);
        repetir++;
    }       
} catch (error) {
    console.warn(error);
}

/*
    *
    * DIFICULTAD EXTRA (opcional):
    * Crea un programa que imprima por consola todos los números comprendidos
    * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    *
*/

try {
    let numeros = 100;
    console.log("### ¡DIFICULTAD EXTRA! ###");
    for(let i=0; i<=numeros; i++){
        if( i >= 10 && i <= 55 ){
            if( i % 2 === 0 && i !== 16 && i % 3 !== 0){
                console.log(">>>: ", i);
            }
        }
    }
} catch (error) {
    console.warn( error );
}

// Aprobado por Chayanne! xD