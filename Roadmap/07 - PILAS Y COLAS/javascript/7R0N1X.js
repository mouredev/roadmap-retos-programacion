// Pila
var pila = []

pila.push(1)
pila.push(2)
pila.push(3)

// console.log(pila)

pila.pop()

// console.log(pila)

// Cola
var cola = []

cola.push('a')
cola.push('b')
cola.push('c')

// console.log(cola)

cola.shift()

// console.log(cola)

/*
Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
el nombre de una nueva web.
 */

let readline = require('readline')
let rl = readline.createInterface({ input: process.stdin, output: process.stdout })
atras = []
adelante = []


function web_navigation() {

  rl.question('Ingresa una url o interactua con palabras "adelante", "atras" o "salir": ', (answer) => {
    let inputFormat = answer.trim().toLowerCase()

    switch (inputFormat) {
      case 'adelante':
        atras.push(adelante.pop())
        currentPage(atras)
        web_navigation()
        break
      case 'atras':
        if (isEmpty(atras)) {
          currentPage(atras)
          web_navigation()
        } else {
          adelante.push(atras.pop())
          currentPage(atras)
          web_navigation()
        }
        break
      case 'salir':
        rl.close()
        break
      default:
        adelante = []
        atras.push(inputFormat)
        currentPage(atras)
        web_navigation()
        break
    }
  })

}

function isEmpty(pila) {
  return pila.length === 0
}

function currentPage(pila) {
  return isEmpty(pila) ? console.log('Estás en la página de inicio') : console.log(`Estas en la web ${pila[pila.length - 1]}`)
}

// web_navigation()

/*
Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
impresora compartida que recibe documentos y los imprime cuando así se le indica.
La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
interpretan como nombres de documentos.
*/

cola = []

function printer() {

  printQueue(cola)

  rl.question('Ingresa un documento o elige "imprimir" o "salir": ', (answer) => {
    let inputFormat = answer.trim().toLowerCase()

    switch (inputFormat) {
      case 'imprimir':
        if (cola.length === 0) {
          console.log('No hay documentos en cola para imprimir.')
          printer()
        } else {
          console.log(`\n Imprimiendo ${cola.shift()}`)
          printer()
        }
        break
      case 'salir':
        rl.close()
        break
      default:
        cola.push(inputFormat)
        printer()
        break
    }
  })
}

function printQueue(cola) {
  if (cola.length === 0) {
    console.log('\n No hay documentos en cola para imprimir.\n')
  } else {
    console.log(`\n         Cola de impresión`)
    cola.forEach(document => {
      console.log(document)
    })
    console.log('\n')
  }
}

printer()