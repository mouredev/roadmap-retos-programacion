/**
 * Operadores aritméticos:
 * 
 * Suma, resta, multiplicación, división, residuo y potenciación
 */

let num1 = 62
let num2 = 4
let operacion

console.log(operacion = num1 + num2)
console.log(operacion = num1 - num2)
console.log(operacion = num1 * num2)
console.log(operacion = num1 / num2)
console.log(operacion = num1 % num2)
console.log(operacion = num1 ** num2)

/**
 * Operadores de asignación:
 * 
 * Se puede observar que se están haciendo las operaciones (+,-,*,/,%,**) entre las variables “a” y “b” y
 * al mismo tiempo se está asignando el resultado de esas operaciones a la variable “a”.
 */

let a = 10
let b = 4

console.log(a += b)
console.log(a -= b)
console.log(a *= b)
console.log(a /= b)
console.log(a %= b)
console.log(a **= b)

/**
 * Operadores de concatenación
 */

let nombre = "Marisol"
let apellido = "Henao"

let nombreCompleto = nombre + " " + apellido
console.log(nombreCompleto) // Marisol Henao

nombreCompleto = `Mi nombre es ${nombre} y mi apellido es ${apellido}` // Para las llaves debe ser con "backticks" (`)
console.log(nombreCompleto) // Mi nombr es Marisol y mi apellido es Henao

/**
 * Operadores de comparación
 */

// Es igual (compara el valor): ==
a = 50
b = 50

let resultado = a == b
console.log(resultado) // true

// Es estrictamente igual (compara el valor y tipo de dato): ===
a = 50
b = "50"

console.log(resultado = a === b) // false

// Es diferente (verifica que los valores sean diferentes): !=
a = 50
b = 20

console.log(resultado = a != b) // true

// Es estrictamente diferente (verifica el valor y tipo de dato): !==
a = 50
b = "50"

console.log(resultado = a !== b) // true

// Los 4 operadores anteriores los podemos utilizar para comparar números, cadenas de texto y boolenos.

// Mayor que: > y Menor que: <
a = 10
b = 15

console.log(resultado = a > b) // false
console.log(resultado = a < b) // true

// Mayor o igual que: ≥ y Menor o igual que: ≤
a = 15
b = 15

console.log(resultado = a >= b) // true
console.log(resultado = a <= b) // true

/**
 * Operadores lógicos
 */

// AND: &&
a = 10
b = 20
let c = 30

// ¿b es mayor que a y b es mayor que c?
console.log(resultado = (b > a) && (b > c)) // false (Porque se tienen que cumplir las 2)

// OR: ||
a = 10
b = 20
c = 30

// ¿b es mayor que a o b es mayor que c?
console.log(resultado = (b > a) || (b > c)) // true (Porque solo es necesario que se cumpla 1)

/**
 * Operadores unarios:
 * 
 * Pueden aumentar o decrecer su valor por si mismos.
 */

a = 10

a++
console.log(a) // 11

a--
console.log(a) // 9

/**
 * Operadores ternarios:
 * 
 * Los operadores ternarios requieren de 3 argumentos o partes para funcionar:
 * "condición" ? "respuesta si la condición es true" : "respuesta si la condición es false"
 */

let numero1 = 5
let numero2 = 8

let comparacion = numero2 > numero1 ? "Sí es mayor" : "No es mayor"
console.log(comparacion) // Sí es mayor

//---------------------------------------------------------------------------------------------------

/**
 * if else if:
 *  
 * "Si" eres mayor de edad y menor de 65 años puedes venir a la fiesta. 
 * "Sino", "si" tienes permiso firmado y eres menor de 18, puedes venir. 
 * "Sino" no puedes venir a la fiesta.
 */

let persona = "Cleopatra"
let edad = 15
let permiso = true

if (edad > 18 && edad < 65) {
	console.log(`${persona} puedes venir a la fiesta`)
} else if (permiso === true && edad < 18) {
	console.log(`${persona} puedes venir, tienes permiso`) // Cleopatra puedes venir, tienes permiso
} else {
	console.log(`${persona} no puedes venir a la fiesta`)
}

/**
 * for:
 * 
 * Imprimir los numeros del 1 al 9
 */

for (let i = 0; i < 10; i++) {
    console.log(i)
}

/**
 * while:
 * 
 * Mientras la cantidad de juguetes sea mayor a 0, regalar un juguete.
 */

let juguetes = 10

while (juguetes > 0) {
    juguetes--
    console.log(`Regalamos un juguete. Nos quedan ${juguetes}`)
}

/**
 * Switch:
 * 
 * Si eres fuerte y comelón: eres Gokú 
 * Si eres veloz y egoísta: eres Vegetta
 * Si eres pequeño y débil: eres Krillin
 * Si eres travieso y juguetón: eres Trunks
 * Si no eres ninguno, eres una sabandija
 */

let personalidad = "Travieso y juguetón"

switch (personalidad) {
    case "Fuerte y comelón":
        console.log("Eres Gokú")
        break
	case "Veloz y egoísta":
		console.log("Eres Vegetta")
		break
	case "Pequeño y débil":
		console.log("Eres Krillin")
		break
	case "Travieso y juguetón":
		console.log("Eres Trunks") // Eres Trunks
		break
	default:
		console.log("Eres una sabandija!") 
}