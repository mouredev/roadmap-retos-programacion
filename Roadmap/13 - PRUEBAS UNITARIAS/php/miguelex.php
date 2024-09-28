<?php 

function sumar($a, $b){
    return $a + $b;
}

global $dict;

$dict = [
    "name" => "Miguel",
    "age" => 48,
    "birth_date" => "1975-09-03",
    "programming_languages" => ["Python", "PHP", "JavaScript"]
];

?>

<?php 
require_once 'miguelex.php';


// Tests - Deben ir en u nfichero aparte de nombre miguelexTest.php

use PHPUnit\Framework\TestCase;

class MiguelexTest extends TestCase {
    public function testSum() {
        $this->assertEquals(4, sumar(2, 2));
        $this->assertEquals(10, sumar(5, 5));
    }

    public function testDictionaryFields() {
        global $dict;

        $this->assertArrayHasKey('name', $dict);
        $this->assertArrayHasKey('age', $dict);
        $this->assertArrayHasKey('birth_date', $dict);
        $this->assertArrayHasKey('programming_languages', $dict);
    }

    public function testDictionaryValues() {
        global $dict;

        $this->assertIsString($dict['name']);
        $this->assertIsInt($dict['age']);
        $this->assertMatchesRegularExpression('/^\d{4}-\d{2}-\d{2}$/', $dict['birth_date']);
        $this->assertIsArray($dict['programming_languages']);
    }
}