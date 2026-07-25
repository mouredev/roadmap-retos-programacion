<?php
/**
 * TEORÍA SOBRE LOGGING EN PHP
 * 
 * PHP proporciona varias formas de implementar logging:
 * 1. error_log() - Función nativa de PHP para logging
 * 2. syslog() - Para logging en el sistema operativo
 * 3. file_put_contents() - Para escribir logs en archivos
 * 4. Librerías como Monolog - Soluciones más completas
 * 
 * Niveles de severidad estándar (PSR-3):
 * - EMERGENCY: Sistema inutilizable
 * - ALERT: Acción inmediata requerida
 * - CRITICAL: Condiciones críticas
 * - ERROR: Condiciones de error
 * - WARNING: Condiciones de advertencia
 * - NOTICE: Eventos normales pero significativos
 * - INFO: Mensajes informativos
 * - DEBUG: Información detallada de depuración
 */

/**
 * Clase Logger personalizada para manejar diferentes niveles de logging
 */
class Logger {
    private string $logFile;
    
    public function __construct(string $logFile = 'app.log') {
        $this->logFile = $logFile;
    }
    
    /**
     * Método privado para escribir el log
     */
    private function writeLog(string $level, string $message): void {
        $timestamp = date('Y-m-d H:i:s');
        $logMessage = "[$timestamp] [$level] $message" . PHP_EOL;
        
        // Escribir en archivo
        file_put_contents($this->logFile, $logMessage, FILE_APPEND);
        
        // También mostrar en consola para este ejemplo
        echo $logMessage;
    }
    
    public function emergency(string $message): void {
        $this->writeLog('EMERGENCY', $message);
    }
    
    public function alert(string $message): void {
        $this->writeLog('ALERT', $message);
    }
    
    public function critical(string $message): void {
        $this->writeLog('CRITICAL', $message);
    }
    
    public function error(string $message): void {
        $this->writeLog('ERROR', $message);
    }
    
    public function warning(string $message): void {
        $this->writeLog('WARNING', $message);
    }
    
    public function notice(string $message): void {
        $this->writeLog('NOTICE', $message);
    }
    
    public function info(string $message): void {
        $this->writeLog('INFO', $message);
    }
    
    public function debug(string $message): void {
        $this->writeLog('DEBUG', $message);
    }
}

/**
 * Clase que representa una Tarea
 */
class Task {
    public function __construct(
        public string $name,
        public string $description,
        public DateTime $createdAt
    ) {}
}

/**
 * Clase para la gestión de tareas con logging integrado
 */
class TaskManager {
    private array $tasks = [];
    private Logger $logger;
    
    public function __construct(Logger $logger) {
        $this->logger = $logger;
    }
    
    /**
     * Añade una nueva tarea al sistema
     */
    public function addTask(string $name, string $description): void {
        $startTime = microtime(true);
        
        try {
            // Verificar si ya existe una tarea con el mismo nombre
            foreach ($this->tasks as $task) {
                if ($task->name === $name) {
                    $this->logger->error("La tarea '$name' ya existe");
                    return;
                }
            }
            
            $task = new Task($name, $description, new DateTime());
            $this->tasks[] = $task;
            
            $this->logger->info("Tarea '$name' añadida exitosamente");
            
            $endTime = microtime(true);
            $executionTime = ($endTime - $startTime) * 1000; // Convertir a millisegundos
            $this->logger->debug("Tiempo de ejecución addTask: {$executionTime}ms");
            
        } catch (Exception $e) {
            $this->logger->error("Error al añadir tarea: " . $e->getMessage());
        }
    }
    
    /**
     * Elimina una tarea por su nombre
     */
    public function removeTask(string $name): void {
        $startTime = microtime(true);
        
        try {
            $initialCount = count($this->tasks);
            $this->tasks = array_filter(
                $this->tasks,
                fn($task) => $task->name !== $name
            );
            
            if (count($this->tasks) === $initialCount) {
                $this->logger->warning("No se encontró la tarea '$name'");
            } else {
                $this->logger->info("Tarea '$name' eliminada exitosamente");
            }
            
            $endTime = microtime(true);
            $executionTime = ($endTime - $startTime) * 1000;
            $this->logger->debug("Tiempo de ejecución removeTask: {$executionTime}ms");
            
        } catch (Exception $e) {
            $this->logger->error("Error al eliminar tarea: " . $e->getMessage());
        }
    }
    
    /**
     * Lista todas las tareas existentes
     */
    public function listTasks(): void {
        $startTime = microtime(true);
        
        try {
            if (empty($this->tasks)) {
                $this->logger->info("No hay tareas registradas");
                return;
            }
            
            $this->logger->info("Lista de tareas:");
            foreach ($this->tasks as $task) {
                $createdAt = $task->createdAt->format('Y-m-d H:i:s');
                $this->logger->info("- {$task->name}: {$task->description} (Creada: $createdAt)");
            }
            
            $endTime = microtime(true);
            $executionTime = ($endTime - $startTime) * 1000;
            $this->logger->debug("Tiempo de ejecución listTasks: {$executionTime}ms");
            
        } catch (Exception $e) {
            $this->logger->error("Error al listar tareas: " . $e->getMessage());
        }
    }
}

// Ejemplo de uso del sistema
function main() {
    // Crear instancia del logger
    $logger = new Logger('tareas.log');
    $logger->info("Iniciando sistema de gestión de tareas");
    
    // Crear instancia del gestor de tareas
    $taskManager = new TaskManager($logger);
    
    // Demostrar diferentes niveles de logging
    $logger->emergency("Ejemplo de mensaje emergency");
    $logger->alert("Ejemplo de mensaje alert");
    $logger->critical("Ejemplo de mensaje critical");
    $logger->error("Ejemplo de mensaje error");
    $logger->warning("Ejemplo de mensaje warning");
    $logger->notice("Ejemplo de mensaje notice");
    $logger->info("Ejemplo de mensaje info");
    $logger->debug("Ejemplo de mensaje debug");
    
    // Ejemplos de uso del gestor de tareas
    $taskManager->addTask("Estudiar PHP", "Aprender sobre logging y POO");
    $taskManager->addTask("Hacer ejercicio", "30 minutos de cardio");
    $taskManager->listTasks();
    $taskManager->removeTask("Estudiar PHP");
    $taskManager->listTasks();
    $taskManager->removeTask("Tarea inexistente");
    
    $logger->info("Finalizando sistema de gestión de tareas");
}

// Ejecutar el programa
main();