<?php

/**
 * TEORÍA DE DECORADORES (ATRIBUTOS) EN PHP
 * 
 * En PHP 8.0+ los decoradores se implementan como "Atributos" y permiten añadir
 * metadatos a las clases, métodos, propiedades y parámetros.
 * 
 * Los atributos en PHP:
 * - Se definen como clases con el atributo #[Attribute]
 * - Se aplican usando la sintaxis #[NombreAtributo]
 * - Pueden recibir parámetros en su constructor
 * - Se pueden consultar usando la API de Reflection
 */

// Ejemplo 1: Decorador simple para una clase
#[Attribute]
class LogClass {
    public function __construct(public string $message = "") {}
}

// Ejemplo 2: Decorador para métodos que registra la ejecución
#[Attribute]
class LogMethod {
    public function __construct(public string $message = "") {}
}

// Ejemplo 3: Decorador contador de llamadas (para el ejercicio extra)
#[Attribute]
class ContadorLlamadas {
    private static array $contadores = [];
    
    public static function incrementar(string $metodo): int {
        if (!isset(self::$contadores[$metodo])) {
            self::$contadores[$metodo] = 0;
        }
        self::$contadores[$metodo]++;
        return self::$contadores[$metodo];
    }
}

// Clase de ejemplo con decoradores
#[LogClass("Esta es una clase de ejemplo")]
class Ejemplo {
    #[LogMethod("Método de saludo")]
    public function saludar(string $nombre): string {
        return "¡Hola $nombre!";
    }
}

// Clase Calculadora con el decorador contador
class Calculadora {
    #[ContadorLlamadas]
    public function sumar(int $a, int $b): int {
        return $a + $b;
    }

    #[ContadorLlamadas]
    public function multiplicar(int $a, int $b): int {
        return $a * $b;
    }
}

// Clase Helper para procesar los decoradores
class DecoratorHelper {
    // Método para procesar decoradores de clase
    public static function processClassDecorators(string $className): void {
        $reflection = new ReflectionClass($className);
        $attributes = $reflection->getAttributes();
        
        foreach ($attributes as $attribute) {
            if ($attribute->getName() === LogClass::class) {
                $instance = $attribute->newInstance();
                echo "Clase {$className} creada: {$instance->message}\n";
            }
        }
    }

    // Método para procesar decoradores de método
    public static function processMethodDecorators(string $className, string $methodName): void {
        $reflection = new ReflectionMethod($className, $methodName);
        $attributes = $reflection->getAttributes();
        
        foreach ($attributes as $attribute) {
            if ($attribute->getName() === LogMethod::class) {
                $instance = $attribute->newInstance();
                echo "Método {$methodName} llamado: {$instance->message}\n";
            } elseif ($attribute->getName() === ContadorLlamadas::class) {
                $contador = ContadorLlamadas::incrementar($className . "::" . $methodName);
                echo "El método {$methodName} ha sido llamado {$contador} veces\n";
            }
        }
    }
}

// Clase Proxy para interceptar llamadas y procesar decoradores
class CalculadoraProxy {
    private Calculadora $calculadora;

    public function __construct() {
        $this->calculadora = new Calculadora();
    }

    public function __call(string $method, array $arguments) {
        DecoratorHelper::processMethodDecorators(Calculadora::class, $method);
        return $this->calculadora->$method(...$arguments);
    }
}

// Código de prueba
echo "=== Pruebas de los decoradores ===\n";

// Prueba del decorador de clase
DecoratorHelper::processClassDecorators(Ejemplo::class);

// Prueba del decorador de método
$ejemplo = new Ejemplo();
DecoratorHelper::processMethodDecorators(Ejemplo::class, 'saludar');
echo $ejemplo->saludar("PHP") . "\n";

// Prueba del decorador contador
$calc = new CalculadoraProxy();
echo "Resultado suma: " . $calc->sumar(5, 3) . "\n";      // Primera llamada a sumar
echo "Resultado suma: " . $calc->sumar(2, 4) . "\n";      // Segunda llamada a sumar
echo "Resultado multiplicación: " . $calc->multiplicar(3, 4) . "\n";  // Primera llamada a multiplicar
echo "Resultado suma: " . $calc->sumar(1, 1) . "\n";      // Tercera llamada a sumar