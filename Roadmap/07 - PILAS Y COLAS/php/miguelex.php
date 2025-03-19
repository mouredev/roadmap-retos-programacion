<?php

// La implementacion la vamos a hacer con array y usando POO
class Cola {
    private $cola = array();
    private $inicio = 0;
    private $fin = 0;
    private $max = 10; // Esto es opcional para limitar el tamaño de la cola. Se puede omitir refactorizando el código. alli donde haga falta

    public function encolar($elemento) {
        if ($this->fin < $this->max) {
            $this->cola[$this->fin] = $elemento;
            $this->fin++;
        } else {
            echo "La cola está llena";
        }
    }

    public function desencolar() {
        if ($this->inicio < $this->fin) {
            $elemento = $this->cola[$this->inicio];
            unset($this->cola[$this->inicio]);
            $this->inicio++;
            return $elemento;
        } else {
            echo "La cola está vacía\n";
        }
    }

    public function mostrar() {
        if ($this->inicio == $this->fin) {
            echo "La cola está vacía\n";
            
        } else {
            for ($i = $this->inicio; $i < $this->fin; $i++) {
                echo $this->cola[$i] . " ";
            }
        }        
    }
}

class Pila {
    private $pila = array();
    private $tope = 0;
    private $max = 7; // Esto es opcional para limitar el tamaño de la pila. Se puede omitir refactorizando el código. alli donde haga falta

    public function getTope(){
        // Esta es una función creada expresamente para el ejercicio extra. No seria necesaria para el funcionamiento de la pila
        return $this->tope;
    }

    public function apilar($elemento) {
        if ($this->tope < $this->max) {
            $this->pila[$this->tope] = $elemento;
            $this->tope++;
        } else {
            echo "La pila está llena\n";
        }
    }

    public function desapilar() {
        if ($this->tope > 0) {
            $this->tope--;
            $elemento = $this->pila[$this->tope];
            unset($this->pila[$this->tope]);
            return $elemento;
        } else {
            echo "La pila está vacía\n";
        }
    }

    public function mostrar() {
        if ($this->tope == 0) {
            echo "La pila está vacía\n";
        } else {
            for ($i = $this->tope - 1; $i >= 0; $i--) {
                echo $this->pila[$i] . " ";
            }
        }        
    }

    public function getPosition($i){
        // Esta es una función creada expresamente para el ejercicio extra. No seria necesaria para el funcionamiento de la pila
        return $this->pila[$i];
    }
}

$cola = new Cola();
$pila = new Pila();

echo "Vamos a trabajar con la cola\n";
echo "Vamos a mostrar el contenido de la cola al inicio de la misma: \n";
$cola->mostrar();
echo "\n";

echo "Vamos a encolar 3 elementos: 1, 2 y 3\n";
$cola->encolar(1);
$cola->encolar(2);
$cola->encolar(3);

echo "Vamos a mostrar el contenido de la cola después de encolar 3 elementos: \n";
$cola->mostrar();
echo "\n";

echo "Vamos a desencolar un elemento\n";
$cola->desencolar();

echo "Vamos a mostrar el contenido de la cola después de desencolar un elemento: \n";
$cola->mostrar();
echo "\n";

echo "Vamos a encolar 2 elementos: 4 y 5 y vamos a desencolar dos\n";
$cola->encolar(4);
$cola->encolar(5);
$cola->desencolar();
$cola->desencolar();

echo "Vamos a mostrar el contenido de la cola después de encolar 2 elementos y desencolar dos: \n";
$cola->mostrar();
echo "\n";

echo "Por ultimo, vamos a desencolar tres elemento (recuerda que realemnte solo nos quedan 2 dentro de la cola)\n";
$cola->desencolar();
$cola->desencolar();
$cola->desencolar();

echo "Vamos a mostrar el contenido de la cola después de desencolar tres elementos: \n";
$cola->mostrar();
echo "\n";

echo "Ahora, vamos a trabajar con la pila\n";

echo "Vamos a mostrar el contenido de la pila al inicio de la misma: \n";

$pila->mostrar();
echo "\n";

echo "Vamos a apilar 3 elementos: 1, 2 y 3\n";

$pila->apilar(1);
$pila->apilar(2);
$pila->apilar(3);

echo "Vamos a mostrar el contenido de la pila después de apilar 3 elementos: \n";
$pila->mostrar();
echo "\n";

echo "Vamos a desapilar un elemento\n";
$pila->desapilar();

echo "Vamos a mostrar el contenido de la pila después de desapilar un elemento: \n";
$pila->mostrar();
echo "\n";

echo "Vamos a apilar 2 elementos: 4 y 5 y vamos a desapilar dos\n";

$pila->apilar(4);
$pila->apilar(5);

$pila->desapilar();
$pila->desapilar();

echo "Vamos a mostrar el contenido de la pila después de apilar 2 elementos y desapilar dos: \n";

$pila->mostrar();
echo "\n";

echo "Por ultimo, vamos a desapilar tres elemento (recuerda que realemnte solo nos quedan 2 dentro de la pila)\n";

$pila->desapilar();
$pila->desapilar();
$pila->desapilar();

echo "Vamos a mostrar el contenido de la pila después de desapilar tres elementos: \n";
$pila->mostrar();
echo "\n";

echo "Vamos a simular el mecanismo adelante/atrás de un navegador web\n";

$pila = new Pila();

$ultimoIndexVisitado = -1; 

do {
    $cabeza = $pila->getTope() - 1;

    echo "Escribe el nombre de la web, adelante, atras o exit: ";
    $entrada = trim(fgets(STDIN));
    if ($entrada == "adelante") {
        if ($ultimoIndexVisitado < $cabeza) { 
            $ultimoIndexVisitado++;
            echo "Navegando adelante a la web: ". $pila->getPosition($ultimoIndexVisitado). "\n";
        } else {
            echo "No hay más webs para navegar adelante\n";
        }
    } elseif ($entrada == "atras") {
        if ($ultimoIndexVisitado > 0) { 
            $ultimoIndexVisitado--;
            echo "Navegando atrás a la web:". $pila->getPosition($ultimoIndexVisitado). "\n";            
        } else {
            echo "No hay más webs para navegar atrás\n";
        }
    } elseif ($entrada != "exit") {
        $pila->apilar($entrada);
        $ultimoIndexVisitado = $pila->getTope() - 1; 
        echo "Estas en la web: $entrada\n";
    }
} while ($entrada != "exit");

echo "Vamos a simular el mecanismo de una cola de impresion\n";

$cola = new Cola();

do {
    echo "Escribe el nombre del documento, imprimir o exit: ";
    $entrada = trim(fgets(STDIN));
    if ($entrada == "imprimir") {
        $documento = $cola->desencolar();
        if ($documento != null) {
            echo "Imprimiendo documento: $documento\n";
        } else {
            echo "No hay documentos para imprimir\n";
        }
    } elseif ($entrada != "exit") {
        $cola->encolar($entrada);
        echo "Documento encolado: $entrada\n";
    }
} while ($entrada != "exit");

