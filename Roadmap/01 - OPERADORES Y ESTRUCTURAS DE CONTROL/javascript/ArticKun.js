

// Operadores Aritmeticos -----

let num1 = 35;
let num2 = 35;

console.log( `Suma:     ${num1} + ${num2} = ${ num1 + num2 }` );
console.log( `Resta:    ${num1} - ${num2} = ${ num1 - num2 }` );
console.log( `Multi:    ${num1} * ${num2} = ${ num1 * num2 }` );
console.log( `Division: ${num1} / ${num2} = ${ num1 / num2 }` );
console.log( `Modulo:   ${num1} % ${num2} = ${ num1 % num2 }` );
console.log( `Expo:     ${num1} ^ ${num2} = ${ num1 ** num2 }` );

// Operadores Comparación -----

let numb1 = 27;
let numb2 = 35;

console.log(`Igualdad:             ${numb1} == ${numb2} = ${numb1 == numb2}`);
console.log(`Igualdad Estricta:    ${numb1} === ${numb2} = ${numb1 === numb2}`);
console.log(`Desigualdad:          ${numb1} != ${numb2} = ${numb1 != numb2}`);
console.log(`Desigualdad Estricta: ${numb1} !== ${numb2} = ${numb1 !== numb2}`);
console.log(`Mayor que:            ${numb1} > ${numb2} = ${numb1 > numb2}`);
console.log(`Mayor Igual que:      ${numb1} >= ${numb2} = ${numb1 >= numb2}`);
console.log(`Menor que:            ${numb1} < ${numb2} = ${numb1 < numb2}`);
console.log(`Menor Igual que:      ${numb1} <= ${numb2} = ${numb1 <= numb2}`);


// Operadores Lógicos -----

// AND (&&)
let x = 5;
let y = 10;

if (x > 0 && y > 0) {
    console.log("Ambas condiciones son verdaderas");
} else {
    console.log("Al menos una condición es falsa");
};

//ORD (||)
let edad = 25;
let tieneLicencia = false;

if (edad >= 18 || tieneLicencia) {
    console.log("Puede conducir");
} else {
    console.log("No puede conducir");
};

//NOT (!)
let llueve = true;

if (!llueve) {
    console.log("No está lloviendo");
} else {
    console.log("Está lloviendo");
};


//Operadores de asignacion -----

//Simple
let a = 10;
console.log(a);  // 10
//Con Adicion
let b = 5;
b += 3;          // Esto es equivalente b = b + 3;
console.log(b);  // 8
// Con Sustraccion
let c = 8;
c -= 2;          // Esto es equivalente c = c - 2;
console.log(c);  // 6
// Con Multiplicacion
let d = 4;
d *= 3;          // Esto es equivalente d = d * 3;
console.log(d);  // 12
//Con Division
let e = 15;
e /= 5;          // Esto es equivalente e = e / 5;
console.log(e);  // 3
// Con Modulo
let f = 17;
f %= 4;          // Esto es equivalente f = f % 4;
console.log(f);  // 1
// Con Potencia
let g = 2;
g **= 3;         // Esto es equivalente g = g ** 3;
console.log(g);  // 8


// Operadores de Pertenencia ----- 

/*
El operador in se utiliza para verificar si una 
propiedad está presente en un objeto.
*/

let persona = { nombre: 'Juan', edad: 25 };

console.log('nombre' in persona);    // true
console.log('apellido' in persona);  // false

/*el operador in también se puede usar con arreglos 
para verificar si un índice está presente en el arreglo
*/

let arreglo = [1, 2, 3];

console.log(0 in arreglo);  // true
console.log(5 in arreglo);  // false


/*El operador instanceof se utiliza para verificar 
si un objeto es una instancia de una clase o constructor específico.
*/

class Animal {
    constructor(nombre) {
        this.nombre = nombre;
    }
}

let perro = new Animal('Buddy');
console.log(perro instanceof Animal);  // true


// Operadores de Bits ----- 

console.log(3 & 4);   // AND -> 0
console.log(3 | 4);   // OR -> 7
console.log(3 ^ 4);   // XOR -> 7
console.log(~3);      // NOT -> -4
console.log(3 << 4);  // Desplazamiento a izquierda -> 48
console.log(3 >> 4);  // Desplazamiento a derecha -> 0


// Sentencias de Control -----

// 1. Condicionales 

// If else
let numero = 10;

if ( numero > 0 ) {
    console.log("El número es positivo");
} else {
    console.log("El número es cero o negativo");
};

// else if
let calificacion = 85;

if (calificacion >= 90) {
    console.log("A - Excelente");
} else if (calificacion >= 80) {
    console.log("B - Bueno");
} else if (calificacion >= 70) {
    console.log("C - Aceptable");
} else if (calificacion >= 60) {
    console.log("D - Necesita mejorar");
} else {
    console.log("F - Insuficiente");
};

//Switch
let diaSemana = 3;
let nombreDia;

switch ( diaSemana ) {
    case 1:
        nombreDia = "Lunes";
        break;
    case 2:
        nombreDia = "Martes";
        break;
    case 3:
        nombreDia = "Miercoles";
        break;
    case 4:
        nombreDia = "Jueves";
        break;
    case 5:
        nombreDia = "Viernes";
        break;
    case 6:
        nombreDia = "Sábado";
        break;
    case 7:
        nombreDia = "Domingo";
        break;
    // ... otros casos ...
    default:
        nombreDia = "Día no válido";
};

console.log( "Hoy es " + nombreDia );


// 2. Ciclos o Bucles

// For
for ( let i = 1; i <= 5; i++ ) {
    console.log( "Iteración número : " + (i) );
};

//While
let contador = 0;

while ( contador < 5 ) {
    console.log( "Iteración número " + ( contador + 1) );
    contador++;
};

//Do While
let contador2 = 0;

do {
    console.log("Iteración número " + ( contador2 + 1) );
    contador2++;
} while ( contador2 < 5 );


// 3. Ciclos para Objetos y Arrays
// For in
//se utiliza para iterar sobre las propiedades enumerables de un objeto.
//Si se utiliza sobre un array este iterara solo las posiciones del indice
let person = {
    nombre: "Fabian",
    edad: 35,
    pais: "Colombia"
};

for ( let propiedad in person ) {
    console.log( propiedad + ": " + person[propiedad] );
};

// For of
// itera sobre cada elemento del array
let frutas = ["Manzana", "Banana", "Uva"];

for ( let fruta of frutas ) {
    console.log( fruta );
};


// 4. Manejo de errores o Excepciones
//Try Catch
try {
// Código que podría lanzar una excepción
// Intentando dividir por cero
    let resultado = 10 / 0; 
// Esta línea nunca se ejecutará si hay una excepción
    console.log(resultado); 
} catch (error) {
// Bloque de código que se ejecuta en caso de excepción
    console.error("Ha ocurrido un error:", error.message);
} finally {
// Bloque de código opcional que siempre se ejecuta, independientemente de si hay una excepción o no
    console.log("Este bloque siempre se ejecuta");
};

// El programa sigue ejecutándose después del manejo de la excepción
console.log("El programa continúa después del bloque try...catch");


// Ejercicio Extra
/*
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
*/

//Version 1
for ( let i = 10; i <= 55; i++ ) {
    if ( i !== 16 && i % 3 !== 0 && i % 2 === 0 ) {
        console.log( i );
    }
};


//Version 2
for (let i = 10; i <= 55; i++) {
    if ( i === 16 || i % 3 === 0 ) {
        continue;
    }
    if (i % 2 === 0) {
        console.log( i );
    }
};