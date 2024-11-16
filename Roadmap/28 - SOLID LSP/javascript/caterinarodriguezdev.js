/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */

class Ball {
  bounce() {
    console.log('La pelota rebota');
  }
}

class BowlingBall extends Ball {
  bounce() {
    throw new Error('La bola de bolos no puede rebotar')
  }
} 

class BallLSP {
  throw() {
    console.log('Tira la bola');
  }
}

class BowlingBallLSP extends Ball {
  throw() {
    console.log('Tira la bola hacia los bolos');
  }
}

class Vehiculo {
  constructor() {
      this.velocidad = 0;
  }

  acelerar(incremento) {
      this.velocidad += incremento;
      console.log(`Acelerando: Velocidad actual = ${this.velocidad} km/h`);
  }

  frenar(decremento) {
      this.velocidad = Math.max(0, this.velocidad - decremento);
      console.log(`Frenando: Velocidad actual = ${this.velocidad} km/h`);
  }
}

class Coche extends Vehiculo {
  constructor(marca) {
      super();
      this.marca = marca;
  }

  acelerar(incremento) {
      super.acelerar(incremento);
      console.log(`El coche ${this.marca} ha acelerado.`);
  }
}

class Bicicleta extends Vehiculo {
  constructor(tipo) {
      super();
      this.tipo = tipo;
  }

  acelerar(incremento) {
      super.acelerar(incremento);
      console.log(`La bicicleta de tipo ${this.tipo} ha acelerado.`);
  }
}

class Motocicleta extends Vehiculo {
  constructor(modelo) {
      super();
      this.modelo = modelo;
  }

  acelerar(incremento) {
      super.acelerar(incremento);
      console.log(`La motocicleta modelo ${this.modelo} ha acelerado.`);
  }
}

function probarVehiculo(vehiculo) {
  vehiculo.acelerar(20);
  vehiculo.frenar(10);
}

const miCoche = new Coche('Toyota');
const miBicicleta = new Bicicleta('Montaña');
const miMotocicleta = new Motocicleta('Yamaha');

probarVehiculo(miCoche);
probarVehiculo(miBicicleta);
probarVehiculo(miMotocicleta);