<?php

class GitHubCLI {
    private $workingDirectory;

    public function setWorkingDirectory($dir) {
        if (is_dir($dir)) {
            $this->workingDirectory = realpath($dir);
            echo "Directorio de trabajo establecido en: " . $this->workingDirectory . PHP_EOL;
        } else {
            echo "Error: El directorio no existe." . PHP_EOL;
        }
    }

    public function createRepository($name) {
        if (empty($this->workingDirectory)) {
            echo "Error: Debe establecer un directorio de trabajo primero." . PHP_EOL;
            return;
        }
        exec("cd $this->workingDirectory && git init $name", $output, $return_var);
        if ($return_var === 0) {
            echo "Repositorio '$name' creado." . PHP_EOL;
        } else {
            echo "Error al crear el repositorio." . PHP_EOL;
        }
    }

    public function createBranch($branchName) {
        exec("cd $this->workingDirectory && git checkout -b $branchName", $output, $return_var);
        if ($return_var === 0) {
            echo "Rama '$branchName' creada." . PHP_EOL;
        } else {
            echo "Error al crear la rama." . PHP_EOL;
        }
    }

    public function changeBranch($branchName) {
        exec("cd $this->workingDirectory && git checkout $branchName", $output, $return_var);
        if ($return_var === 0) {
            echo "Cambiado a la rama '$branchName'." . PHP_EOL;
        } else {
            echo "Error al cambiar de rama." . PHP_EOL;
        }
    }

    public function showPendingCommits() {
        exec("cd $this->workingDirectory && git status", $output);
        echo implode(PHP_EOL, $output);
    }

    public function commitChanges($message) {
        exec("cd $this->workingDirectory && git add . && git commit -m \"$message\"", $output, $return_var);
        if ($return_var === 0) {
            echo "Cambios comprometidos con el mensaje: \"$message\"." . PHP_EOL;
        } else {
            echo "Error al hacer commit." . PHP_EOL;
        }
    }

    public function showCommitHistory() {
        exec("cd $this->workingDirectory && git log", $output);
        echo implode(PHP_EOL, $output);
    }

    public function deleteBranch($branchName) {
        exec("cd $this->workingDirectory && git branch -d $branchName", $output, $return_var);
        if ($return_var === 0) {
            echo "Rama '$branchName' eliminada." . PHP_EOL;
        } else {
            echo "Error al eliminar la rama." . PHP_EOL;
        }
    }

    public function setRemoteRepository($url) {
        exec("cd $this->workingDirectory && git remote add origin $url", $output, $return_var);
        if ($return_var === 0) {
            echo "Repositorio remoto establecido en: $url." . PHP_EOL;
        } else {
            echo "Error al establecer el repositorio remoto." . PHP_EOL;
        }
    }

    public function pull() {
        exec("cd $this->workingDirectory && git pull", $output, $return_var);
        if ($return_var === 0) {
            echo "Pull realizado correctamente." . PHP_EOL;
        } else {
            echo "Error al realizar pull." . PHP_EOL;
        }
    }

    public function push() {
        exec("cd $this->workingDirectory && git push origin HEAD", $output, $return_var);
        if ($return_var === 0) {
            echo "Push realizado correctamente." . PHP_EOL;
        } else {
            echo "Error al realizar push." . PHP_EOL;
        }
    }

    public function run() {
        while (true) {
            echo PHP_EOL . "Selecciona una opción:" . PHP_EOL;
            echo "1. Establecer el directorio de trabajo" . PHP_EOL;
            echo "2. Crear un nuevo repositorio" . PHP_EOL;
            echo "3. Crear una nueva rama" . PHP_EOL;
            echo "4. Cambiar de rama" . PHP_EOL;
            echo "5. Mostrar ficheros pendientes de hacer commit" . PHP_EOL;
            echo "6. Hacer commit" . PHP_EOL;
            echo "7. Mostrar el historial de commits" . PHP_EOL;
            echo "8. Eliminar rama" . PHP_EOL;
            echo "9. Establecer repositorio remoto" . PHP_EOL;
            echo "10. Hacer pull" . PHP_EOL;
            echo "11. Hacer push" . PHP_EOL;
            echo "12. Salir" . PHP_EOL;

            $option = (int)readline("Opción: ");

            switch ($option) {
                case 1:
                    $dir = readline("Introduce el directorio de trabajo: ");
                    $this->setWorkingDirectory($dir);
                    break;
                case 2:
                    $name = readline("Introduce el nombre del repositorio: ");
                    $this->createRepository($name);
                    break;
                case 3:
                    $branchName = readline("Introduce el nombre de la nueva rama: ");
                    $this->createBranch($branchName);
                    break;
                case 4:
                    $branchName = readline("Introduce el nombre de la rama a la que deseas cambiar: ");
                    $this->changeBranch($branchName);
                    break;
                case 5:
                    $this->showPendingCommits();
                    break;
                case 6:
                    $message = readline("Introduce el mensaje del commit: ");
                    $this->commitChanges($message);
                    break;
                case 7:
                    $this->showCommitHistory();
                    break;
                case 8:
                    $branchName = readline("Introduce el nombre de la rama a eliminar: ");
                    $this->deleteBranch($branchName);
                    break;
                case 9:
                    $url = readline("Introduce la URL del repositorio remoto: ");
                    $this->setRemoteRepository($url);
                    break;
                case 10:
                    $this->pull();
                    break;
                case 11:
                    $this->push();
                    break;
                case 12:
                    echo "Saliendo..." . PHP_EOL;
                    exit;
                default:
                    echo "Opción no válida." . PHP_EOL;
            }
        }
    }
}

$cli = new GitHubCLI();
$cli->run();
