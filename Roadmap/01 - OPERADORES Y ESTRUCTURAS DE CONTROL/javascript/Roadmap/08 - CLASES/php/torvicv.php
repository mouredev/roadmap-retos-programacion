<?php

class Pila {

    private $pila;

    private $attribute1;
    private $attribute2;

    public function __construct(array $pila, int $attribute1, string $attribute2)
    {
        $this->pila = $pila;
        $this->attribute1 = $attribute1;
        $this->attribute2 = $attribute2;
    }

    public function getPila(): array {
        return $this->pila;
    }

    public function getPilaString(): string {
        return json_encode($this->pila);
    }

    public function getAttribute1(): int {
        return $this->attribute1;
    }

    public function getAttribute2(): string {
        return $this->attribute2;
    }

    public function setPila(array $pila) {
        $this->pila = $pila;
    }

    public function setAttribute1(int $attribute1) {
        $this->attribute1 = $attribute1;
    }

    public function setAttribute2(string $attribute2) {
        $this->attribute2 = $attribute2;
    }

    public function __toString(): string
    {
        return 'pila: ' . json_encode($this->pila) . 
        ', attribute1: ' . $this->attribute1 . 
        ', attribute2: ' . $this->attribute2;
    }
}

$pila1 = new Pila([1, 2, 3, 4, 5], 1, 'world');

echo $pila1->__toString().'<br />';

echo $pila1->getPilaString().'<br />';

echo $pila1->getAttribute1().'<br />';

echo $pila1->getAttribute2().'<br />';

$pila1->setPila(['hello', 'world']);

$pila1->setAttribute1(2);

$pila1->setAttribute2('bye');

echo $pila1->__toString().'<br />';

echo $pila1->getPilaString().'<br />';

echo $pila1->getAttribute1().'<br />';

echo $pila1->getAttribute2().'<br />';

/**
 * Clase para la dificultad extra.
 */
class PilaOpt {

    private $pila;

    public function __construct(array $pila)
    {
        $this->pila = $pila;
    }

    public function getPila(): array {
        return $this->pila;
    }

    public function getPilaString(): string {
        return json_encode($this->pila);
    }

    public function setPila(array $pila) {
        $this->pila = $pila;
    }

    /**
     * Método para introducir un elemento en la pila.
     */
    public function push($element) {
        array_push($this->pila, $element);
    }

    /**
     * Método para eliminar un elemento de la pila.
     * Último en entrar, primero en salir.
     */
    public function pop() {
        return array_pop($this->pila);
    }

    /**
     * Método para conseguir la cantidad de elementos.
     */
    public function counter() {
        return count($this->pila);
    }

    public function __toString(): string
    {
        return 'pila: ' . json_encode($this->pila);
    }
}

$pilaOpt = new PilaOpt([1, 2, 3]);

echo 'Mostramos los elementos del array: '.$pilaOpt->getPilaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(3): '.$pilaOpt->counter();

echo 'Añadimos un nuevo elemento al array.<br />';

$pilaOpt->push(4);

echo 'Mostramos los elementos del array: '.$pilaOpt->getPilaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(4): '.$pilaOpt->counter();

echo 'Eliminamos el último elemento del array que se introdujo(4): '.$pilaOpt->pop().'<br />';

echo 'Mostramos los elementos del array: '.$pilaOpt->getPilaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(3): '.$pilaOpt->counter();

echo 'Eliminamos el último elemento del array que se introdujo(3): '.$pilaOpt->pop().'<br />';

echo 'Mostramos los elementos del array: '.$pilaOpt->getPilaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(2): '.$pilaOpt->counter();

/**
 * Clase para la dificultad extra.
 */
class ColaOpt {

    private $cola;

    public function __construct(array $cola)
    {
        $this->cola = $cola;
    }

    public function getCola(): array {
        return $this->cola;
    }

    public function getcolaString(): string {
        return json_encode($this->cola);
    }

    public function setCola(array $cola) {
        $this->cola = $cola;
    }

    /**
     * Método para introducir un elemento en la pila.
     */
    public function push($element) {
        array_push($this->cola, $element);
    }

    /**
     * Método para eliminar un elemento de la pila.
     * Último en entrar, primero en salir.
     */
    public function shift() {
        return array_shift($this->cola);
    }

    public function counter() {
        return count($this->cola);
    }

    public function __toString(): string
    {
        return 'cola: ' . json_encode($this->cola);
    }
}

$colaOpt = new ColaOpt([1, 2, 3]);

echo 'Mostramos los elementos del array: '.$colaOpt->getcolaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(3): '.$colaOpt->counter();

echo 'Añadimos un nuevo elemento al array.<br />';

$colaOpt->push(4);

echo 'Mostramos los elementos del array: '.$colaOpt->getcolaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(4): '.$colaOpt->counter();

echo 'Eliminamos el primer elemento del array que se introdujo(1): '.$colaOpt->shift().'<br />';

echo 'Mostramos los elementos del array: '.$colaOpt->getcolaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(3): '.$colaOpt->counter();

echo 'Eliminamos el segundo elemento del array que se introdujo(2): '.$colaOpt->shift().'<br />';

echo 'Mostramos los elementos del array: '.$colaOpt->getcolaString().'<br />';

echo 'Mostramos la cantidad de elementos en la pila(2): '.$colaOpt->counter();

?>