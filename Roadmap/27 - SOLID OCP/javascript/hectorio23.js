// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

"use strict";

/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA:
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
*/

class Operacion {
    calcular(a, b) {
        throw new Error('Método calcular debe ser implementado');
    }
}

class Suma extends Operacion {
    calcular(a, b) {
        return a + b;
    }
}

class Resta extends Operacion {
    calcular(a, b) {
        return a - b;
    }
}

class Multiplicacion extends Operacion {
    calcular(a, b) {
        return a * b;
    }
}

class Division extends Operacion {
    calcular(a, b) {
        if (b === 0) {
            throw new Error('División por cero');
        }
        return a / b;
    }
}

class Potencia extends Operacion {
    calcular(a, b) {
        return Math.pow(a, b);
    }
}

class Calculadora {
    constructor() {
        this.operaciones = {};
    }

    agregarOperacion(nombre, operacion) {
        this.operaciones[nombre] = operacion;
    }

    calcular(nombre, a, b) {
        const operacion = this.operaciones[nombre];
        if (!operacion) {
            throw new Error('Operación no soportada');
        }
        return operacion.calcular(a, b);
    }
}

const calc = new Calculadora();
calc.agregarOperacion('+', new Suma());
calc.agregarOperacion('-', new Resta());
calc.agregarOperacion('*', new Multiplicacion());
calc.agregarOperacion('/', new Division());
calc.agregarOperacion('^', new Potencia());

console.log("[+] - Suma:", calc.calcular('+', 5, 3));
console.log("[+] - Resta:", calc.calcular('-', 5, 3));
console.log("[+] - Multiplicación:", calc.calcular('*', 5, 3));
console.log("[+] - División:", calc.calcular('/', 5, 3));
console.log("[+] - Potencia:", calc.calcular('^', 5, 3));
