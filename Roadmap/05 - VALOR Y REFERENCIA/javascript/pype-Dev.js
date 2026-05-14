/**
 * Valor y Referencia
 */

// Tipos Primitivos: Paso por VALOR
// Number
let num1 = 10;
let num2 = num1;
num2 += num1 * 9;

num1 = 50;

console.log(num1);   // 10
console.log(num2);   // 100

//String
let saludo = 'Hola';
let mensaje = saludo;
mensaje = saludo + " " + 'Mundo!';

saludo = 'Hola JavaScript!';

console.log(saludo);   // Hola JavaScript!
console.log(mensaje);   // Hola Mundo!

// Tipos No Primitivos: Paso por REFERENCIA
// Objects
const persona = {name: 'Karen', gender: 'Mujer'};
const edad = persona;

edad.age = 23;

console.log(persona);   // {name: 'Karen', gender: 'Mujer', age: 23}
console.log(edad);   // {name: 'Karen', gender: 'Mujer', age: 23}

// Arrays
const familia = ['Monica', 'Juan', 'Alejandra'];
const integrantes = familia;

integrantes.push('Karen');

console.log(familia);   // (4) ['Monica', 'Juan', 'Alejandra', 'Karen']
console.log(integrantes);   // (4) ['Monica', 'Juan', 'Alejandra', 'Karen']

// Funciones por VALOR
function calificacionExtra(calificacionFinal){
    calificacionFinal = calificacionFinal + 25;
    console.log(`Nota final del módulo: ${calificacionFinal}`);   // Nota final del módulo: 85
}

let calificacionParcial = 60;
calificacionExtra(calificacionParcial);

console.log(`Nota parcial del módulo: ${calificacionParcial}`);   // Nota parcial del módulo: 60

// Funciones por REFERENCIA
let heroesMarvel = ['Iron Man', 'Capitan America', 'Thor'];

function nuevosHeroes (equipoAvengers, miembros){
    equipoAvengers.push(miembros);
    console.log('Todos los Vengadores de Marvel:', equipoAvengers);   // Todos los Vengadores de Marvel: (4) ['Iron Man', 'Capitan America', 'Thor', 'Spider Man']
}

nuevosHeroes(heroesMarvel, 'Spider Man');

console.log('Vengadores originales:', heroesMarvel);   // Vengadores originales: (4) ['Iron Man', 'Capitan America', 'Thor', 'Spider Man']

/**
 * DIFICULTAD EXTRA
 */

// Paso por VALOR
let paramX = 5;
let paramY = 10;

const swapValor = (paramX, paramY) => {
    let paramTemp;

    paramTemp = paramX;
    paramX = paramY;
    paramY = paramTemp;
    
    return [paramX, paramY];
}

let [paramNewX, paramNewY] = swapValor(paramX, paramY);

console.log(`Variables originales: X es ${paramX} y Y es ${paramY}`);
console.log(`Nuevas variables: X es: ${paramNewX} y Y es ${paramNewY}`);

// Paso por REFERENCIA
let person1 = {name : 'Karen'};
let person2 = {name : 'Felipe'};

const swapReferencia = (p1, p2) => {
    let personTemp;

    personTemp = p1;
    p1 = p2;
    p2 = personTemp;

    return [p1.name, p2.name];
}

let [newName1, newName2] = swapReferencia(person1, person2);

console.log(`Los nombres originales son: ${person1.name} y ${person2.name}`);
console.log(`Los nombres invertidos son: ${newName1} y ${newName2}`);


