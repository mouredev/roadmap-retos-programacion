let num1 = 2
let num2 = 5

console.log ("Operadores de comparación")

console.log(2 == num1)//igual
console.log(num1 != 3)//No es Igual
console.log("2" === num1)//Estrictamente igual
console.log("2" !== num1)//Desigualdad estricta
console.log(num2 > num1)//Mayor que
console.log(num2 >= num1)//Mayor o igual que
console.log(num1 < num2)//Menor que
console.log(num1 <= num2)//Menor o igual que

console.log ("Operadores aritméticos")

console.log(num1 + num2) // Suma
console.log(num1 - num2) // Resta
console.log(num1 * num2) // Multiplicación
console.log(num1 / num2) // División
console.log(num1 % num2) // Resto
console.log(num1 ++)// Incremento
console.log(num1 --) // Decremento


console.log ("Operadores bit a bit")

let a = 10
let b = 2

console.log(a & b) // AND bit a bit
console.log(a | b) // OR bit a bit
console.log(a ^ b) // XOR bit a bit
console.log(~a)    // NOT bit a bit
console.log(a << 1) // Desplazamiento a la izquierda
console.log(a >> 1) // Desplazamiento a la derecha
console.log(a >>> 1)// Desplazamiento a la derecha sin signo

console.log ("Operadores lógicos")

let myNumber = 8
let myNumber2 = 5

let resultado = (myNumber > myNumber2) && (myNumber2 > 0)
console.log(resultado) // Salida: true

let resultado1 = (myNumber < myNumber2) || (myNumber2 >0)
console.log(resultado1)  // Salida: true

let resultado2 = !(myNumber < myNumber2)
console.log(resultado2)  // Salida: true

console.log("Operadores de cadena")

let word = "javascript"
console.log("Hola desde" + " " + word) // Operador de concatenación

console.log("Operador condicional (Ternario)")

let edad = 18
let result = edad >= 18 ? "Es mayor de edad" : "Es menor de edad"
console.log(result)

/*
Utilizando las operaciones con operadores que tú quieras, crea ejemplos
que representen todos los tipos de estructuras de control que existan
en tu lenguaje:
Condicionales, iterativas, excepciones...
*/

// Condicional

if (edad >= 18){
    console.log("Eres mayor de edad")
}else{
    console.log("Eres menor de edad")
}

// Bucle for

let mult = 5
for (let i = 1; i <=10; i++){
    console.log(`${mult} x ${i} = ${mult * i}`)
}

// Bucle forEach
let paises = ["Argentina", "España", "Noruega", "Luxemburgo"]
paises.forEach(pais => {
    console.log(pais)
})

// Bucle for...in
for (let pais in paises) {
    console.log(paises[pais])
}

// Bucle while

let num = 1
while ( num >= 10){
    if (num% 2 == 0){
        console.log(`${num} es par`)
    }
    num++
}

// Bucle Do While
num = 1
do{
    if(num % 2 == 0){
        console.log(`${num} es par`)
    }
    num++
}while(num >=10)

// Switch
let mes = 4

switch (mes){
    case 1:
        console.log("Enero")
        break;
    case 2:
        console.log("Febrero")
        break;
    case 3:
        console.log("Marzo")
        break;
    case 4:
        console.log("Abril")
        break;
    default:
        console.log("Numero de mes no válido")
}

/*
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

for (let i = 10; i <= 55; i++){
    if(i % 2 ==0 && i != 16 && i % 3 !== 0){
        console.log(i)
    }
}