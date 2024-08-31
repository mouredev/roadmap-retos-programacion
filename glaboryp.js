let numero = 1
console.log(numero++) // Operador de incremento sufijo
console.log(++numero) // Operador de incremento prefijo
console.log(numero--) // Operador de decremento sufijo
console.log(--numero) // Operador de decremento prefijo

let numero1 = 3
let numero2 = 6
console.log(numero1 + numero2) // Operador de adición o suma
console.log(numero1 - numero2) // Operador de sustracción o resta
console.log(numero1 / numero2) // Operador de división
console.log(numero1 * numero2) // Operador de multiplicación
console.log(numero1 % numero2) // Operador de residuo
console.log(numero1 ** numero2) // Operador de exponenciación

console.log(numero1 < numero2) // Operador menor que
console.log(numero1 <= numero2) // Operador menor o igual que
console.log(numero1 > numero2) // Operador mayor que
console.log(numero1 >= numero2) // Operador mayor o igual que
console.log(numero1 == numero2) // Operador igualdad
console.log(numero1 === numero2) // Operador igualdad estricta
console.log(numero1 != numero2) // Operador desigualdad
console.log(numero1 !== numero2) // Operador desigualdad estricta

let booleano = true
console.log(!booleano) // Operador NOT lógico

let booleano1 = true
let booleano2 = true
console.log(booleano1 && booleano2) // Operador AND lógico
console.log(booleano1 || booleano2) // Operador OR lógico

const objeto = { nombre: 'Gloria', apellidos: 'Labory' }
console.log('nombre' in objeto) // El operador in determina si un objeto tiene una determinada propiedad

const dia = new Date(1996, 7, 25)
console.log(dia instanceof Date) // El operador instanceof determina si un objeto es una instancia de otro objeto

console.log(booleano1 ? 'Es verdadero' : 'Es falso')

if (booleano1) {
  console.log('booleano1 es verdadero')
} else if (booleano2) {
  console.log('booleano2 es verdadero y booleano1 es falso')
} else {
  console.log('Tanto booleano1 como booleano2 son falsos')
}

const ejemplo = 'perro'
switch (ejemplo) {
  case 'perro':
    console.log('Es un perro')
    break;

  case 'gato':
    console.log('Es un gato')
    break;

  case 'pez':
    console.log('Es un pez')
    break;

  case 'tigre':
    console.log('Es un tigre')
    break;

  default:
    console.log('No se sabe que es')
    break;
}

const lista = [1, 5, 33, 4, 51, 9, 1, 82, 3]
let suma = 0
for (let index = 0; index < lista.length; index++) {
  suma += lista[index]
}
console.log(suma)

suma = 0
lista.forEach(element => {
  suma += element
})
console.log(suma)

let n = 0
let x = 0
while (n < 3) {
  n++
  x += n
}
console.log(n)
console.log(x)

/* 
  Crea un programa que imprima por consola todos los números comprendidos 
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
for (let index = 10; index <= 55; index++) {
  if(index !== 16 && index % 3 !== 0) {
    console.log(index)
  }
}