/**
 * <-------------- Pilas -------------->
 * En javascript de manera nativa NO existen las pilas como tal, pero sí podemos hacer uso de los arrays para crearlas.
 * Una pila es una estructura de datos que únicamente nos permite introducir datos en la cima o parte superior; del
 * mismo modo, para eliminar datos únicamente lo podemos hacer por la cima o parte superior. Por tales motivos es más
 * conocida como una estructura LIFO (Last In, First Out), o sea, el último en entrar, es el primero en salir.
*/

class Pila {
  elementos = [] // Este array simulará ser una pila

  insertar = (elemento) => { // Inserta un elemento en la parte superior de la pila
    this.elementos.push(elemento)
    return this.elementos
  }

  Eliminar = () => { // Elimina un elemento de la parte superior de la pila
    return this.elementos.pop()
  }

  cima = () => { // Indica cuál es el último elemento de la pila
    return this.elementos[this.elementos.length-1]
  }

  estaVacio = () => { // Comprueba si la pila está vacía
    return this.elementos.length === 0
  }

  largo = () => { // Indica el número de elementos que contiene la pila
    return this.elementos.length
  }
}

let pila = new Pila() // Creo una instancia de la clase Pila para poder usar sus métodos

console.log(pila.estaVacio()) // true
console.log(pila.insertar("Amarillo")) // [ 'Amarillo' ]
console.log(pila.insertar("Azul")) // [ 'Amarillo', 'Azul' ]
console.log(pila.insertar("Verde")) // [ 'Amarillo', 'Azul', 'Verde' ]
console.log(pila.estaVacio()) // false
console.log(pila.largo()) // 3
console.log(pila.cima()) // Verde
console.log(pila.Eliminar()) // Verde
console.log(pila.Eliminar()) // Azul
console.log(pila.Eliminar()) // Amarillo

/**
 * <-------------- Colas -------------->
 * En javascript de manera nativa NO existen las colas como tal, pero sí podemos hacer uso de los arrays para crearlas.
 * Una cola es una estructura de datos que únicamente nos permite introducir datos al final, o sea después del último dato 
 * ingresado; por el contrario, para eliminar datos únicamente lo podemos hacer por el principio o inicio de la cola. Por tales
 * motivos es más conocida como una estructura FIFO (First In, First Out), o sea, el primero en entrar, es el primero en salir.
*/

class Cola {
  elementos = [] // Este array simulará ser una cola

  insertar = (elemento) => { // Inserta un elemento al final de la cola
    this.elementos.splice(0, 0, elemento)
    return this.elementos
  }

  Eliminar = () => { // Elimina un elemento del principio o inicio de la cola
    return this.elementos.pop()
  }

  estaVacio = () => { // Comprueba si la cola está vacía
    return this.elementos.length === 0
  }

  largo = () => { // Indica el número de elementos que contiene la cola
    return this.elementos.length
  }
}

let cola = new Cola() // Creo una instancia de la clase Cola para poder usar sus métodos

console.log(cola.estaVacio()) // true
console.log(cola.insertar("Amarillo")) // [ 'Amarillo' ]
console.log(cola.insertar("Azul")) // [ 'Azul', 'Amarillo' ]
console.log(cola.insertar("Verde")) // [ 'Verde', 'Azul', 'Amarillo' ]
console.log(cola.estaVacio()) // false
console.log(cola.largo()) // 3
console.log(cola.Eliminar()) // Amarillo
console.log(cola.Eliminar()) // Azul
console.log(cola.Eliminar()) // Verde