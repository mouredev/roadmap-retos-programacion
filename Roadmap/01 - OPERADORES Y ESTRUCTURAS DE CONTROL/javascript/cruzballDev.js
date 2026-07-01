/*EJERCICIO:
  Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
*/

let a = 2;
let b = 5;
let c = "5";


// Aritméticos

console.log("Suma 2 + 5 = " + (a + b))
console.log("Suma 2 + 5 = " + a + b)
console.log(`Suma 2 + 5 = ${a + b}`)
console.log("Suma 2 + 5 = ", a + b)
console.log("Resta 2 - 5 = ", a - b)
console.log("División 2 / 5 = ", a / b)
console.log("multiplicación 2 * 5 = ", a * b)
console.log("Resto = 2 % 5 ", a % b)
console.log("Exponente = 2 ** 5 ", a ** b)
console.log("Incremento ++a ", ++a)
console.log("Decrimento --a", --a)


// De comparación

console.log("Mayor que 5 > 2 = ", b > a)
console.log("Menor que = 5 < 2", b < a)
console.log("Mayor igual = 5 >= 5", b >= b)
console.log("Menor igual = 5 <= 2", b <= a)
console.log("Igual = 5 == `5`", b == c) // Compara solo el valor
console.log("Estrictamente igual = 5 === `5`  ", b === c) // Compara valor y tipo de dato
console.log("Distinto = 5 != `5`", b != c) // Compara solo el valor
console.log("Estrictamente Distinto = 5 !== `5` ", b !== c) // Compara valor y tipo de dato

//Lógicos

let d = true;
let e = false;

console.log("AND = ", d && e)
console.log("OR = ", d || e)
console.log("NOT = ", !d)
console.log("NOT = ", !e)

// Asignación

let num = 10

num += 5; // 15
num -= 5; // 5
num *= 5; // 50
num /= 5; // 2
num %= 5; // 0

console.log(num);


// IDENTIDAD (SOLO PARA OBJETOS)

const myObjeto1 = {
    numero : 1
}
const myObjeto2 = {
    numero : 1
}

const myObjeto3 = myObjeto1;

console.log(`myObjeto1 === myObjeto2 es:  ${myObjeto1 === myObjeto2}`)
console.log(`myObjeto1 === myObjeto3 es:  ${myObjeto1 === myObjeto3}`)
console.log(`myObjeto1 !== myObjeto2 es:  ${myObjeto1 !== myObjeto2}`)
console.log(`myObjeto1 !== myObjeto3 es:  ${myObjeto1 !== myObjeto3}`)


// PERTENENCIA (SOLO PARA OBJETOS)

console.log("Está numero en myObjeto1","numero" in myObjeto1) // true
console.log("Está nombre en myObjeto1","nombre" in myObjeto1) // false

// Operador Ternario

let nota  = 7

let resultado = nota >= 5 ? "Aprobado" : "Suspenso";
console.log(resultado)

/*Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
    Debes hacer print por consola del resultado de todos los ejemplos.
*/


// CONDICIONALES

//condicional if

let numPositiv = 20

if(numPositiv >= 1) {
    console.log(`Si, ${numPositiv} es un número positivo`)
}

// Condicional if / else if

let profesion = "Técnicosss"

if(profesion == "Programador") {
    console.log("Mi profesión es Programador")
}else if (profesion == "Técnico") {
    console.log("Mi profesión es Técnico")
}else {
    console.log("Mi profesión no es Programador ni Técnico")
}

// Operador ternario

let myName = "Antonio"
let logeado = true

let mensaje = logeado ? `Bienvenido ${myName}` : "Tiene que logearse"

console.log(mensaje)

// Switch

let dia = 5

switch(dia) {
    case 1:
        console.log("Lunes")
        break;
    case 2:
        console.log("Martes")
        break;
    case 3:
        console.log("Miercoles")
        break;
    default:
        console.log("Otro día")
}


// ITERATIVOS

//while

let i = 1

while(i <= 3){
    console.log("while", i)
    i++
}

// Do while

let j = 1

do {
    console.log("do .......while", j)
    j++
}while(j <=3);

// For

let animales = ["Perro", "Gato", "Gallina", "Conejo"]

/* for(i = 0; i < animales.length; i++) {
    console.log("Los animales son: " + animales[i])
} */

    for(let animal of animales) {
        console.log( animal + ": Es un animal;")
    }

console.log("------------------------------------------------------------------------")


// For of

const frutas = ["Manzana", "Pera", "Naranja"];

for(let fruta of frutas) {
    console.log(fruta)
}

const palabra = "Hola"

for(let letra of palabra) {
    console.log(letra)
}
console.log("\n --------------\n")
const frase = "Esto es una frase"

for(let word of frase) {
    console.log(word)
}

console.log("------------------------------------------------------------------------")

// For in

const persona1 = {
    nombre: "Manolo",
    edad: 25,
    email: "manolo25@gmail.com"
}

for(let clave in persona1) { // Para obtener la clave del objeto
    console.log(clave)
}

for(let clave in persona1) {
    console.log(`${clave} : ${persona1[clave]}`) // Para obtener la clave del objeto y EL VALOR del objeto
}

// Break
for (let x = 1; x <= 5; x++) {
    if (x === 3) {
        break;
    }
    console.log("break:", x);
}

// Continue
for (let y = 1; y <= 5; y++) {
    if (y === 3) {
        continue;
    }
    console.log("continue:", y);
}


// Try catch
let numero = -3

try{
    if(numero >= 1 ) {
        console.log(`El número: ${numero} es un número válido`)
    }else{
        throw new Error("Ha ocurrido un error")
    }

}catch(error) {
    console.log("Error capturado", error.message)
}
finally {
    console.log("El programa ha terminado")
}


const numeros = [10, 20, 30];

numeros.forEach(numero => {
    console.log(numero)
})

// forEach
frutas.forEach((fruta) => {
    console.log( fruta);
});

numeros.forEach((num, i, array) => {
    console.log(`Elemento: ${num}, posición: ${i}`);
    console.log("Array completo:", array);
});

// sumar valores

let suma = 0

numeros.forEach(num => {
    suma += num
})
 console.log(suma)

 const usuarios = [
    { nombre: "Ana", edad: 25 },
    { nombre: "Luis", edad: 30 }
];

usuarios.forEach(usuario => {
    console.log(usuario.nombre, usuario.edad);
});

for (let usuario in usuarios){
    console.log(usuario, usuarios[usuario])
}

/* DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

/*
let pares = []

 for(let i = 9; i <= 55; i++ ) {
    if( i % 2 !== 0) {
       continue
    }
    if( i === 16) {
            continue
    }
    if( i % 3 === 0) {
        continue
    }
    pares.push(i)
}
console.log(pares) */

//------------ Un solo if que incluyen varias condiciones usando operadores lógicos------------



// ------------Con || para descartar el resultado de las condiciones------------


/*
let pares = []

for(let i = 9; i <= 55; i++ ) {
    if(i % 3 === 0 || i === 16 || i % 2 !== 0) {
        continue
    }
    pares.push(i)
}
console.log(pares) */


// ------------Con && para incluir el resulado de las condiciones------------

let pares = []

for(let i = 9; i <= 55; i++) {
    if(i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        pares.push(i)
    }
}
console.log(pares)