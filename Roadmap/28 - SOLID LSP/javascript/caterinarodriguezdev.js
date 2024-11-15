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

