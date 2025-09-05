// * EJERCICIO:

/* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes) */



// Operadores aritméticos

let num1 = 7
let num2 = 3

//Suma
console.log(`La suma de ${num1} + ${num2} es igual a: ${num1 + num2}`)

//Resta
console.log(`La resta de ${num1} - ${num2} es igual a: ${num1 - num2}`)

//Multiplicación
console.log(`La multiplicación de ${num1} * ${num2} es igual a: ${num1 * num2}`)

//División
console.log(`La división de ${num1} / ${num2} es igual a: ${num1 / num2}`)

//Incremento
let num3 = 6
console.log(`El número original es ${num3}`)

num3++
console.log(`Si incrementamos en 1 el número resultante es: ${num3}`)

//Decremento
num3 = 6
num3--
console.log(`Si decrementamos en 1 el número resultante es: ${num3}`)

// Operadores de asignación

let num4 = 5
console.log(`El número original es :${num4}`)
num4 += 2
console.log(`Si le añadimos 2 sería igual a: ${num4}`)
num4 -= 2
console.log(`Si le restamos 2 sería igual a: ${num4}`)
num4 *= 2
console.log(`Si lo multiplicamos *2 sería igual a: ${num4}`)
num4 /= 2
console.log(`Si le dividimos / 2 sería igual a: ${num4}`)
num4 **= 2
console.log(`Si lo elevamos al cuadrado nos da como resultado: ${num4}`)
num4 %= 2
console.log(`El resto de 2 es igual a: ${num4}`)

// Operadores de comparación

let num5 = 9
console.log(`El primer número es: ${num5}`)
let num6 = 7
console.log(`El segundo número es: ${num6}`)

console.log(`El número ${num5} es mayor que ${num6}: ${num5 > num6}`)
console.log(`El número ${num5} es menor que ${num6}: ${num5 < num6}`)
console.log(`El número ${num5} es mayor o igual que ${num6}: ${num5 >= num6}`)
console.log(`El número ${num5} es menor o igual que ${num6}: ${num5 <= num6}`)
console.log(`El número ${num5} es igual que ${num6}: ${num5 == num6}`) // Igualdad por valor
console.log(`El número ${num6} es igual que ${num6}: ${num6 === num6}`) // Igualdad por identidad
console.log(`El número ${num5} es igual que "9": ${num5 === "9"}`) 
console.log(`El número ${num5} es igual que 9: ${num5 === 9}`) 
console.log(`El número ${num5} es diferente que 9: ${num5 != 9}`) 

//Operadores lógicos


//AND (&&)

console.log(5>3 && 7>4)
console.log(5 < 10 && 15 < 20)
console.log(5 < 10 && 15 > 20)
console.log(5 < 10 && 15 > 20 && 30 > 40)


//OR (||)

console.log(5 > 10 || 15 > 20)
console.log(5 < 10 || 15 < 20)
console.log(5 < 10 || 15 > 20)

console.log(5 < 10 && 15 > 20 || 30 < 40)

// not (!)
console.log(!true)
console.log(!false)
console.log(!(5 < 10 && 15 >20))


// Operadores ternarios

const tenemosAgua = true

tenemosAgua ? console.log("Nos bañamos") : console.log("Pura colonia y sale jajajaja!")

let num7 = 7 // 0111
let num8 = 8 // 1000
let num9 = 9 // 1001
let num10 = -9
let resultado = 0

// Operadores bitwise

//Operador &
console.log(resultado=(num7 & num8))
console.log(resultado=(num9 & num8))

//Operador |
console.log(resultado=(num7 | num8))

// Operador ^
console.log(resultado =(num7 ^ num8))
console.log(resultado =(num9 ^ num8))

// Operador NOT ~
console.log(~num7)

//Operadores de desplazamiento

//Operador de desplazamiento de izquierda
console.log(resultado=(num7 << 2))

//Operador de desplazamiento de derecha
console.log(resultado=(num7 >> 2))

//Operador de desplazamiento a la derecha con relleno cero 
console.log(resultado=(num10 >>> 2))

//Operador typeof
let var1 = "Palabra"
console.log(typeof(var1))
console.log(typeof(num1))
console.log(typeof(true))

class Person{
    constructor(name, age, alias){
        this.name = name
        this.age = age
        this.alias = alias

    }
}
console.log(typeof(Person))

let person = new Person("Carlos", 33, "CarlosMqz969")
console.log(typeof(person))


//Operador instanceof
console.log(person instanceof Person)
console.log(person instanceof Object)
console.log(person instanceof Array)

// Operador in

console.log("name" in person)
console.log("alias" in person)
console.log("country" in person)

// Operador de función nula
// Ideal para valores que pueden ser null o undefined 
let bebida = null
let resultadoBebida = bebida ?? "Agua"
console.log(resultadoBebida)

// Operador coma ,
// Evalua varias expresiones y devuelve la última

let x = (console.log("Uno"), console.log("Dos"), 3)
console.log(x)

/*
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.

*/

// Condicionales

// if 
// else 
// if else

let edad = 20

if(edad == 18){
    console.log(`Acabas de cumplir la mayoria de edad tienes: ${edad} años de edad, bienvenido!`)
} else if(edad < 18){
    console.log(`Lo lamento no eres mayor de edad tienes: ${edad} años y debes superar los 18 años de edad para poder ingresar`)
} else{
    console.log(`Tienes: ${edad} años de edad, bienvenido!`)
}

// switch

let idioma = 9
let saludo

switch(idioma){
    case 0:
        saludo = "Hola y bienvenido al mundo de la programación" // Español
        break
        case 1:
        saludo ="Hello and welcome to the world of programming" // Ingles
        break
        case 2:
        saludo ="Hallo und willkommen in der Welt des Programmierens" // Aleman
        break
        case 3:
        saludo = "Bonjour et bienvenue dans le monde de la programmation" // Frances
        break
        case 4:
        saludo = "こんにちは、プログラミングの世界へようこそ" // Japones
        break
        case 5:
        saludo = "Olá e bem-vindo ao mundo da programação" // Portugues
        break
        case 6:
        saludo = "你好，歡迎來到程式設計世界" // Chino
        break
        default:
        saludo = "您沒有添加正確的語言" // Error en chino jajajaja

}
console.log(saludo)

/*
Iterativas (bucles)

for

while

do...while

for...of (para recorrer arrays)

for...in (para recorrer propiedades de objetos)

*/

// Bucle for

for (i = 1; i<= 20; i++){
    console.log(`Vamos en el número: ${i}`)
}
console.log("Felicidades saliste del bucle for! :D")

// Bucle while

let numeros = [5, 3, 2, 7, 3, 0]
let iterable = 0
let sumatoria = 0

while (numeros[iterable] !== 0) {
    sumatoria += numeros[iterable]
    iterable ++
}

console.log("La suma total es: " + sumatoria)

// do while

let iterable1 = 10

do {
    console.log(`Contemos del 10 al 1: ${iterable1}`)
    iterable1 --
} while (iterable1 >= 1)
    console.log("Cuenta regresiva terminada :D")

//for...of (para recorrer arrays)

let myArray = new Array(5)
myArray = [1, 2, 3, 4, 5]

for (let array_valor of myArray){
    console.log(array_valor)
}

//for...in (para recorrer propiedades de objetos)

let account = {
    name: "Carlos",
    surname: "Marquez",
    age: 33
}

for (let object_valor in account) {
    console.log(`${object_valor}: ${account[object_valor]}`)
}

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 * */

for (let range = 10; range <= 55; range ++){
    if(range %2 == 0 && range != 16 && range %3 != 0){
        console.log(`numero: ${range}`)
    } 
}

