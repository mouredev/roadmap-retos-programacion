<?php
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
    public function calculate(float $a, float $b, string $operation): float {
        switch ($operation) {
            case 'sum':
                return $a + $b;
            case 'subtract':
                return $a - $b;
            case 'multiply':
                return $a * $b;
            case 'divide':
                return $a / $b;
            // Si queremos agregar una nueva operación, debemos modificar esta clase
            // violando el principio OCP
            default:
                throw new Exception('Operación no soportada');
        }
    }
}

// EJEMPLO CORRECTO (Siguiendo OCP)
// Definimos una interfaz para las operaciones
interface Operation {
    public function execute(float $a, float $b): float;
    public function getSymbol(): string;
}

// Implementamos cada operación como una clase separada
class Addition implements Operation {
    public function execute(float $a, float $b): float {
        return $a + $b;
    }

    public function getSymbol(): string {
        return '+';
    }
}

class Subtraction implements Operation {
    public function execute(float $a, float $b): float {
        return $a - $b;
    }

    public function getSymbol(): string {
        return '-';
    }
}

class Multiplication implements Operation {
    public function execute(float $a, float $b): float {
        return $a * $b;
    }

    public function getSymbol(): string {
        return '*';
    }
}

class Division implements Operation {
    public function execute(float $a, float $b): float {
        if ($b === 0.0) {
            throw new Exception('No se puede dividir por cero');
        }
        return $a / $b;
    }

    public function getSymbol(): string {
        return '/';
    }
}

// Podemos agregar nuevas operaciones sin modificar el código existente
class Power implements Operation {
    public function execute(float $a, float $b): float {
        return pow($a, $b);
    }

    public function getSymbol(): string {
        return '^';
    }
}

// La calculadora que cumple con OCP
class Calculator {
    private array $operations;

    public function __construct() {
        $this->operations = [];
    }

    // Método para registrar nuevas operaciones
    public function registerOperation(Operation $operation): void {
        $this->operations[$operation->getSymbol()] = $operation;
    }

    // Método para realizar cálculos
    public function calculate(float $a, float $b, string $symbol): float {
        if (!isset($this->operations[$symbol])) {
            throw new Exception("Operación $symbol no soportada");
        }
        return $this->operations[$symbol]->execute($a, $b);
    }
}

// Ejemplo de uso
try {
    // Creamos una instancia de la calculadora
    $calculator = new Calculator();

    // Registramos las operaciones básicas
    $calculator->registerOperation(new Addition());
    $calculator->registerOperation(new Subtraction());
    $calculator->registerOperation(new Multiplication());
    $calculator->registerOperation(new Division());

    // Probamos las operaciones básicas
    echo "2 + 3 = " . $calculator->calculate(2, 3, '+') . PHP_EOL;
    echo "5 - 2 = " . $calculator->calculate(5, 2, '-') . PHP_EOL;
    echo "4 * 3 = " . $calculator->calculate(4, 3, '*') . PHP_EOL;
    echo "8 / 2 = " . $calculator->calculate(8, 2, '/') . PHP_EOL;

    // Agregamos una nueva operación (potencia) sin modificar el código existente
    $calculator->registerOperation(new Power());
    
    // Probamos la nueva operación
    echo "2 ^ 3 = " . $calculator->calculate(2, 3, '^') . PHP_EOL;

    // Probamos un error (división por cero)
    echo "5 / 0 = " . $calculator->calculate(5, 0, '/') . PHP_EOL;
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}

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
 * 
 * 4. DIFERENCIAS CON LA VERSIÓN TYPESCRIPT:
 *    - Uso de array asociativo en lugar de Map
 *    - Manejo de tipos flotantes en lugar de number
 *    - Uso de try-catch para el manejo de excepciones
 *    - Sintaxis específica de PHP para declaración de tipos
 */