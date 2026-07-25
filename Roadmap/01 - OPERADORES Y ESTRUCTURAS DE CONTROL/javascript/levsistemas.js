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

let suma = 2 + 2
let resta = 2 - 1
let multiplicar = 2 * 2
let dividir = 2 / 2
let potenciacion = 2 ** 2
let raiz = Math.sqrt(9)
let modulo = 6 % 2
let adicionar=0

console.log("Suma: 2 + 2", suma)
console.log("Resta: 2 - 1", resta)
console.log("Multiplicar: 2 * 2", multiplicar)
console.log("Dividir: 2 / 2", dividir)
console.log("Potenciacion: 2 ** 2", potenciacion)
console.log("Raiz: 9", raiz)
console.log("Modulo: 6 % 2", modulo)

adicionar++

console.log(adicionar)

adicionar--

console.log(adicionar)

let verdadero = true

console.log(verdadero)

let falso = false

console.log(falso)

if(1+1==2 && 6-5==1) {
    console.log("Comparador AND &&")
}

if(2+2==4 || 5-5==1) {
    console.log("Comparador OR ||")
}

if (!false) {
    console.log("Esta condición también es válida!")
}

if(true!==(!true)) {
    console.log("Condicion donde es diferente y se cumple.")
}

if(2 + 2 === 4) {
    console.log("Condición donde la triple comparacion funciona por valor y tipo.")
}

if(1 + 1 == "2") {
    console.log("Condición que se cumple a modo de valor")
}

if(1 + 1 === "2") {
    console.log("Este mensaje no se va a imprimir")
} else {
    console.log("Este mensaje pasando por ELSE si se imprimirá")
}

const miArreglo = [100, 200, 300, 400]
console.log(0 in miArreglo, "Funciona")
console.log(1 in miArreglo, "Funciona")
console.log(2 in miArreglo, "Funciona")
console.log(3 in miArreglo, "Funciona")
console.log(4 in miArreglo, "No Funcionará")

const persona = {
    nombre: "Leandro",
    edad: 38
};

console.log("nombre" in persona)
console.log("hobbies" in persona)

// DIFICULTAD EXTRA

for ( let i=10 ; i<=55 ; i++ ) {
    
    if(i % 2 == 0) {
        console.log("Los números Pares: ", i)
    }
    
    if(i!==16){
        console.log("Los números distintos a 16... ", i)
    }
    
    if(i % 3!==0){
        console.log("Los números no múltiplos de 3...", i)
    }
}