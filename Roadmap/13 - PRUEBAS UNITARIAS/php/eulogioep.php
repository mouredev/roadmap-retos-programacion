<?php

/**
 * Función que suma dos números y retorna el resultado.
 * @param int|float $a Primer número a sumar.
 * @param int|float $b Segundo número a sumar.
 * @return int|float La suma de a y b.
 */
function suma($a, $b) {
    return $a + $b;
}

/**
 * Crea y retorna un array asociativo con datos personales.
 * @return array Array asociativo con datos personales.
 */
function crearArrayAsociativo() {
    return [
        "name" => "Tu nombre",
        "age" => 30,
        "birth_date" => "1993-01-01",
        "programming_languages" => ["PHP", "JavaScript", "Python"]
    ];
}

// Incluimos PHPUnit para las pruebas
use PHPUnit\Framework\TestCase;

/**
 * Clase de pruebas unitarias para las funciones suma y crearArrayAsociativo.
 */
class PruebasUnitarias extends TestCase
{
    /**
     * Prueba la función suma con varios casos.
     */
    public function testSuma()
    {
        $this->assertEquals(5, suma(2, 3), "La suma de 2 y 3 debería ser 5");
        $this->assertEquals(0, suma(-1, 1), "La suma de -1 y 1 debería ser 0");
        $this->assertEquals(-5, suma(-2, -3), "La suma de -2 y -3 debería ser -5");
    }

    /**
     * Prueba la existencia de todas las claves en el array asociativo.
     */
    public function testExistenciaClaves()
    {
        $array = crearArrayAsociativo();
        $this->assertArrayHasKey('name', $array, "El array debe contener la clave 'name'");
        $this->assertArrayHasKey('age', $array, "El array debe contener la clave 'age'");
        $this->assertArrayHasKey('birth_date', $array, "El array debe contener la clave 'birth_date'");
        $this->assertArrayHasKey('programming_languages', $array, "El array debe contener la clave 'programming_languages'");
    }

    /**
     * Prueba que los datos en el array asociativo son correctos.
     */
    public function testDatosCorrectos()
    {
        $array = crearArrayAsociativo();
        $this->assertEquals("Tu nombre", $array['name'], "El nombre debe ser 'Tu nombre'");
        $this->assertIsInt($array['age'], "La edad debe ser un entero");
        $this->assertMatchesRegularExpression('/^\d{4}-\d{2}-\d{2}$/', $array['birth_date'], "La fecha de nacimiento debe tener el formato YYYY-MM-DD");
        $this->assertIsArray($array['programming_languages'], "Los lenguajes de programación deben ser un array");
        $this->assertNotEmpty($array['programming_languages'], "La lista de lenguajes de programación no debe estar vacía");
    }
}

?>