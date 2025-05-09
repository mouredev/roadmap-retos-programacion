<?php
/*
 * TEORÍA DE CALLBACKS EN PHP:
 * 
 * Un callback en PHP es una función que se pasa como argumento a otra función
 * para ser ejecutada más tarde. PHP ofrece varias formas de implementar callbacks:
 * 
 * 1. Funciones anónimas (closures)
 * 2. Arrays callable ([objeto/clase, método])
 * 3. Strings con nombres de funciones
 * 4. Arrow functions (PHP 7.4+)
 * 
 * Los callbacks son útiles para:
 * 1. Personalizar el comportamiento de funciones
 * 2. Implementar patrones de diseño como Observer
 * 3. Manejar eventos y procesamiento asíncrono (en la medida que PHP lo permite)
 */

// Función de utilidad para simular espera
function simularEspera() {
    $segundos = rand(1, 10);
    echo "Procesando... ({$segundos} segundos)\n";
    sleep($segundos);
}

// Ejemplo simple de callback
function procesarTarea(string $tarea, callable $callback): void {
    echo "Iniciando tarea: {$tarea}\n";
    
    // Simulamos algún procesamiento
    sleep(1);
    
    // Ejecutamos el callback
    $callback();
}

// Clase para el simulador de restaurante
class RestaurantePedidos {
    public function procesarPedido(
        string $plato,
        callable $onConfirmacion,
        callable $onListo,
        callable $onEntrega
    ): void {
        // Callback de confirmación
        $onConfirmacion("Pedido confirmado: {$plato}");
        
        // Simular preparación
        simularEspera();
        
        // Callback de listo
        $onListo("¡{$plato} está listo!");
        
        // Simular entrega
        simularEspera();
        
        // Callback de entrega
        $onEntrega("{$plato} ha sido entregado. ¡Buen provecho!");
    }
}

// Función principal para ejecutar los ejemplos
function main(): void {
    echo "=== Ejemplo Simple de Callback ===\n";
    
    // Ejemplo usando una función anónima
    procesarTarea("Tarea de prueba", function() {
        echo "¡Tarea completada!\n";
    });
    
    echo "\n=== Simulador de Restaurante ===\n";
    
    $restaurante = new RestaurantePedidos();
    
    // Procesamos un pedido usando el simulador
    $restaurante->procesarPedido(
        "Paella Valenciana",
        // Callback de confirmación - usando arrow function (PHP 7.4+)
        fn($mensaje) => echo "CONFIRMACIÓN: {$mensaje}\n",
        // Callback de listo - usando función anónima tradicional
        function($mensaje) {
            echo "LISTO: {$mensaje}\n";
        },
        // Callback de entrega - también usando función anónima
        function($mensaje) {
            echo "ENTREGA: {$mensaje}\n";
        }
    );
}

// Ejecutar el programa
main();

?>