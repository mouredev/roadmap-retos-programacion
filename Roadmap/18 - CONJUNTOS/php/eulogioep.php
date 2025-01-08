<?php
/**
 * TEORÍA: Conjuntos en PHP
 * 
 * En PHP, no existe una estructura de datos específica para conjuntos como en otros lenguajes.
 * Sin embargo, podemos simular conjuntos usando arrays y algunas funciones específicas:
 * 
 * 1. array_unique() - Para eliminar duplicados
 * 2. array_values() - Para reindexar arrays después de operaciones
 * 3. array_intersect() - Para intersección
 * 4. array_diff() - Para diferencia
 * 5. array_merge() - Para unión
 * 
 * También usaremos la clase SplObjectStorage para demostrar una implementación
 * más orientada a objetos cuando sea necesario.
 */

class ConjuntosEjemplo {
    private $conjunto;

    public function __construct() {
        $this->conjunto = [];
    }

    /**
     * Muestra el contenido actual del conjunto
     */
    public function mostrarConjunto($mensaje = "Conjunto actual") {
        echo "$mensaje: [" . implode(", ", $this->conjunto) . "]\n";
    }

    /**
     * 1. Añade un elemento al final
     */
    public function agregarAlFinal($elemento) {
        $this->conjunto[] = $elemento;
        $this->conjunto = array_values(array_unique($this->conjunto));
        $this->mostrarConjunto("Después de añadir '$elemento' al final");
    }

    /**
     * 2. Añade un elemento al principio
     */
    public function agregarAlPrincipio($elemento) {
        array_unshift($this->conjunto, $elemento);
        $this->conjunto = array_values(array_unique($this->conjunto));
        $this->mostrarConjunto("Después de añadir '$elemento' al principio");
    }

    /**
     * 3. Añade varios elementos en bloque al final
     */
    public function agregarVariosAlFinal($elementos) {
        $this->conjunto = array_values(array_unique(array_merge($this->conjunto, $elementos)));
        $this->mostrarConjunto("Después de añadir varios elementos al final");
    }

    /**
     * 4. Añade varios elementos en bloque en una posición concreta
     */
    public function agregarVariosEnPosicion($elementos, $posicion) {
        $primera_parte = array_slice($this->conjunto, 0, $posicion);
        $segunda_parte = array_slice($this->conjunto, $posicion);
        $this->conjunto = array_values(array_unique(array_merge($primera_parte, $elementos, $segunda_parte)));
        $this->mostrarConjunto("Después de añadir varios elementos en posición $posicion");
    }

    /**
     * 5. Elimina un elemento en una posición concreta
     */
    public function eliminarEnPosicion($posicion) {
        if (isset($this->conjunto[$posicion])) {
            $elemento = $this->conjunto[$posicion];
            unset($this->conjunto[$posicion]);
            $this->conjunto = array_values($this->conjunto);
            $this->mostrarConjunto("Después de eliminar elemento en posición $posicion");
        }
    }

    /**
     * 6. Actualiza el valor de un elemento en una posición concreta
     */
    public function actualizarEnPosicion($posicion, $nuevoValor) {
        if (isset($this->conjunto[$posicion])) {
            $this->conjunto[$posicion] = $nuevoValor;
            $this->conjunto = array_values(array_unique($this->conjunto));
            $this->mostrarConjunto("Después de actualizar elemento en posición $posicion");
        }
    }

    /**
     * 7. Comprueba si un elemento está en el conjunto
     */
    public function contiene($elemento) {
        $resultado = in_array($elemento, $this->conjunto);
        echo "¿El conjunto contiene '$elemento'? " . ($resultado ? "Sí" : "No") . "\n";
        return $resultado;
    }

    /**
     * 8. Elimina todo el contenido del conjunto
     */
    public function limpiar() {
        $this->conjunto = [];
        $this->mostrarConjunto("Después de limpiar el conjunto");
    }

    /**
     * Obtiene el conjunto actual
     */
    public function obtenerConjunto() {
        return $this->conjunto;
    }
}

/**
 * Clase para operaciones extra con conjuntos
 */
class OperacionesExtra {
    /**
     * Unión de dos conjuntos
     */
    public static function union($conjunto1, $conjunto2) {
        return array_values(array_unique(array_merge($conjunto1, $conjunto2)));
    }

    /**
     * Intersección de dos conjuntos
     */
    public static function interseccion($conjunto1, $conjunto2) {
        return array_values(array_intersect($conjunto1, $conjunto2));
    }

    /**
     * Diferencia de dos conjuntos
     */
    public static function diferencia($conjunto1, $conjunto2) {
        return array_values(array_diff($conjunto1, $conjunto2));
    }

    /**
     * Diferencia simétrica de dos conjuntos
     */
    public static function diferenciaSimetrica($conjunto1, $conjunto2) {
        $diff1 = array_diff($conjunto1, $conjunto2);
        $diff2 = array_diff($conjunto2, $conjunto1);
        return array_values(array_merge($diff1, $diff2));
    }
}

// Demostración de uso
echo "PARTE 1: OPERACIONES BÁSICAS\n";
$demo = new ConjuntosEjemplo();

$demo->agregarAlFinal("Elemento1");
$demo->agregarAlPrincipio("Elemento2");
$demo->agregarVariosAlFinal(["Elemento3", "Elemento4", "Elemento5"]);
$demo->agregarVariosEnPosicion(["ElementoA", "ElementoB"], 2);
$demo->eliminarEnPosicion(3);
$demo->actualizarEnPosicion(1, "ElementoActualizado");
$demo->contiene("Elemento1");
$demo->limpiar();

echo "\nPARTE 2: OPERACIONES EXTRA\n";
$conjunto1 = [1, 2, 3, 4, 5];
$conjunto2 = [4, 5, 6, 7, 8];

echo "Conjunto 1: [" . implode(", ", $conjunto1) . "]\n";
echo "Conjunto 2: [" . implode(", ", $conjunto2) . "]\n";

$union = OperacionesExtra::union($conjunto1, $conjunto2);
echo "Unión: [" . implode(", ", $union) . "]\n";

$interseccion = OperacionesExtra::interseccion($conjunto1, $conjunto2);
echo "Intersección: [" . implode(", ", $interseccion) . "]\n";

$diferencia = OperacionesExtra::diferencia($conjunto1, $conjunto2);
echo "Diferencia (conjunto1 - conjunto2): [" . implode(", ", $diferencia) . "]\n";

$diferenciaSimetrica = OperacionesExtra::diferenciaSimetrica($conjunto1, $conjunto2);
echo "Diferencia simétrica: [" . implode(", ", $diferenciaSimetrica) . "]\n";
?>