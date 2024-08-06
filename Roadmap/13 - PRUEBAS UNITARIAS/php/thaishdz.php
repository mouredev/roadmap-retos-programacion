<?php

/*
    * Esta es solo la parte EXTRA, la hice como si se tratase de testear 
    * los datos de un estudiante.
    *Student.php y StudentTest.php son dos ficheros independientes.
*/


// Student.php -----------------------------------------------------------------

namespace App;


class Student
{
    private $studentData; 

    public function __construct()
    {
        $this->studentData = [
            "name" => "Benedicto el Sabio",
            "age"  => 24,
            "birth_date" => new \DateTime("2000-11-10"),
            "programming_languages" => ["php", "python", "javascript"]
        ];
    }

    public function studentData() : array 
    {
        return $this->studentData;
    }
}

// StudentTest.php -----------------------------------------------------------------

use PHPUnit\Framework\TestCase;
use App\Student;


class StudentTest extends TestCase
{
    protected $student;

    protected function setUp(): void
    {
        $this->student = new Student();
    }

    public function testStudentDataFieldsExist()
    {
        $this->assertArrayHasKey("name", $this->student->studentData());
        $this->assertArrayHasKey("age", $this->student->studentData());
        $this->assertArrayHasKey("birth_date", $this->student->studentData());
        $this->assertArrayHasKey("programming_languages", $this->student->studentData());
    }

    // 2 ways of defining an assertion

    function testStudentDataIsCorrect() 
    {
        self::assertIsString($this->student->studentData()["name"]);
        self::assertIsInt($this->student->studentData()["age"]);
        self::assertInstanceOf(\DateTime::class, $this->student->studentData()["birth_date"]);
        self::assertIsArray($this->student->studentData()["programming_languages"]);
    }
    
}