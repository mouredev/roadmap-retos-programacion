let x = prompt("Ingrese un número")
a = parseInt(x)
let y = prompt("Ingrese otro número")
b = parseInt(y)

const sum = a + b
const sub = a - b
const factor = a * b
const div = a / b
const mod = a % b

console.log("La suma es", sum, "La resta es", sub, "La multiplicacion es", factor, "El resto de la divison es", div, "El modulo es", mod)

//Los siguientes ejercicios aplican operadores de igualdad


//Cuenta y lista los números comprendidos entre a y b usando bucles if y for. En cao de que A sea menor que B, la lista es ascendente
if (a < b) {
    console.log("a es menor a b")
    for (let i = a; i <= b; i++) {
        console.log(i)
    }
} else if (a === b) {
    console.log("a es igual a b")
}

//Cuenta y lista los números comprendidos entre a y b usando bucles while. En caso de que A sea mayor que B, la lista es descendiente
if (a > b) {
    console.log("a es mayor a b")
    do {
        console.log(a)
        a--
    } while(a > b);
}

// Operadores logicos 

if (a != b) {
    console.log("A es diferente a b")
} if (a <= 10 && a >= 1) {
    console.log("A esta entre 10 y 1")
} else if (a <= 10 || a >= 1) {
    console.log("A puede estar fuera del rango del 1 al 10")
}

/* Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3 */

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i != 16 && i % 3 != 0) {
        console.log(i)
    }
}