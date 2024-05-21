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
    public function expects($callback, $result)
    {
        return $callback() === $result;
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
    }
    public function assertFalse($condition, $message = '')
    {
    }
    public function assertNull($value, $message = '')
    {
    }
}


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