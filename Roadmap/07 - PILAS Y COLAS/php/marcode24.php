<?php

/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

class Stack {
    private $items;

    public function __construct() {
        $this->items = [];
    }

    public function push($element) {
        array_push($this->items, $element);
    }

    public function pop() {
        if ($this->isEmpty()) {
            return 'La pila está vacía';
        }
        return array_pop($this->items);
    }

    public function isEmpty() {
        return empty($this->items);
    }

    public function peek() {
        return end($this->items);
    }

    public function clear() {
        $this->items = [];
    }

    public function size() {
        return count($this->items);
    }
}

class Queue {
    private $items;

    public function __construct() {
        $this->items = [];
    }

    public function enqueue($element) {
        array_push($this->items, $element);
    }

    public function dequeue() {
        if ($this->isEmpty()) {
            return 'La cola está vacía';
        }
        return array_shift($this->items);
    }

    public function isEmpty() {
        return empty($this->items);
    }

    public function size() {
        return count($this->items);
    }
}

$pila = new Stack();
$pila->push(1);
$pila->push(2);
$pila->push(3);
echo $pila->pop() . PHP_EOL; // 3
echo $pila->pop() . PHP_EOL; // 2

$cola = new Queue();
$cola->enqueue('a');
$cola->enqueue('b');
$cola->enqueue('c');
echo $cola->dequeue() . PHP_EOL; // a
echo $cola->dequeue() . PHP_EOL; // b

class Navegador {
    private $history;
    private $future;
    private $currentPage;

    public function __construct() {
        $this->history = new Stack();
        $this->future = new Stack();
        $this->currentPage = null;
    }

    // navegar a una nueva página
    public function goToPage($page) {
        if ($this->currentPage !== null) {
            $this->history->push($this->currentPage);
        }
        $this->currentPage = $page;
        $this->future->clear();
        echo 'Página actual: ' . $this->currentPage . PHP_EOL;
    }

    // retroceder a la página anterior
    public function goBack() {
        if ($this->history->isEmpty()) {
            echo 'No hay páginas anteriores' . PHP_EOL;
            return;
        }
        $this->future->push($this->currentPage);
        $this->currentPage = $this->history->pop();
        echo 'Página actual: ' . $this->currentPage . PHP_EOL;
    }

    // avanzar a la página siguiente
    public function goForward() {
        if ($this->future->isEmpty()) {
            echo 'No hay páginas siguientes' . PHP_EOL;
            return;
        }
        $this->history->push($this->currentPage);
        $this->currentPage = $this->future->pop();
        echo 'Página actual: ' . $this->currentPage . PHP_EOL;
    }
}

$navegador = new Navegador();
$navegador->goToPage('google.com');
$navegador->goToPage('facebook.com');
$navegador->goToPage('twitter.com');
$navegador->goBack(); // regresa a facebook.com
$navegador->goBack(); // regresa a google.com
$navegador->goForward(); // avanza a facebook.com
$navegador->goToPage('instagram.com'); // instagram.com
$navegador->goBack(); // regresa a facebook.com
$navegador->goForward(); // avanza a instagram.com


// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges

?>