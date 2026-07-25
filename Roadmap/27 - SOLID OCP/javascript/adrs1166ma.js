/* 🔥 EJERCICIO:
Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.
*/
console.log("----- EJEMPLO SIMPLE -----");

//  * Ejemplo Incorrecto: Clase no extensible sin modificar código existente
// --------------------------------------------------------------------------------------------------------------
class CalculadoraIncorrecta {
    calcular(operacion, a, b) {
        switch(operacion) {
            case 'suma':
                return a + b;
            case 'resta':
                return a - b;
            default:
                throw new Error("Operación no soportada.");
        }
    }
}

// Uso incorrecto
const calcIncorrecta = new CalculadoraIncorrecta();
console.log("Suma (incorrecto):", calcIncorrecta.calcular('suma', 5, 3)); // 8
console.log("Resta (incorrecto):", calcIncorrecta.calcular('resta', 5, 3)); // 2
// ¡Problema!: Para añadir "multiplicación", debemos editar la clase CalculadoraIncorrecta

//  * Ejemplo Correcto: Clases abiertas para extensión
// --------------------------------------------------------------------------------------------------------------
class Operacion {
    ejecutar(a, b) {
        throw new Error("Operación no implementada.");
    }
}

class Suma extends Operacion {
    ejecutar(a, b) {
        return a + b;
    }
}

class Resta extends Operacion {
    ejecutar(a, b) {
        return a - b;
    }
}

class CalculadoraCorrecta {
    constructor(operacion) {
        this.operacion = operacion;
    }

    calcular(a, b) {
        return this.operacion.ejecutar(a, b);
    }
}

// Uso correcto
const suma = new Suma();
const resta = new Resta();
const calcSuma = new CalculadoraCorrecta(suma);
const calcResta = new CalculadoraCorrecta(resta);

console.log("Suma (correcto):", calcSuma.calcular(5, 3)); // 8
console.log("Resta (correcto):", calcResta.calcular(5, 3)); // 2

// Nueva operación sin modificar clases existentes
class Multiplicacion extends Operacion {
    ejecutar(a, b) {
        return a * b;
    }
}

const multiplicacion = new Multiplicacion();
const calcMultiplicacion = new CalculadoraCorrecta(multiplicacion);
console.log("Multiplicación (correcto):", calcMultiplicacion.calcular(5, 3)); // 15

// --------------------------------------------------------------------------------------------------------------
/* 🔥 DIFICULTAD EXTRA (opcional):
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.
*/
console.log("\n----- SISTEMA DE CALCULADORA EXTENSIBLE -----");

class OperacionBase {
    ejecutar(a, b) {
        throw new Error("Operación no implementada.");
    }
}

class SumaOp extends OperacionBase {
    ejecutar(a, b) { return a + b; }
}

class RestaOp extends OperacionBase {
    ejecutar(a, b) { return a - b; }
}

class MultiplicacionOp extends OperacionBase {
    ejecutar(a, b) { return a * b; }
}

class DivisionOp extends OperacionBase {
    ejecutar(a, b) {
        if (b === 0) throw new Error("División por cero.");
        return a / b;
    }
}

class Calculadora {
    constructor() {
        this.operaciones = {};
    }

    registrarOperacion(nombre, operacion) {
        this.operaciones[nombre] = operacion;
    }

    calcular(operacion, a, b) {
        if (!this.operaciones[operacion]) {
            throw new Error(`Operación "${operacion}" no registrada.`);
        }
        return this.operaciones[operacion].ejecutar(a, b);
    }
}

// Registrar operaciones iniciales
const calc = new Calculadora();
calc.registrarOperacion('suma', new SumaOp());
calc.registrarOperacion('resta', new RestaOp());
calc.registrarOperacion('multiplicacion', new MultiplicacionOp());
calc.registrarOperacion('division', new DivisionOp());

// Ejemplos de uso
console.log("Suma:", calc.calcular('suma', 10, 5)); // 15
console.log("Resta:", calc.calcular('resta', 10, 5)); // 5
console.log("Multiplicación:", calc.calcular('multiplicacion', 10, 5)); // 50
console.log("División:", calc.calcular('division', 10, 5)); // 2

//  * Agregar nueva operación (OCP cumplido)
// --------------------------------------------------------------------------------------------------------------
class Potencia extends OperacionBase {
    ejecutar(a, b) {
        return Math.pow(a, b);
    }
}

// Registrar potencia sin modificar la clase Calculadora
calc.registrarOperacion('potencia', new Potencia());
console.log("Potencia:", calc.calcular('potencia', 2, 3)); // 8