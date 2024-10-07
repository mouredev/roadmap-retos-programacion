<?php

/**
 * Clase para manejar tareas asíncronas
 */
class TareaAsincrona {
    private $nombre;
    private $segundos;
    private $pid;

    /**
     * Constructor de la clase
     * @param string $nombre Nombre de la tarea
     * @param int $segundos Duración de la tarea en segundos
     */
    public function __construct($nombre, $segundos) {
        $this->nombre = $nombre;
        $this->segundos = $segundos;
    }

    /**
     * Ejecuta la tarea de forma asíncrona
     * @return bool True si la tarea se inició correctamente
     */
    public function ejecutar() {
        // Crear un proceso hijo
        $pid = pcntl_fork();
        
        if ($pid == -1) {
            die("No se pudo crear el proceso hijo\n");
        } else if ($pid) {
            // Proceso padre
            $this->pid = $pid;
            return true;
        } else {
            // Proceso hijo
            echo "{$this->nombre} - Iniciando...\n";
            echo "{$this->nombre} - Durará {$this->segundos} segundos\n";
            sleep($this->segundos);
            echo "{$this->nombre} - Finalizada\n";
            exit(0);
        }
    }

    /**
     * Espera a que la tarea termine
     */
    public function esperar() {
        if ($this->pid) {
            pcntl_waitpid($this->pid, $status);
        }
    }
}

/**
 * Demostración básica de una tarea asíncrona
 */
function demostracionBasica() {
    echo "=== Demostración Básica ===\n";
    $tarea = new TareaAsincrona("TareaEjemplo", 2);
    $tarea->ejecutar();
    $tarea->esperar();
}

/**
 * Implementación de la dificultad extra
 */
function dificultadExtra() {
    echo "\n=== Dificultad Extra ===\n";
    
    // Crear las tareas
    $tareaC = new TareaAsincrona("Tarea C", 3);
    $tareaB = new TareaAsincrona("Tarea B", 2);
    $tareaA = new TareaAsincrona("Tarea A", 1);
    $tareaD = new TareaAsincrona("Tarea D", 1);

    // Ejecutar C, B y A en paralelo
    $tareaC->ejecutar();
    $tareaB->ejecutar();
    $tareaA->ejecutar();

    // Esperar a que terminen C, B y A
    $tareaC->esperar();
    $tareaB->esperar();
    $tareaA->esperar();

    // Ejecutar D después de que las otras hayan terminado
    $tareaD->ejecutar();
    $tareaD->esperar();
}

// Función principal
function main() {
    demostracionBasica();
    dificultadExtra();
}

// Ejecutar el programa
main();

?>