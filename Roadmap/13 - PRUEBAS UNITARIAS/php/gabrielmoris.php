<?php
/*
* EXERCISE:
* Create a function that is responsible for adding two numbers and returning
* its result.
* Create a test, using the tools of your language, that is
* able to determine if that function is executing correctly.
*/

// There are several libraries available for unit testing. I will create my own Tests.
function sum($num1, $num2)
{

    // I mock an error
    if ($num1 > 5) {
        $num1 = $num1 + 10;
    }

    return $num1 + $num2;
}

class Test
{
    public function expects($callback, $result, $message = "", ...$args)
    {
        if (is_string($callback)) {
            $callback = function (...$args) use ($callback) {
                return $callback(...$args);
            };
        }

        $actualResult = $callback(...$args);

        if (empty($message)) {
            return $actualResult === $result;
        }

        if ($actualResult !== $result) {
            return $message;
        }
    }

    public function assertEquals($val1, $val2, $message = "")
    {
        if (empty($message)) {
            return $val1 === $val2;
        }

        if ($val1 !== $val2) {
            return $message;
        }
    }

    public function assertNotEquals($val1, $val2, $message = "")
    {
        if (empty($message)) {
            return $val1 !== $val2;
        }

        if ($val1 === $val2) {
            return $message;
        }
    }

    public function assertFalse($condition, $message = '')
    {
        if (empty($message)) {
            return $condition === false;
        }

        if ($condition !== false) {
            return $message;
        }
    }

    public function assertNull($value, $message = '')
    {
        if (empty($message)) {
            return $value === null;
        }

        if ($value !== null) {
            return $message;
        }
    }

    public function has_all_keys($object, $keys)
    {
        foreach ($keys as $key) {
            if (!property_exists($object, $key)) {
                echo "Property " . $key . " is not in this Object\n";
                return false;
            }
        }

        return true;
    }
}

$test = new Test();
$result = $test->expects('sum', 7, '', 3, 4);
var_dump($result);
$result = $test->expects('sum', 9, '', 6, 3);
echo $result ? 'Test Case 2 Passed' : 'Test Case 2 Failed';
echo "\n";



/* 
* EXTRA DIFFICULTY (optional):
* Create a dictionary with the following keys and values:
* "name": "Your name"
* "age": "Your age"
* "birth_date": "Your date of birth"
* "programming_languages": ["List of programming languages"]
* Create two tests:
* A first one that determines that all fields exist.
* A second one that determines that the data entered is correct.
*/

$dictionary = (object) ["name" => "Gabrielmoris", "age" => 34, "birthday" => "15.18.1986", "programming_languages" => ["Javascript", "Typescript", "PHP", "Rust"]];

echo $test->has_all_keys($dictionary, ["name", "age", "birthday", "programming_languages"]) ?  "It has all properties\n" :  "Error\n";
echo $test->has_all_keys($dictionary, ["failure"]) ?  "It has all properties\n" :  "Error\n";

echo $test->assertEquals($dictionary->name, "Gabrielmoris") ? "Name correct\n" : "Not my name\n";
echo $test->assertEquals($dictionary->age, 34) ? "Age correct\n" : "Not my age\n";
echo $test->assertEquals($dictionary->birthday, "15.18.1986") ? "Birthday correct\n" : "Not my birthday\n";
echo $test->assertEquals($dictionary->programming_languages, ["Javascript", "Typescript", "PHP", "Rust"]) ? "Programming languages correct\n" : "Not my Programming languages\n";
