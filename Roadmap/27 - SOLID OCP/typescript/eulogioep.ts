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
    calculate(a: number, b: number, operation: string): number {
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
// Definimos una interfaz para las operaciones
interface Operation {
    execute(a: number, b: number): number;
    getSymbol(): string;
}

// Implementamos cada operación como una clase separada
class Addition implements Operation {
    execute(a: number, b: number): number {
        return a + b;
    }
    getSymbol(): string {
        return '+';
    }
}

class Subtraction implements Operation {
    execute(a: number, b: number): number {
        return a - b;
    }
    getSymbol(): string {
        return '-';
    }
}

class Multiplication implements Operation {
    execute(a: number, b: number): number {
        return a * b;
    }
    getSymbol(): string {
        return '*';
    }
}

class Division implements Operation {
    execute(a: number, b: number): number {
        if (b === 0) throw new Error('No se puede dividir por cero');
        return a / b;
    }
    getSymbol(): string {
        return '/';
    }
}

// Podemos agregar nuevas operaciones sin modificar el código existente
class Power implements Operation {
    execute(a: number, b: number): number {
        return Math.pow(a, b);
    }
    getSymbol(): string {
        return '^';
    }
}

// La calculadora que cumple con OCP
class Calculator {
    private operations: Map<string, Operation>;

    constructor() {
        this.operations = new Map();
    }

    // Método para registrar nuevas operaciones
    registerOperation(operation: Operation): void {
        this.operations.set(operation.getSymbol(), operation);
    }

    // Método para realizar cálculos
    calculate(a: number, b: number, symbol: string): number {
        const operation = this.operations.get(symbol);
        if (!operation) {
            throw new Error(`Operación ${symbol} no soportada`);
        }
        return operation.execute(a, b);
    }
}

// Ejemplo de uso
function main() {
    // Creamos una instancia de la calculadora
    const calculator = new Calculator();

    // Registramos las operaciones básicas
    calculator.registerOperation(new Addition());
    calculator.registerOperation(new Subtraction());
    calculator.registerOperation(new Multiplication());
    calculator.registerOperation(new Division());

    // Probamos las operaciones básicas
    console.log('2 + 3 =', calculator.calculate(2, 3, '+'));
    console.log('5 - 2 =', calculator.calculate(5, 2, '-'));
    console.log('4 * 3 =', calculator.calculate(4, 3, '*'));
    console.log('8 / 2 =', calculator.calculate(8, 2, '/'));

    // Agregamos una nueva operación (potencia) sin modificar el código existente
    calculator.registerOperation(new Power());
    
    // Probamos la nueva operación
    console.log('2 ^ 3 =', calculator.calculate(2, 3, '^'));
}

// Ejecutamos el programa
main();

/*
 * EXPLICACIÓN DE POR QUÉ ESTE DISEÑO CUMPLE CON OCP:
 * 
 * 1. ABIERTO PARA EXTENSIÓN:
 *    - Podemos agregar nuevas operaciones creando nuevas clases que implementen la interfaz Operation
 *    - No necesitamos modificar ninguna clase existente
 *    - Cada operación está encapsulada en su propia clase
 * 
 * 2. CERRADO PARA MODIFICACIÓN:
 *    - La clase Calculator no necesita ser modificada para agregar nuevas operaciones
 *    - El código existente permanece intacto cuando agregamos nuevas funcionalidades
 *    - La interfaz Operation define un contrato claro que no cambia
 * 
 * 3. VENTAJAS DE ESTE DISEÑO:
 *    - Fácil de mantener y extender
 *    - Cada operación está aislada y puede ser probada independientemente
 *    - Reduce el acoplamiento entre componentes
 *    - Facilita la adición de nuevas operaciones sin riesgo de afectar las existentes
 */