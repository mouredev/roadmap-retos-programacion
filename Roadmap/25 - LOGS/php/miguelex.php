<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

ini_set('log_errors', 1);
ini_set('error_log', './log.txt');

// Error fatal
if (false) {
    // Este código nunca se ejecutará
    error_log("Este es un ejemplo de mensaje de error fatal", 0);
}

// Advertencia
$result = @file_get_contents('non_existing_file.txt');
if ($result === false) {
    error_log("Este es un ejemplo de mensaje de advertencia", 0);
}

// Notificación
$undefined_var;
error_log("Este es un ejemplo de mensaje de notificación", 0);

// Deprecado
function oldFunction() {
    error_log("Este es un ejemplo de mensaje de función obsoleta", 0);
}

oldFunction();

// 5. Estricto
class MyClass {
    function MyClass() {
        error_log("Este es un ejemplo de mensaje de nivel estricto", 0);
    }
}
$obj = new MyClass();

// 6. Mensaje personalizado
error_log("Este es un ejemplo de mensaje de log personalizado", 0);

echo "Logs enviados al archivo configurado.";


// Extra

class TaskManager {
    private $tasks = [];

    public function addTask($name, $description) {
        $start_time = microtime(true);

        if (isset($this->tasks[$name])) {
            error_log("Advertencia: La tarea '$name' ya existe.", 0);
            return false;
        }

        $this->tasks[$name] = $description;
        error_log("Información: Tarea '$name' añadida.", 0);

        $end_time = microtime(true);
        $execution_time = $end_time - $start_time;
        error_log("Tiempo de ejecución para añadir tarea '$name': $execution_time segundos.", 0);

        return true;
    }

    public function deleteTask($name) {
        $start_time = microtime(true);

        if (!isset($this->tasks[$name])) {
            error_log("Advertencia: La tarea '$name' no existe.", 0);
            return false;
        }

        unset($this->tasks[$name]);
        error_log("Información: Tarea '$name' eliminada.", 0);

        $end_time = microtime(true);
        $execution_time = $end_time - $start_time;
        error_log("Tiempo de ejecución para eliminar tarea '$name': $execution_time segundos.", 0);

        return true;
    }

    public function listTasks() {
        $start_time = microtime(true);

        if (empty($this->tasks)) {
            error_log("Información: No hay tareas para listar.", 0);
            return [];
        }

        $end_time = microtime(true);
        $execution_time = $end_time - $start_time;
        error_log("Tiempo de ejecución para listar tareas: $execution_time segundos.", 0);

        return $this->tasks;
    }
}

$taskManager = new TaskManager();

echo "\n\nEJERCICIO EXTRA\n\n";

function showMenu() {
    echo "\nGestión de Tareas\n";
    echo "1. Añadir tarea\n";
    echo "2. Eliminar tarea\n";
    echo "3. Listar tareas\n";
    echo "4. Salir\n";
    echo "Seleccione una opción: ";
}

function addTask($taskManager) {
    echo "Ingrese el nombre de la tarea: ";
    $name = trim(fgets(STDIN));
    echo "Ingrese la descripción de la tarea: ";
    $description = trim(fgets(STDIN));

    if ($taskManager->addTask($name, $description)) {
        echo "Tarea '$name' añadida con éxito.\n";
    } else {
        echo "Error al añadir la tarea '$name'.\n";
    }
}

function deleteTask($taskManager) {
    echo "Ingrese el nombre de la tarea a eliminar: ";
    $name = trim(fgets(STDIN));

    if ($taskManager->deleteTask($name)) {
        echo "Tarea '$name' eliminada con éxito.\n";
    } else {
        echo "Error al eliminar la tarea '$name'.\n";
    }
}

function listTasks($taskManager) {
    $tasks = $taskManager->listTasks();
    if (empty($tasks)) {
        echo "No hay tareas.\n";
    } else {
        echo "Lista de Tareas:\n";
        foreach ($tasks as $name => $description) {
            echo " - $name: $description\n";
        }
    }
}

while (true) {
    showMenu();
    $choice = trim(fgets(STDIN));

    switch ($choice) {
        case '1':
            addTask($taskManager);
            break;
        case '2':
            deleteTask($taskManager);
            break;
        case '3':
            listTasks($taskManager);
            break;
        case '4':
            echo "Saliendo...\n";
            exit;
        default:
            echo "Opción no válida. Por favor, intente de nuevo.\n";
    }
}



