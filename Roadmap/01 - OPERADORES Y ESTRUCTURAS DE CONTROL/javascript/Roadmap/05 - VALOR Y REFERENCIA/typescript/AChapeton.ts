//Variables por Valor

let a: string = 'Hola Mundo'
let b: string = a //El valor de "a" se asigna a "b"

a += '!' //Se modifica el valor de "a"

console.log("a", a)
console.log("b", b)


//Variables por Referencia
//Con estructuras, no se crea un nuevo valor, sino que ambas variables apuntan a un mismo espacio en memoria

const c = [1, 2, 3]
const d = c

c.push(4)

console.log('c', c)
console.log('d', d)


//Funciones utilizando Variables por Valor


const firstFunction = (str: string) => {
  str = 'nuevo valor dentro de la funcion'
  return str
}

const strOriginal: string = 'Fuera de la funcion'
console.log('Por valor - Dentro de la funcion: ', firstFunction(strOriginal))
console.log('Por valor - Fuera de la funcion: ', strOriginal)


//Funciones utilizando Varibles por Referencia

const secondFunction = (arr: Array<string>) => {
  arr.push('Moure')
  return arr
}

const arrOriginal: Array<string> = ['Andres', 'Brais', 'Chape']
console.log('Por referencia - Dentro de la funcion: ', secondFunction(arrOriginal))
console.log('Por referencia - Fuera de la funcion: ', arrOriginal)


// EJERCICIO EXTRA

//Funcion para intercarbiar variables por valor

const intercambiarValor = (num1: number, num2: number): [number, number] => {
  const temp: number = num1
  num1 = num2
  num2 = temp
  return [num1, num2]
}

let primerValor: number = 10
let segundoValor: number = 5

console.group('Valores antes del intercambio')
  console.log('primerValor: ', primerValor)
  console.log('segundoValor: ', segundoValor)
console.groupEnd()

let [nuevoPrimerValor, nuevoSegundoValor] = intercambiarValor(primerValor, segundoValor)

console.group('Valores despues del intercambio')
  console.log('primerValor: ', primerValor)
  console.log('segundoValor: ', segundoValor)
console.groupEnd()

console.group('Nuevos valores intercambiados')
  console.log('nuevoPrimerValor: ', nuevoPrimerValor)
  console.log('nuevoSegundoValor: ', nuevoSegundoValor)
console.groupEnd()


//Funcion para intercarbiar variables por referecia

interface Usuario {
  name: string,
  mainEmail: string,
  secondEmail: string
}

const intercambiarReferencias = (user: Usuario): Usuario => {
  let temp: string = user.mainEmail
  user.mainEmail = user.secondEmail
  user.secondEmail = temp

  return user
}

let usuarioOriginal: Usuario = {
  name: 'Andres',
  mainEmail: 'andres@new.com',
  secondEmail: 'andres@test.com',
}

console.group('Referencias antes del intercambio')
  console.log('usuarioOriginal: ', usuarioOriginal)
console.groupEnd()

let nuevoUsuario: Usuario = intercambiarReferencias(usuarioOriginal)

console.group('Referencias despues del intercambio')
  console.log('usuarioOriginal: ', usuarioOriginal)
console.groupEnd()

console.group('Nuevas Referencias intercambiadas')
  console.log('nuevoUsuario: ', nuevoUsuario)
console.groupEnd()