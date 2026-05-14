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

//Operadores aritméticos

console.log("suma", 17 + 8)
console.log("resta", 25 - 11)
console.log("multiplicacion", 6 * 7)
console.log("división", 20 / 4)
console.log("módulo", 17 % 5)
console.log("potencia", 2 ** 8)

//incremento
let a = 5
a++ 
console.log(a)

//decremento
a--
console.log(a)

//Operadores de asignación
let x = 10
console.log(x += 5)
console.log(x -= 3)
console.log(x *= 2)
console.log(x /= 4)
console.log(x %= 3)
console.log(x **= 2)


//Operadores de comparación
let numero = 5
console.log(numero > 5)
console.log(numero >= 5)
console.log(numero < 5)
console.log(numero <= 5)

console.log(numero == "5")
console.log(numero != 7)
console.log(numero === "5")
console.log(numero !== 5)

//Operadores lógicos
//AND &&
let num1 = 10
let num2 = 5
console.log (num1 > 10 && num2 == 5)

//OR ||
console.log(num1 < 10 || num2 == 5)

//NOT !
console.log(!(num1 == 10))

//Operador ternario
let edad = 17
console.log(edad > 17 ? "Permitir ingreso" : "No puede ingresar")

//Operadores de identidad
let str1 = "Hola"
let str2 = "Hola"
console.log(str1 === str2) //true
console.log(str1 !== str2) //false  

let num3 = 5
let num4 = 5
console.log(num3 == num4) //true
console.log(num3 != num4) //false

//Bitwise
let num5 = 5 // 0101 en binario
let num6 = 3 // 0011 en binario
console.log(num5 & num6) // 0001 en binario
console.log(num5 | num6) // 0111 en binario
console.log(num5 ^ num6) // 0110 en binario
console.log(~num5) // -6 en binario
console.log(num5 << 1) // 1010 en binario
console.log(num5 >> 1) // 0010 en binario

//Condiconales
let nota =85
if (nota >= 90){
    console.log("Excelente")
} else if (nota >= 70){
    console.log("Aprobado")
} else {
    console.log("Reprobado")
}

let dia = 3
let nombreDia
switch (dia){
    case 1:
        nombreDia = "Lunes"
        break;
    case 2:
        nombreDia = "Martes"
        break;
    case 3:
        nombreDia = "Miércoles"
        break;
    case 4:
        nombreDia = "Jueves"
        break;
    case 5:
        nombreDia = "Viernes"
        break;
    case 6:
        nombreDia = "Sábado"
        break;
    case 7:
        nombreDia = "Domingo"
        break;
    default:
        nombreDia = "No es un día valido"
}
console.log(nombreDia)

//Bucles
let suma = 0
for (let i = 1; i<=5; i++) {
    suma += i
}
console.log(suma)

let temp
let resultado = 1 
while (resultado < 100) {
    temp = resultado
    resultado = resultado*2
}
console.log(temp)

let arrayFrutas = ["🍎","🍌","🍇"]
for (let fruta of arrayFrutas) {
    console.log(fruta)
}

let usuario = {nombre:"Ana", edad:22}
for (let propiedad in usuario) {
    console.log(`${propiedad}: ${usuario[propiedad]}`)
}

try {
    console.log(JSON.parse("Esto no es un Json"))
} catch (err) {
    console.log(`Error: ${err.message}`)
}

try {
    console.log(JSON.parse('{"nombre": "Ana"}'))
} catch (error) {
    console.log(`Error: ${error.message}`)
} finally {
    console.log("Esto siempre se ejecuta")
}