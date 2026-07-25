/* Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

let resta = `resta de 10 -5 igual a ${10 - 5}`
let suma = ` suma de 10 + 5 igual a ${10 + 5}`
let division = `division de 10/5 igual a${10 / 5}`
let multiplicaion = `multiplicacion de 10/5 igual a ${10 * 5} `
let modulo = `modulo de 10%5 igual a ${10 % 5} `
let exponente = `exponente de 10**5 igual a ${10 ** 5} `

let mayorQue = 5 > 1;
let menorQue = 5 < 1;
let mayorOIgualQue = 5 >= 1;
let menorOIgualQue = 5 <= 1;
let iguales = 5 === '5';
let igualesNoEsticto = 5 == '5';
let desigual = 5 != '5';
let desigualEstricto = 5 !== '5';

let and_operator = first_bool && second_bool;   // AND
let or_operator = first_bool || second_bool;    // OR
let not_operator = !(first_bool);   

console.log(exponente)

 /*
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
- Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.
 */
let nota1 = 3
let nota2 = 4
let nota3 = 2
let promedio = (nota1 + nota2 + nota3) / 5


if (promedio >= 3) {
    console.log(` aprobo la materia-su promedio es:${promedio}`)
} else if (promedio < 3 && promedio > 2) {
    console.log(`puede rescuperar la mareteria ${promedio}`)

} else {
    console.log(`reprobo la materia-su promedio es:${promedio}`)
}

let edad = 17
let mayor_menor = edad >= 18 ? `eres mayor de edad:${edad}` : `eres menor de edad :${edad}`
console.log(mayor_menor)

for (let index = 0; index < 20; index++) {
    console.log(`numeros: ${index}`);

}
let i = 0
while (i < 20) {
    i++
    console.log(`numeros ${i}`)
}
do {
    i++
    console.log(`numeros ${i}`)

} while (i < 20);


let animal = "loro";

switch (animal) {
    case "perro":
        console.log(`tu mascota es un perro`);
        break;
    case "gato":
        console.log("tu mascota es un gato")
        break;
    default:
        console.log(`ingresa si es gato o perro`);
        break;
}
try {
    console.log(nombre); // Error: 'nombre' no está definido
} catch (error) {
    console.log("  hubo un error:", error.message);
}


/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}
