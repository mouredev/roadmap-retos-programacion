<?php

    // Clases en PHP
    class Vehiculo{
        // Atributos
        private $nombre;
        private $numRuedas;

        // Constructor
        public function __construct($nombre, $numRuedas){
            $this->nombre = $nombre;
            $this->numRuedas = $numRuedas;
        }

        // Método mágico __toString
        public function __toString(){
            return "Nombre: " . $this->nombre . " - Ruedas: " . $this->numRuedas;
        }
    }

    $coche = new Vehiculo("Coche", 4); // Instanciamos un objeto de la clase Vehiculo
    $bicicleta = new Vehiculo("Bicicleta", 2);

    echo $coche . "\n"; // Llamamos al método __toString para imprimir el contenido del objeto
    echo $bicicleta . "\n";

    // Extra

    class Stack {
        private $stack = array();

        public function __construct($item){
            $this->push($item);
        }

        public function push($item){
            array_push($this->stack, $item);
        }

        public function pop(){
            return array_pop($this->stack);
        }

        public function numElements(){
            return count($this->stack);
        }

        public function __toString(){
            return implode(", ", $this->stack);
        }
    }

    // Ejemplo de uso de la clase Stack
    $stack = new Stack(1); // Instanciamos un objeto de la clase Stack
    
    // añadimos dos elementos mas a la pila
    $stack->push(2);
    $stack->push(3);

    // Mostramos el contenido de la pila
    echo "El contenido actual de la pila es: ".$stack . "\n";
    echo "Extraemos el elemeto ".$stack->pop() . " que es el que esta en la cima de la pila\n";
    echo "La pila tiene un total de ".$stack->numElements() . " elementos\n";
    echo "Volvemos a mostrar el contenido de la pila: ".$stack . "\n";

    class Queue {
        private $queue = array();

        public function __construct($item){
            $this->enqueue($item);
        }

        public function enqueue($item){
            array_push($this->queue, $item);
        }

        public function dequeue(){
            return array_shift($this->queue);
        }

        public function numElements(){
            return count($this->queue);
        }

        public function __toString(){
            return implode(", ", $this->queue);
        }
    }


    // Ejemplo de uso de la clase Queue
    $queue = new Queue(1); // Instanciamos un objeto de la clase Queue
    
    // añadimos tres elementos a la cola
    $queue->enqueue(2);
    $queue->enqueue(3);
    $queue->enqueue(4);

    // Mostramos el contenido de la cola
    echo "El contenido actual de la cola es: ".$queue . "\n";
    echo "Extraemos el elemeto ".$queue->dequeue() . " que es el que esta en la cabeza de la cola\n";
    echo "La cola tiene un total de ".$queue->numElements() . " elementos\n";
    echo "Volvemos a mostrar el contenido de la cola: ".$queue . "\n";
    




