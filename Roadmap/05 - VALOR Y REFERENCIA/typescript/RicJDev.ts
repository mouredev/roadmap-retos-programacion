//Tipos de datos por valor
let number1: number = 10
let number2: number = number1

console.log(number2)

number1 += 20

console.log(number1)
console.log(number2)

//Función con variables por valor
let number3: number = 5

function add40(num: number) {
	return num + 40
}

console.log(number3)

add40(number3)
console.log(number3)

//Tipos de datos por referencia
let array1: number[] = [12, 30, 12]
let array2: number[] = array1

console.log(array1)

array2.push(10)

console.log(array1)
console.log(array2)

//Función con variables por referencia
let array3: number[] = [10, 20, 30]

function customPop(arr: any[]) {
	return (arr.length -= 1)
}

console.log(array3)

customPop(array3)
console.log(array3)

//EXTRA
function changeValues(a: any, b: any) {
	let change = a

	a = b
	b = change

	return [a, b]
}

//Variables por valor
let number4 = 20
let number5 = 50

let [newNumber4, newNumber5] = changeValues(number4, number5)

console.log('Valores originales:', number4, number5)
console.log('Valores cambiados:', newNumber4, newNumber5)

//Variables por referencia
let array5 = [12, 10, 14]
let array6 = [20, 22, 25]

let [newArray5, newArray6] = changeValues(array5, array6)

console.log('Valores originales:', array5, array6)
console.log('Valores cambiados:', newArray5, newArray6)
