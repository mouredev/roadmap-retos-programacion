<?php
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
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