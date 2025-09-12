<?php

// Ejercicio Básico

class Rectangle {
    public $width;
    public $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }
}

class Circle {
    public $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }
}

class AreaCalculator {
    public function calculate($shapes) {
        $area = 0;
        foreach ($shapes as $shape) {
            if ($shape instanceof Rectangle) {
                echo "\nEl area del rectangulo es: ". $shape->width * $shape->height;
            } elseif ($shape instanceof Circle) {
                echo "\nEl area del circulo es: ". pi() * $shape->radius * $shape->radius;
            }
        }
    }
}

$shapes = [
    new Rectangle(5, 10),
    new Circle(7)
];

echo "Ejercicio básico (sin cumplir OCP)";
$calculator = new AreaCalculator();
echo $calculator->calculate($shapes);

// El problema de esta solución es que si ahroa creamos una clase triangle (por ejemplo) y queremos calcualr su área, debemos modificar AreaCalculator para tener en cuenta la nueva forma

interface Shape {
    public function area();
}

class Rectangle2 implements Shape {
    private $width;
    private $height;

    public function __construct($width, $height) {
        $this->width = $width;
        $this->height = $height;
    }

    public function area() {
        return $this->width * $this->height;
    }
}

class Circle2 implements Shape {
    private $radius;

    public function __construct($radius) {
        $this->radius = $radius;
    }

    public function area() {
        return pi() * $this->radius * $this->radius;
    }
}

class AreaCalculator2 {
    public function calculate($shapes) {
        
        foreach ($shapes as $shape) {
            echo "\nEl área de la forma es: ". $shape->area();
        }
    }
}

$shapes = [
    new Rectangle2(5, 10),
    new Circle2(7)
];

echo "\nEjercicio básico (cumpliendo OCP)";
$calculator = new AreaCalculator2();
echo $calculator->calculate($shapes);

// Con este enfoque, la clase Triangle tendría su propia definición de como calcular el área y AreaCalculator2 no se tendría que modificar

// Ejercicio Extra

interface Operation {
    public function calculate ($a, $b);
}

class Sum implements Operation {
    public function calculate($a, $b) {
        return $a + $b;
    }
}

class Substract implements Operation {
    public function calculate($a, $b) {
        return $a - $b;
    }
}

class Multiply implements Operation {
    public function calculate($a, $b) {
        return $a * $b;
    }
}

class Divition implements Operation{
    public function calculate($a, $b) {
        return $a / $b;
    }
}

class Calculator {
    public function calculate($operation, $a, $b) {
        return $operation->calculate($a, $b);
    }
}

$calculator = new Calculator();
echo "\nEjercicio extra";
echo "\nLa suma de 5 y 10 es: ". $calculator->calculate(new Sum(), 5, 10);
echo "\nLa resta de 5 y 10 es: ". $calculator->calculate(new Substract(), 5, 10);
echo "\nLa multiplicación de 5 y 10 es: ". $calculator->calculate(new Multiply(), 5, 10);
echo "\nLa división de 5 y 10 es: ". $calculator->calculate(new Divition(), 5, 10);

// A continuación vamos a añadir la operación potencia.

class Power implements Operation {
    public function calculate($a, $b) {
        return pow($a, $b);
    }
}

echo "\nLa potencia de 5 y 10 es: ". $calculator->calculate(new Power(), 5, 10);

// Como vemos, no hemos tenido que modificar nada en la clase Calculator