const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

/*
  * EJERCICIO:
  * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
  * y crea un ejemplo simple donde se muestre su funcionamiento
  * de forma correcta e incorrecta.
*/

// Funcionamiento incorrecto

/*
class ShopVehicles {
  saleBus() {
    console.log('Se ha vendido un Bus')
  }

  saleCar() {
    console.log('Se ha vendido un auto')
  }
}
*/

// Funcionamiento correcto:

class ShopVehicles {
  sale() {
    console.log('Se ha vendido un auto')
  }
}

class saleTruck extends ShopVehicles {
  sale() {
    console.log('Se ha vendido un camión')
  }
}

class saleBus extends ShopVehicles {
  sale() {
    console.log('Se ha vendido un bus')
  }
}

const saleTruck1 = new saleTruck()
saleTruck1.sale()

const saleBus1 = new saleBus()
saleBus1.sale()

/*
  * DIFICULTAD EXTRA (opcional):
  * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
  * Requisitos:
  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
  * Instrucciones:
  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
  * 2. Comprueba que el sistema funciona.
  * 3. Agrega una quinta operación para calcular potencias.
  * 4. Comprueba que se cumple el OCP.
*/

class Calculator {
  operation() { return }
}

class AdditionOperation extends Calculator {
  operation(a, b) {
    return `${a} + ${b} = ${a + b}`
  }
}

class SubtractionOperation extends Calculator {
  operation(a, b) {
    return `${a} - ${b} = ${a - b}`
  }
}

class MultiplyOperation extends Calculator {
  operation(a, b) {
    return `${a} * ${b} = ${a * b}`
  }
}

class DivideOperation extends Calculator {
  operation(a, b) {
    if (b === 0) throw new Error('No se puede dividir por cero')
    return `${a} / ${b} = ${a / b}`
  }
}

class ExponentiationOperation extends Calculator {
  operation(a, b) {
    return `${a} ** ${b} = ${a ** b}`
  }
}

function MenuCalculator() {
  console.log('1 - Sumar')
  console.log('2 - Restar')
  console.log('3 - Multiplicar')
  console.log('4 - Dividir')
  console.log('5 - Potencia')
  console.log('0 - Salir')

  rl.question('Selección: ', (option) => {
    if (option == '1') {
      rl.question('Ingresa el numero A: ', (numberA) => {
        rl.question('Ingresa el numero B: ', (numberB) => {
          const addition = new AdditionOperation()
          console.log(addition.operation(parseInt(numberA), parseInt(numberB)))
          MenuCalculator()
        })
      })
    } else if (option == '2') {
      rl.question('Ingresa el numero A: ', (numberA) => {
        rl.question('Ingresa el numero B: ', (numberB) => {
          const substraction = new SubtractionOperation()
          console.log(substraction.operation(parseInt(numberA), parseInt(numberB)))
          MenuCalculator()
        })
      })
    } else if (option == '3') {
      rl.question('Ingresa el numero A: ', (numberA) => {
        rl.question('Ingresa el numero B: ', (numberB) => {
          const multiply = new MultiplyOperation()
          console.log(multiply.operation(parseInt(numberA), parseInt(numberB)))
          MenuCalculator()
        })
      })
    } else if (option == '4') {
      rl.question('Ingresa el numero A: ', (numberA) => {
        rl.question('Ingresa el numero B: ', (numberB) => {
          const divide = new DivideOperation()
          console.log(divide.operation(parseInt(numberA), parseInt(numberB)))
          MenuCalculator()
        })
      })
    } else if (option == '5') {
      rl.question('Ingresa el numero A: ', (numberA) => {
        rl.question('Ingresa el numero B: ', (numberB) => {
          const exponentiation = new ExponentiationOperation()
          console.log(exponentiation.operation(parseInt(numberA), parseInt(numberB)))
          MenuCalculator()
        })
      })
    } else if (option == '0') {
      rl.close()
    } else {
      console.log('Opción inválida')
      MenuCalculator()
    }
  })
}

MenuCalculator()