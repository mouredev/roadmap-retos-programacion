<?php

// Implementación de la Pila (Stack - LIFO)
class Stack {
    private $items = [];

    // Método para añadir un elemento a la pila
    public function push($element) {
        array_push($this->items, $element);
    }

    // Método para quitar un elemento de la pila
    public function pop() {
        if ($this->isEmpty()) {
            echo "Error: Pila vacía\n";
            return null;
        }
        return array_pop($this->items);
    }

    // Método para verificar si la pila está vacía
    public function isEmpty() {
        return empty($this->items);
    }

    // Método para obtener el elemento en la cima de la pila sin quitarlo
    public function peek() {
        if ($this->isEmpty()) {
            echo "Error: Pila vacía\n";
            return null;
        }
        return end($this->items);
    }
}

// Implementación de la Cola (Queue - FIFO)
class Queue {
    private $items = [];

    // Método para añadir un elemento a la cola
    public function enqueue($element) {
        array_push($this->items, $element);
    }

    // Método para quitar un elemento de la cola
    public function dequeue() {
        if ($this->isEmpty()) {
            echo "Error: Cola vacía\n";
            return null;
        }
        return array_shift($this->items);
    }

    // Método para verificar si la cola está vacía
    public function isEmpty() {
        return empty($this->items);
    }

    // Método para obtener el primer elemento de la cola sin quitarlo
    public function peek() {
        if ($this->isEmpty()) {
            echo "Error: Cola vacía\n";
            return null;
        }
        return $this->items[0];
    }
}

// Función para el simulador de navegador web
function webBrowserSimulator() {
    $backStack = new Stack();
    $forwardStack = new Stack();
    $currentPage = "";

    echo "Simulador de navegador web (escribe 'salir' para terminar):\n";

    while (true) {
        $input = strtolower(trim(readline("Ingresa una acción o nombre de página web: ")));

        if ($input === 'salir') {
            break;
        } elseif ($input === 'atrás') {
            if (!$backStack->isEmpty()) {
                $forwardStack->push($currentPage);
                $currentPage = $backStack->pop();
                echo "Página actual: $currentPage\n";
            } else {
                echo "No hay páginas anteriores\n";
            }
        } elseif ($input === 'adelante') {
            if (!$forwardStack->isEmpty()) {
                $backStack->push($currentPage);
                $currentPage = $forwardStack->pop();
                echo "Página actual: $currentPage\n";
            } else {
                echo "No hay páginas siguientes\n";
            }
        } else {
            if ($currentPage !== "") {
                $backStack->push($currentPage);
            }
            $forwardStack = new Stack();  // Limpia la pila de adelante
            $currentPage = $input;
            echo "Página actual: $currentPage\n";
        }
    }
}

// Función para el simulador de impresora compartida
function printerSimulator() {
    $printQueue = new Queue();

    echo "\nSimulador de impresora compartida (escribe 'salir' para terminar):\n";

    while (true) {
        $input = strtolower(trim(readline("Ingresa un nombre de documento o 'imprimir': ")));

        if ($input === 'salir') {
            break;
        } elseif ($input === 'imprimir') {
            $document = $printQueue->dequeue();
            if ($document !== null) {
                echo "Imprimiendo: $document\n";
            }
        } else {
            $printQueue->enqueue($input);
            echo "Documento añadido a la cola: $input\n";
        }
    }
}

// Ejecutar los simuladores
webBrowserSimulator();
printerSimulator();

?>