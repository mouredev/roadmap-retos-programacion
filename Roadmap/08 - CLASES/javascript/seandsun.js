/*
<-------------- Clases -------------->
Básicamente una clase es una manera en la que podemos organizar o gestionar nustro código con el objetivo de simplificar
el funcionamiento de nuestros programas y que nuestro código se pueda leer y entender de una mejor manera.
*/

// Declaración de una clase. La primera letra del nombre debe ir en mayúscula.
class Deporte {

  // Constructor: solo puede haber uno, se encarga de inicializar o crear las propiedades que contiene en los objetos creados a partir de esta clase.
  constructor(nombre) {       
    this.nombre = nombre    // Propiedad sin definir (undefined), se recibirá su valor como parámetro al crear el objeto.
    this.tipo = "Acuático"  // Propiedad definida, o sea que será igual para todos los objetos creados. Se puede moficar después.
  }

  // Métodos: son como funciones pero sin la palabra "function"
  velocidad() {
    return "Va muy rápido."
  }

  print() {
    return `${this.nombre} - ${this.tipo} - ${this.velocidad()}`
  }
} 

// Instanciar o crear un objeto de la clase Deporte, esto nos permitirá trabajar con sus propiedades y métodos
const nuevoDeporte = new Deporte("Natación") // nuevoDeporte = {nombre: "Natación", tipo: "Acuático"}
console.log(nuevoDeporte.print());           // 'Natación - Acuático - Va muy rápido.'
nuevoDeporte.nombre = "Paracaidismo"         // Modifico el valor del atributo "nombre"
nuevoDeporte.tipo = "Aéreo"                  // Modifico el valor del atributo "tipo"
console.log(nuevoDeporte.print());           // 'Paracaidismo - Aéreo - Va muy rápido.' 


/*
<-------------- Palabra clave: this -------------->
Esta palabra clave se utiliza bastante dentro de las clases para hacer referencia al OBJETO INSTANCIADO, más no a la clase.
*/

class Arbol {

  constructor(nombre) {
    this.nombre = nombre // "this" hace referencia al "nombre" del "objeto instanciado"
    // nuevoArbol.nombre = "cerezo"    
  }

  /*
  Fuera de la clase instanciamos el objeto "nuevoArbol" de la clase "Arbol", por lo tanto la palabra "this" haría
  referencia a "nuevoArbol", en otras palabras "this.nombre" estaría haciendo referencia a "nuevoArbol.nombre"
  */
}

const nuevoArbol = new Arbol('cerezo')
console.log(nuevoArbol.nombre); // cerezo 


// <-------------- Clase Pila -------------->
// Last In, First Out

class Pila {

  constructor() {
    this.elementos = []
  }

  insertar = (elemento) => {
    this.elementos.push(elemento)
    return this.elementos
  }

  Eliminar = () => {
    return this.elementos.pop()
  }

  largo = () => {
    return this.elementos.length
  }

  imprimir = () => {
    return this.elementos
  }
}

const pila = new Pila() 

pila.insertar("Amarillo")
pila.insertar("Azul")
pila.insertar("Verde")
console.log(pila.largo()) // 3
console.log(pila.imprimir()); // [ 'Amarillo', 'Azul', 'Verde' ]
pila.Eliminar()
pila.Eliminar()
pila.Eliminar()
console.log(pila.imprimir()); //  []


// <-------------- Clase Colas -------------->
// First In, First Out

class Cola {
  
  constructor() {
    this.elementos = []
  }
  
  insertar = (elemento) => {
    this.elementos.splice(0, 0, elemento)
    return this.elementos
  }

  Eliminar = () => {
    return this.elementos.pop()
  }

  largo = () => {
    return this.elementos.length
  }

  imprimir = () => {
    return this.elementos
  }
}

const cola = new Cola()

cola.insertar("Amarillo")
cola.insertar("Azul")
cola.insertar("Verde")
console.log(cola.largo()) // 3
console.log(cola.imprimir()); // [ 'Verde', 'Azul', 'Amarillo' ]
cola.Eliminar()
cola.Eliminar()
cola.Eliminar()
console.log(cola.imprimir()); // []