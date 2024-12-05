/*
  * EJERCICIO:
  * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)"
  * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
*/

// Forma incorrecta
/*
  class Animal {
    fly() {
      console.log("Volar")
    }

    swim() {
      console.log("Nadar")
    }

    walk() {
      console.log("Caminar")
    }
  }

  class Bird extends Animal {
    fly() {
      console.log("Volar")
    }
  }

  class Fish extends Animal {
    swim() {
      console.log("Nadar")
    }
  }

  class Dog extends Animal {
    walk() {
      console.log("Caminar")
    }
    fly() {
      throw new Error("No puede volar")
    }
  }

  const bird = new Bird()
  bird.fly()

  const fish = new Fish()
  fish.swim()

  const dog = new Dog()
  dog.walk()

  dog.fly()
*/

// Forma correcta

class AnimalCanFly {
  fly() {
    console.log("Volar")
  }
}

class AnimalCanSwim {
  swim() {
    console.log("Nadar")
  }
}

class AnimalCanWalk {
  walk() {
    console.log("Caminar")
  }
}

class Bird extends AnimalCanFly {
  fly() {
    console.log("Volar")
  }
}

class Fish extends AnimalCanSwim {
  swim() {
    console.log("Nadar")
  }
}

class Dog extends AnimalCanWalk {
  walk() {
    console.log("Caminar")
  }
}

const bird = new Bird()
const fish = new Fish()
const dog = new Dog()

bird.fly()
fish.swim()
dog.walk()

/*
  * DIFICULTAD EXTRA (opcional):
  * Crea un gestor de impresoras.
  * Requisitos:
  * 1. Algunas impresoras sólo imprimen en blanco y negro.
  * 2. Otras sólo a color.
  * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
  * Instrucciones:
  * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
  * 2. Aplica el ISP a la implementación.
  * 3. Desarrolla un código que compruebe que se cumple el principio.
*/

class Printable {
  print(document) {
    console.log(`Printing ${document}`)
  }
}

class Scannable {
  scan(document) {
    console.log(`Scanning ${document}`)
  }
}

class Faxable {
  sendFax(document) {
    console.log(`Sending ${document}`)
  }
}

class BlackAndWhitePrinter extends Printable {}
class ColorPrinter extends Printable {}
class MultifunctionalPrinter extends Printable {
  constructor() {
    super()
    this.scanner = new Scannable()
    this.fax = new Faxable()
  }

  scan(document) {
    this.scanner.scan(document)
  }

  sendFax(document) {
    this.fax.sendFax(document)
  }
}

const bwPrinter = new BlackAndWhitePrinter()
bwPrinter.print("Document1")

const colorPrinter = new ColorPrinter()
colorPrinter.print("Document2")

const multiPrinter = new MultifunctionalPrinter()
multiPrinter.print("Document3")
multiPrinter.scan("Document3")
multiPrinter.sendFax("Document3")