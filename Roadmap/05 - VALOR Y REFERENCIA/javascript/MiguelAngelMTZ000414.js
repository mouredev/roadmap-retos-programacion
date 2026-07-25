console.warn("----------(◉◉∖____/◉◉)---------- Tipo por valor ----------(OO∖____/OO)----------")

// Hay 5 tipos de datos que son pasados por valor_Number: Boolean, Null, Undefined, String y Number los cuales son de tipo valor_Numberes primitivos

let valor_Number1 = 918
let valor_Number2 = 40
let valor_String1 = "Porsche"
let valor_String2 = "Spyder"
let valor_String5 = "2414"
let valor_Null1 = null
let valor_Undefined1 = undefined
let valor_boolean1 = true

valor_Number5 = valor_Number1 // valor_Number5 toma el valor de valor_Number1: undefined = 918
valor_Number3 = valor_Number1 // valor_Number3 toma el valor de valor_Number1: undefined = 918
valor_Number1 = valor_Number2 // valor_Number1 toma el valor de valor_Number2: 918 = 40
valor_Number2 = valor_Number1 // valor_Number2 toma el valor de valor_Number1: 20 = 40
valor_Number3 = valor_Number1 // valor_Number3 toma el valor de valor_Number1: 918 = 40
valor_Number4 = valor_Number3 // valor_Number4 toma el valor de valor_Number3: undefined = 40
valor_Number6 = valor_Number5 // valor_Number6 toma el valor de valor_Number5: undefined = 918
valor_Number7 = valor_String1.concat(" ", valor_Number6, " ", valor_String2) // valor_Number7 toma el valor de valor_String1: undefined = Porsche concatenando 918 y Spyder
// valor_String1.concat(" ", valor_String2)
valor_String3 = valor_String1 // valor_String3 toma el valor de valor_String1: undefined = Porsche
valor_String4 = valor_Number5.toString() // valor_String4 toma el valor de valor_Number5 convirtiendolo en String: undefined = 918
valor_Number8 = parseInt(valor_String5) // valor_Number8 toma el valor de valor_String5 convertiendolo en Number: undefined = 2414
valor_Number1 = valor_Null1 // valor_Number1 toma el valor de valor_Null1: 40 = null
valor_Null2 = valor_Undefined1 // valor_Null2 toma el valor de valor_Undefined: undefined = undefined

console.log("valor por tipo: " + typeof valor_Number5 + " = " + valor_Number5)
console.log("valor por tipo: " + typeof valor_Number1 + " = " + valor_Number1)
console.log("valor por tipo: " + typeof valor_Number2 + " = " + valor_Number2)
console.log("valor por tipo: " + typeof valor_Number3 + " = " + valor_Number3)
console.log("valor por tipo: " + typeof valor_Number4 + " = " + valor_Number4)
console.log("valor por tipo: " + typeof valor_Number6 + " = " + valor_Number6)
console.log("valor por tipo: " + typeof valor_Number7 + " = " + valor_Number7)
console.log("valor por tipo: " + typeof valor_String3 + " = " + valor_String3)
console.log("valor por tipo: " + typeof valor_String1 + " = " + valor_String1)
console.log("valor por tipo: " + typeof valor_String4 + " = " + valor_String4)
console.log("valor por tipo: " + typeof valor_Number8 + " = " + valor_Number8)
console.log("valor por tipo: " + typeof valor_Number1 + " = " + valor_Number1)
console.log("valor por tipo: " + typeof valor_Null2 + " = " + valor_Null2)

console.warn("----------(◉◉∖____/◉◉)---------- Tipo por Referencia ----------(OO∖____/OO)----------")
let referencia_Arreglo0 = [1, 2, 3, 4, 5, 6, 7, 8] // Definimos un arreglo de tipo Number
let referencia_Arreglo1 = [10, 20, 30, 40] // Definimos un arreglo de tipo Number
let referencia_Arreglo2 = [60, 70, 80, 90] // Definimos un arreglo de tipo Number

referencia_Arreglo5 = [...referencia_Arreglo1] // Creamos una copia a partir del arreglo[...referencia_Arreglo1], usando el operador de propagación, ahora es un arreglo independiente
referencia_Arreglo3 = referencia_Arreglo1 // El arreglo "referencia_Arraglo1" es asignado como arreglo [referencia_Arreglo3]
referencia_Arreglo3.push(50) // Agregamos un nuevo valor al final del arreglo con la función push
referencia_Arreglo3.unshift(9) // Agregamos un nuevo valor al principio del arreglo con la función unshift
referencia_Arreglo4 = referencia_Arreglo3 // El arreglo [referencia_Arreglo4] toma la referencia del arreglo [referencia_Arreglo3] 
referencia_Arreglo6 = [...referencia_Arreglo1] // Creamos una copia a partir del arreglo [referencia_Arreglo1], ahora es un arreglo 
referencia_Arreglo7 = referencia_Arreglo6 // El arreglo [referencia_Arreglo7] toma la referencia del arreglo [referencia_Arreglo6]
referencia_Arreglo7.push(60) // Agregamos un nuevo valor al final del arreglo con la funcion push
referencia_Arreglo8 = [...referencia_Arreglo7] // Creamos una copia a partir del arreglo [referencia_Arreglo7], ahora es un arreglo 
referencia_Arreglo8.push(70) // Agregamos un nuevo valor al final del arreglo con la funcion push 
referencia_Arreglo9 = [...referencia_Arreglo4] // Creamos una copias a partir del arreglo [referencia_Arreglo4], ahora es un arreglo 
referencia_Arreglo10 = referencia_Arreglo9.concat(referencia_Arreglo2) // Con la funcion concat fucionaremos los arreglos [referencia_Arreglo9] y [referencia_Arreglo2] creando un nuevo arreglo con los valores existentes.
referencia_Arreglo10.push(100) // Agregaremos dos valores al final del arreglo con la funcion push 
referencia_Arreglo10.push(110) // Agregaremos dos valores al final del arreglo con la funcion push 
referencia_Arreglo11 = [].concat(referencia_Arreglo0, referencia_Arreglo10) // Con la funcion concat fucionaremos dos arreglos
referencia_Arreglo10.push(120) // Agregamos un valor al final del arreglo con la funcion push
referencia_Arreglo11.unshift(0) // Agregamos un valor al principio del arreglo con la funcion unshift
referencia_Arreglo11.push(110) // Agregamos un valor al final del arreglo con la funcion push


console.log(`Valor por referencia:`, referencia_Arreglo1)
console.log(`Valor por referencia:`, referencia_Arreglo2)
console.log(`Valor por referencia:`, referencia_Arreglo3)
console.log(`Valor por referencia:`, referencia_Arreglo4)
console.log(`Valor por referencia copia:`, referencia_Arreglo5)
console.log(`Valor por referencia copia:`, referencia_Arreglo6)
console.log(`Valor por referencia:`, referencia_Arreglo7)
console.log(`Valor por referencia copia:`, referencia_Arreglo8)
console.log(`Valor por referencia copia:`, referencia_Arreglo9)
console.log(`Valor por referencia, unión:`, referencia_Arreglo10)
console.log(`Valor por referencia, unión:`, referencia_Arreglo11)

console.warn("----------(◉◉∖____/◉◉)---------- Extra ----------(OO∖____/OO)----------")
console.log("---------- Valor ----------")
let valor1 = 10 // Declaramos dos valores
let valor2 = 20 // Declaramos dos valores
function Valor(valor_1, valor_2) {
    valor_original_1 = valor_1 // valor_original_1 tomara el valor de valor_1: undefined = 10
    valor_original_2 = valor_2 // valor_original_2 tomara el valor de valor_2: undefined = 20
    valor1 = valor_1 // valor1 tomara el valor de valor_1: undefined = 10
    valor_1 = valor_2 // valor_1 tomara el valor de valor_2: 10 = 20
    valor_2 = valor1 // valor_2 tomara el valor1: 20 = 10
    console.log(`${valor_original_1}, ${valor_original_2}`) // Salida: 10, 20
    console.log(`${valor_1}, ${valor_2}`) // Salida: 20, 10
}
Valor(valor1, valor2)

console.log("---------- Referencia ----------")
let referencia1 = [1, 2, 3, 4, 5] // Definimos dos arreglos
let referencia2 = [6, 7, 8, 9, 10] // Definimos dos arreglos

// Definimos una funcion que recibira dos parametros/argumentos
function Referencia(referencia_1, referencia_2) {
    referencia_copia1 = referencia_1 // referencia_copia1 tomara el valor de referencia_1: undefined = referencia1
    referencia_copia2 = referencia_2 // referencia_copia2 tomara el valor de referencia_2: undefined = referencia2
    referencia_copia1.unshift(0) // Agregamos un valor al principio del arreglo con la funcion unshift [referencia_copia1]
    referencia_1 = referencia_copia2 // referencia_1 tomar el valor de referencia_copia2: 
    referencia_1.push(11) // Agregamos un valor al final del arreglo con la funcion push [referencia_1]
    referencia_2 = referencia_copia1 // referencia_2 toma el valor de referencia_copia1
    referencia_2.unshift(-3, -2, -1) // Agregamos varios valores al principio del arreglo [referencia_2]
    console.log(`${referencia_copia1}, ${referencia_copia2}`)
    console.log(`${referencia_1}, ${referencia_2}`)
}
Referencia(referencia1, referencia2)
