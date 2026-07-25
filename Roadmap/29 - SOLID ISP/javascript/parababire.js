// Incorrecto

/* class Animal {
  constructor(name) {
    this.name = name
    if (new.target === Animal) {
      throw new Error('Animal es una interface y no puede ser instanciada')
    }
    if (!this.eat) {
      throw new Error('Debe implimentar el método eat')
    }
    if (!this.fly) {
      throw new Error('Debe implimentar el método fly')
    }
    if (!this.swim) {
      throw new Error('Debe implimentar el método swim')
    }
  }
}

class Fish extends Animal {
  eat() {
    console.log(`${this.name} is eating`)
  }
  swim() {
    console.log(`${this.name} is swimming`)
  }
  fly() {
    console.error("ERROR! Fishes can't fly")
  }
}

class Bird extends Animal {
  eat() {
    console.log(`${this.name} is eating`)
  }
  swim() {
    console.error("ERROR! Birds can't swim");
  }
  fly() {
    console.log(`${this.name} is flying`)
  }
}

const bird = new Bird('Titi the Parrot');
bird.swim(); // ERROR! Birds can't swim

const fish = new Fish('Neo the Dolphin');
fish.fly(); // ERROR! Fishes can't fly
 */
// Correcto

class Swimmer {
  constructor(name) {
    this.name = name
    if (new.target === Swimmer) {
      throw new Error('Swimmer es una interface y no puede ser instanciada')
    }
    if (!this.swim) {
      throw new Error('Debe implimentar el método swim')
    }
  }
}

class Flyer {
  constructor(name) {
    this.name = name
    if (new.target === Flyer) {
      throw new Error('Flyer es una interface y no puede ser instanciada')
    }
    if (!this.fly) {
      throw new Error('Debe implimentar el método eat')
    }
  }
}

// Implement interfaces for specific types of animals

class Bird extends Flyer {
  constructor(name) {
    super(name);
  }
  fly() {
    console.log(`${this.name} is flying`);
  }
  eat() {
    console.log(`${this.name} is eating`);
  }
}

class Fish extends Swimmer {
  constructor(name) {
    super(name);
  }
  swim() {
    console.log(`${this.name} is swimming`);
  }
  eat() {
    console.log(`${this.name} is eating`);
  }
}

// Usage

const bird = new Bird('Titi the Parrot');
bird.fly(); // Titi the Parrot is flying
bird.eat(); // Titi the Parrot is eating

console.log('\n');

const fish = new Fish('Neo the Dolphin');
fish.swim(); // Neo the Dolphin is swimming
fish.eat(); // Neo the Dolphin is eating

// Extra

class Printer {
  constructor() {
    if (new.target === Printer) {
      throw new Error("Printer es una interface no puedes instanciarla.")
    }
    if (!this.print) {
      throw new Error("Debes implementar el método print")
    }
  }
}

class BlackAndWhitePrinter extends Printer {
  print() {
    console.log("Se imprime en blanco y negro.")
  }
}

class ColorPrinter extends Printer {
  print() {
    console.log("Se imprime a color.")
  }
}

const sendingFax = {
  sendFax() {
    console.log("Enviando fax.")
  }
}

const scanner = {
  scanning() {
    console.log("Escaneando documento.")
  }
}

Object.assign(ColorPrinter.prototype, sendingFax)
Object.assign(ColorPrinter.prototype, scanner)

const multifuncional = new ColorPrinter()
multifuncional.print()
multifuncional.sendFax()
multifuncional.scanning()

function testInterface(object, interface) {
  const prototypeProperties = Object.getOwnPropertyNames(interface.prototype)

  for (const method of prototypeProperties) {
    if (!object[method] || typeof object[method] !== 'function') {
      throw new Error(`La clase no implementa el método ${method} de la interface.`)
  }
  }
}
testInterface(multifuncional, Printer)