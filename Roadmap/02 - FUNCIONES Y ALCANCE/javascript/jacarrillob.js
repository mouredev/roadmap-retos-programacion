// Ejemplo de función sin parámetros ni retorno
function handleGreet () {
  console.log('¡Hola! Bienvenido.')
}

// Ejemplo de función con un parámetro y sin retorno
function handleShowMessage (message) {
  console.log(message)
}

// Ejemplo de función con múltiples parámetros y con retorno
const handleSum = (a, b) => {
  return a + b
}

// Ejemplo de función dentro de otra función
function handleMathematicalOperations (a, b) {
  function sum () {
    return a + b
  }
  function subtraction () {
    return a - b
  }
  console.log('Suma:', sum())
  console.log('Resta:', subtraction())
}

// Ejemplo de variable global
let globalVariable = 'José'

function handleGreetGlobally () {
  console.log('Hola,', globalVariable)
}

// Ejemplo de variable local
function handleGreetLocally () {
  let localVariable = 'Pepito'
  console.log('Hola,', localVariable)
}

// Ejemplo de función integrada en JavaScript
let list = [1, 2, 3, 4, 5]

function handlePrintLengthArray () {
  console.log('Longitud de la lista:', list.length)
}

// Llamadas a las funciones
handleGreet()
handleShowMessage('Este es un mensaje de prueba.')
console.log('Resultado de la suma:', handleSum(5, 3))
handleMathematicalOperations(10, 5)
handleGreetGlobally()
handleGreetLocally()
handlePrintLengthArray()

console.log('\n ***EXTRA***\n')

function handlePrintNumbersWithText (text1, text2) {
    let contador = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(`${text1} - ${text2}`)
        } else if (i % 3 === 0) {
            console.log(text1)

        } else if (i % 5 === 0) {
            console.log(text2)
        } else {
            console.log(i)
            contador++
        }
    }

    return contador
}

const timesPrinted = handlePrintNumbersWithText('Uno', 'Dos')
console.log('Número de veces impreso: ', timesPrinted)

