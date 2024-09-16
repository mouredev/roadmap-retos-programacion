/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 */

// Forma incorrecta
class Form {
  constructor(name) {
    this.name = name;
  }

  calcName() {
    if (this.name === "Hernan") {
      return `Hola Hernan...!`;
    } else if (this.name === "Agustin") {
      return "Hola Agustin...!";
    } else {
      return `Chau ${this.name}`;
    }
  }
}

const form = new Form("Hernan");
form.calcName();

// Forma correcta
class Form {
  calcName() {
    throw new Error("Metodo no implementado");
  }
}

class Saludo1 extends Form {
  calcName() {
    return "Hola Hernan...!";
  }
}

class Saludo2 extends Form {
  calcName() {
    return "Hola Agustin";
  }
}

class Saludo3 extends Form {
  calcName() {
    return `Hola ${this.name}`;
  }
}

const saludo = new Saludo1();
saludo.calcName();

/* DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */
class Calculadora {
  constructor() {
    this.operations = {};
  }

  agregarOperacion(nombre, operacion) {
    this.operations[nombre] = operacion;
  }

  calculate(nombre, a, b) {
    return this.operations[nombre].execute(a, b);
  }
}

class Operation {
  execute(a, b) {
    throw new Error("Método no implementado");
  }
}

class Sumar extends Operation {
  execute(a, b) {
    return a + b;
  }
}

class Restar extends Operation {
  execute(a, b) {
    return a - b;
  }
}

class Multiplicar extends Operation {
  execute(a, b) {
    return a * b;
  }
}

class Dividir extends Operation {
  execute(a, b) {
    if (a === 0) {
      throw new Error("Error!, No se puede divir por 0.");
    }
    return a / b;
  }
}

const calculadora = new Calculadora();
calculadora.agregarOperacion("sumar", new Sumar());
calculadora.agregarOperacion("restar", new Restar());
calculadora.agregarOperacion("multiplicar", new Multiplicar());
calculadora.agregarOperacion("dividir", new Dividir());

console.log(calculadora.calculate("sumar", 10, 5));
