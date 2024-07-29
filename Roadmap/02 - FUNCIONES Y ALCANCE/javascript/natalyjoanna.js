
// Funcion basica

function greet() {
  console.log("Hello, World!");
}

greet()

// Funcion que resive parametros sin retorno

function greetPerson(name) {
  console.log("Hello, " + name)
}

greetPerson("Nataly")

// funcion con un parametro y retorno

function pares(num) {
  let res 
  if(num%2==0) {
    res = true
  } else (
    res = false
  )
  return res
}

let num = 10102
let respuesta = pares(num)
if (respuesta==true) { console.log("El nuemro es par"); } else { console.log("El numero es impar") }

// Funcion con retorno y varios parametros

function suma(a,b) {
  return a + b
}

let a = 23
let b = 22
const total = suma(a,b)
console.log("Suma: ", total)

// Funcion dentro de funcion

function calculadora(a,b) {

  function resta() {
    return a-b
  }

  function multiplicacion() {
    return a*b
  }

  function division() {
    return a/b
  }

  return {
    resta: resta(),
    multiplicacion: multiplicacion(),
    division: division()
  }

}

const resultados = calculadora(a,b)
console.log("Resta: ", resultados.resta)
console.log("Multiplicacion: ", resultados.multiplicacion)
console.log("Division: ", resultados.division)

// Funcion de javascript

const fecha = new Date()
const dia = fecha.getDate()
const mes = fecha.getMonth()
const año = fecha.getFullYear()
const formatoFecha = `${dia}/${mes}/${año}` 
console.log("La fecha actual es: ", formatoFecha)

// DIFICULTAD EXTRA

function imprimirMensaje(texto01, texto02) {
  let count = 0
  for(let num=1; num<=100;num++){
    if(num%3==0 && num%5==0){
      console.log(`${texto01} ${texto02}`)
    } else if (num%3==0){
      console.log(texto01)
    } else if(num%5==0) {
      console.log(texto02)
    } else {
      console.log(num)
      count++
    }
  }
  return count
}

let impresion = imprimirMensaje("Hola", "Adios")
console.log("Las veces que se imprimio un numero fueron: ", impresion)