var readline = require('readline')

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})
/*
  * EJERCICIO:
  * Implementa los mecanismos de introducción y recuperación de elementos propios de las
  * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
  * o lista (dependiendo de las posibilidades de tu lenguaje).
*/

//Pilas LIFO
class Lifo {
  list: (number | string)[] = []
  adding(data: number | string): void {
    this.list.push(data)
  }
  removing(): void {
    this.list.pop()
  }
}

const myLifo: Lifo = new Lifo
myLifo.adding(1)
myLifo.adding(2)
myLifo.adding(3)
myLifo.removing()
console.log(myLifo)

// Colas FIFO

class Fifo {
  list: (number | string)[] = []
  adding(data: number | string): void {
    this.list.push(data)
  }
  removing(): void {
    this.list.shift()
  }
}

const myFifo: Fifo = new Fifo
myFifo.adding(1)
myFifo.adding(2)
myFifo.adding(3)
myFifo.removing()
console.log(myFifo)

/*
  * DIFICULTAD EXTRA (opcional):
  * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
  *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
  *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
  *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
  *   el nombre de una nueva web.
  * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
  *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
  *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
  *   interpretan como nombres de documentos.
*/

function webNavigator(): void {
  const list: Array<string> = []
  rl.question('Ingresa el nombre de una web, "adelante", "atrás" o "salir": ', (response: string) => {
    if (response === 'atrás' && list.length > 0) {
      list.pop()
    } else if (response !== 'adelante' && response !== 'salir' && response !== 'atrás') {
      list.push(response)
    }
    if (response === 'salir') {
      rl.close()
    } else {
      console.log(`Página actual: ${list[list.length - 1] || "Inicio"}`)
      webNavigator()
    }
  })
}
webNavigator()

const printerList: Array<string> = []
function printer(): void {
  console.log('list', printerList)
  rl.question('Ingresa imprimir o un nombre de documento: ', (response: string) => {
    if (response === 'imprimir') {
      console.log(printerList[0])
      printerList.shift()
      printer()
    } else if (response !== 'imprimir') {
      printerList.push(response)
      printer()
    } else {
      console.log('opcion incorrecta')
      rl.close()
    }
  })
}

printer()