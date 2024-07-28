/*
  EJERCICIO:
  Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
  y crea un ejemplo simple donde se muestre su funcionamiento
  de forma correcta e incorrecta.
*/

console.log("+++++++++ IMPLEMENTACIÓN INCORRECTA +++++++++");

class IncorrectForm {
  constructor(type) {
    this.type = type;
  }

  calcArea() {
    if (this.type === 'circle') {
      console.log(`Área de círculo π x r²`);
      console.log(`3.1416 * (6 * 6) = ${Math.PI * (6 * 6)}`);
    } else if (this.type === 'rectangle') {
      // Lógica para calcular el área de un rectángulo.
    } else if (this.type === 'triangle') {
      // Lógica para calcular el área de un triángulo.
    }
  }
}

const incorrectForm = new IncorrectForm('circle');
incorrectForm.calcArea();

console.log("\n+++++++++ IMPLEMENTACIÓN CORRECTA +++++++++");

class Form {
  calcArea() {
    throw new Error('Cálculo no implementado');
  }
}

class Circle extends Form {
  calcArea() {
    console.log(`Área de círculo π x r²`);
    console.log(`3.1416 * (6 * 6) = ${Math.PI * (6 * 6)}`);
  }
}

class Triangle extends Form {
  // Lógica para calcular el área de un triángulo.
}

/*
  SI ESTE CÓDIGO SE EJECUTA MOSTRARÁ EL ERROR DEBIDO A QUE LA CLASE TRIANGLE NO TIENE DEFINIDO EL MÉTODO calcArea()

  const triangle = new Triangle();
  triangle.calcArea();
*/

const circle = new Circle();
circle.calcArea();

/*
  DIFICULTAD EXTRA (opcional):
  Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
  Requisitos:
  - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
  Instrucciones:
  1. Implementa las operaciones de suma, resta, multiplicación y división.
  2. Comprueba que el sistema funciona.
  3. Agrega una quinta operación para calcular potencias.
  4. Comprueba que se cumple el OCP.
*/

console.log("\n+++++++++ CALCULADORA +++++++++");

class OperationValidation {
  operation() {
    throw new Error (`La operación ${this.constructor.name} no existe`);
  }
}

class Calculator {
  showResult(operationData) {
    const operationName = operationData[0];
    const value1 = operationData[1];
    const value2 = operationData[2];
    const result = operationData[3];

    console.log(`La ${operationName} de los valores ${value1} y ${value2} es: ${result}`);
  }
}

class Addition extends OperationValidation {
  operation(a, b) {
    const operationType = "Suma";

    return [operationType, a, b, a + b];
  }
}

class Substraction extends OperationValidation {
  operation(a, b) {
    const operationType = "Resta";

    return [operationType, a, b, a - b];
  }
}

class Multiplication extends OperationValidation {
  operation(a, b) {
    const operationType = "Multiplicación";

    return [operationType, a, b, a * b];
  }
}

class Division extends OperationValidation {
  operation(a, b) {
    const operationType = "División";

    return [operationType, a, b, a / b];
  }
}

class Power extends OperationValidation {
  operation(a, b) {
    const operationType = "Potencia";

    return [operationType, a, b, a ** b];
  }
}

const calculator = new Calculator();
const addition = new Addition();
const substraction = new Substraction();
const multiplication = new Multiplication();
const division = new Division();
const power = new Power();

calculator.showResult(addition.operation(1, 2));
calculator.showResult(substraction.operation(3, 4));
calculator.showResult(multiplication.operation(5, 6));
calculator.showResult(division.operation(7, 8));
calculator.showResult(power.operation(9, 10));
