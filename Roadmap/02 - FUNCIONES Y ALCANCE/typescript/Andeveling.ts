// Ejemplo de función sin parámetros ni retorno
function saludarAlMundo(): void {
  console.log("¡Hola mundo!")
}

// Ejemplo de función con un parámetro y retorno
function duplicar(numero: number): number {
  return numero * 2
}

// Ejemplo de función con varios parámetros y retorno
function sumar(a: number, b: number): number {
  return a + b
}

// Ejemplo de función dentro de función
function operacionesMatematicas(): void {
  function resta(a: number, b: number): number {
    return a - b
  }

  const resultadoResta = resta(10, 5)
  console.log("Resultado de la resta:", resultadoResta)
}

// Ejemplo de uso de funciones ya creadas en el lenguaje
const arrayEjemplo: number[] = [1, 2, 3, 4, 5]
const sumaArray = arrayEjemplo.reduce((a, b) => a + b, 0)
console.log("Suma del array:", sumaArray)

// Ejemplo de variable local y global
let variableGlobal: number = 100

function mostrarVariableGlobal(): void {
  console.log("Variable global dentro de la función:", variableGlobal)
}

function cambiarVariableGlobal(): void {
  let variableLocal: number = 50
  variableGlobal = variableLocal
  console.log("Variable global cambiada dentro de la función:", variableGlobal)
}

// Llamadas a las funciones
saludarAlMundo()
console.log("Resultado de duplicar(4):", duplicar(4))
console.log("Resultado de sumar(3, 7):", sumar(3, 7))
operacionesMatematicas()
console.log("Variable global fuera de la función:", variableGlobal)
mostrarVariableGlobal()
cambiarVariableGlobal()
console.log("Variable global después de cambiarVariableGlobal:", variableGlobal)

// Funcion que recibe dos paremetros
function cadenasRetornoNumero(fizz: string = "fizz", buzz: string = "buzz"): number {
  if (typeof fizz !== "string" || typeof buzz !== "string") {
    throw new Error("Los argumentos deben ser cadenas de texto")
  }
  let contador = 0
  for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log(fizz + buzz)
      contador++
    } else if (i % 3 === 0) {
      console.log(fizz)
      contador++
    } else if (i % 5 === 0) {
      console.log(buzz)
      contador++
    } else {
      console.log(i)
    }
  }
  return contador
}
