/*
 * PRINCIPIO ABIERTO-CERRADO (OCP)
 * 
 * El principio establece que las entidades de software (clases, módulos, funciones, etc.) 
 * deberían estar:
 * - ABIERTAS para la extensión: Podemos agregar nuevo comportamiento
 * - CERRADAS para la modificación: No debemos modificar el código existente
 * 
 * Beneficios:
 * 1. Código más mantenible y escalable
 * 2. Reduce el riesgo de bugs en código existente
 * 3. Facilita la adición de nuevas funcionalidades
 */

// EJEMPLO INCORRECTO (Violando OCP)
// ❌ Cada vez que queremos agregar una nueva operación, debemos modificar la clase existente
class BadCalculator {
    calculate(a, b, operation) {
        switch (operation) {
            case 'sum':
                return a + b;
            case 'subtract':
                return a - b;
            case 'multiply':
                return a * b;
            case 'divide':
                return a / b;
            // Si queremos agregar una nueva operación, debemos modificar esta clase
            // violando el principio OCP
            default:
                throw new Error('Operación no soportada');
        }
    }
}

// EJEMPLO CORRECTO (Siguiendo OCP)
// Definimos una clase base para las operaciones
class Operation {
    execute(a, b) {
        throw new Error('Método execute debe ser implementado');
    }

    getSymbol() {
        throw new Error('Método getSymbol debe ser implementado');
    }
}

// Implementamos cada operación como una clase separada
class Addition extends Operation {
    execute(a, b) {
        return a + b;
    }

    getSymbol() {
        return '+';
    }
}

class Subtraction extends Operation {
    execute(a, b) {
        return a - b;
    }

    getSymbol() {
        return '-';
    }
}

class Multiplication extends Operation {
    execute(a, b) {
        return a * b;
    }

    getSymbol() {
        return '*';
    }
}

class Division extends Operation {
    execute(a, b) {
        if (b === 0) {
            throw new Error('No se puede dividir por cero');
        }
        return a / b;
    }

    getSymbol() {
        return '/';
    }
}

// Podemos agregar nuevas operaciones sin modificar el código existente
class Power extends Operation {
    execute(a, b) {
        return Math.pow(a, b);
    }

    getSymbol() {
        return '^';
    }
}

// La calculadora que cumple con OCP
class Calculator {
    constructor() {
        this.operations = new Map();
    }

    // Método para registrar nuevas operaciones
    registerOperation(operation) {
        if (!(operation instanceof Operation)) {
            throw new Error('La operación debe ser una instancia de Operation');
        }
        this.operations.set(operation.getSymbol(), operation);
    }

    // Método para realizar cálculos
    calculate(a, b, symbol) {
        const operation = this.operations.get(symbol);
        if (!operation) {
            throw new Error(`Operación ${symbol} no soportada`);
        }
        return operation.execute(a, b);
    }

    // Método para listar operaciones disponibles
    getAvailableOperations() {
        return Array.from(this.operations.keys());
    }
}

// Clase para formatear los resultados
class ResultFormatter {
    static format(a, b, symbol, result) {
        return `${a} ${symbol} ${b} = ${result}`;
    }
}

// Ejemplo de uso con manejo de errores
function runCalculatorDemo() {
    try {
        // Creamos una instancia de la calculadora
        const calculator = new Calculator();

        // Registramos las operaciones básicas
        calculator.registerOperation(new Addition());
        calculator.registerOperation(new Subtraction());
        calculator.registerOperation(new Multiplication());
        calculator.registerOperation(new Division());

        // Mostramos las operaciones disponibles
        console.log('Operaciones disponibles:', calculator.getAvailableOperations());

        // Probamos las operaciones básicas
        const testCases = [
            { a: 2, b: 3, symbol: '+' },
            { a: 5, b: 2, symbol: '-' },
            { a: 4, b: 3, symbol: '*' },
            { a: 8, b: 2, symbol: '/' }
        ];

        testCases.forEach(({ a, b, symbol }) => {
            const result = calculator.calculate(a, b, symbol);
            console.log(ResultFormatter.format(a, b, symbol, result));
        });

        // Agregamos una nueva operación (potencia) sin modificar el código existente
        calculator.registerOperation(new Power());
        console.log('\nNueva operación agregada:');
        console.log(ResultFormatter.format(2, 3, '^', calculator.calculate(2, 3, '^')));

        // Probamos el manejo de errores
        console.log('\nProbando manejo de errores:');
        console.log(ResultFormatter.format(5, 0, '/', calculator.calculate(5, 0, '/')));
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// Ejecutamos la demostración
runCalculatorDemo();

/*
 * EXPLICACIÓN DE POR QUÉ ESTE DISEÑO CUMPLE CON OCP:
 * 
 * 1. ABIERTO PARA EXTENSIÓN:
 *    - Podemos agregar nuevas operaciones creando nuevas clases que extiendan de Operation
 *    - No necesitamos modificar ninguna clase existente
 *    - Cada operación está encapsulada en su propia clase
 * 
 * 2. CERRADO PARA MODIFICACIÓN:
 *    - La clase Calculator no necesita ser modificada para agregar nuevas operaciones
 *    - El código existente permanece intacto cuando agregamos nuevas funcionalidades
 *    - La clase base Operation define un contrato claro que no cambia
 * 
 * 3. VENTAJAS DE ESTE DISEÑO:
 *    - Fácil de mantener y extender
 *    - Cada operación está aislada y puede ser probada independientemente
 *    - Reduce el acoplamiento entre componentes
 *    - Facilita la adición de nuevas operaciones sin riesgo de afectar las existentes
 * 
 * 4. CARACTERÍSTICAS ESPECÍFICAS DE LA IMPLEMENTACIÓN EN JAVASCRIPT:
 *    - Uso de clases ES6
 *    - Uso de Map para almacenar las operaciones
 *    - Validación de tipos en tiempo de ejecución
 *    - Clase auxiliar para formateo de resultados
 *    - Manejo de errores con try-catch
 *    - Uso de métodos estáticos y arrow functions
 */