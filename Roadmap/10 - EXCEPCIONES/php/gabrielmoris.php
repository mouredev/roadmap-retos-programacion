<?php
/*
* EXERCISE:
* Explore the concept of exception handling according to your language.
* Force an error in your code, capture the error, print the error
* and prevent the program from stopping unexpectedly.
* Try dividing "10/0" or accessing a non-existent index
* of a list to try to cause an error.
*/

// I can Customice my error:
class CustomException extends Exception
{
    public function errorMessage()
    {
        //error message
        $errorMsg = 'What happened here?? It seems that in line ' . $this->getLine() . ' in the file ' . $this->getFile()
            . ': <b>' . $this->getMessage() . '</b> is not a valid E-Mail address' . "\n";
        return $errorMsg;
    }
}


$email = "someone@example...com\n";

try {
    //check if
    if (filter_var($email, FILTER_VALIDATE_EMAIL) === FALSE) {
        //throw exception if email is not valid
        throw new CustomException($email);
    }
} catch (CustomException $e) {
    //display custom message
    echo $e->errorMessage();
}

function divide($numerator, $denominator)
{
    if ($denominator == 0) {
        throw new Exception("An error occurred: Division by zero is not allowed.\n");
    }
    return $numerator / $denominator;
}

try {
    $infinite = divide(10, 0);
} catch (Exception $e) {
    $errorMessage = $e->getMessage();
    echo $errorMessage;
} finally {
    // Code to be executed regardless of an exception
    echo "This code will always be executed.\n";
}


/* EXTRA DIFFICULTY (optional):
* Create a function that can process parameters, but also
* can throw 3 different types of exceptions (one of them has to
* correspond to a custom exception type created by us
* manually) in case of an error.
* Capture all exceptions from where you call the function.
* Print the type of error.
* Print if no error has occurred.
* Print that execution has finished.
*/

function error_processor($param1, $param2)
{

    if (!is_numeric($param1) || !is_numeric($param2)) {
        throw new InvalidArgumentException(("OOOOPS!\n"));
    }

    if ($param1 === $param2) {
        throw new CustomException(("Vaya vaya!\n"));
    }

    if ($param1 == 0 || $param2 == 0) {
        throw new OutOfRangeException("Parameters cant be 0.\n");
    }

    return $param1 / $param2;
}

try {
    error_processor(1, 2);
    error_processor(2, 2);
} catch (InvalidArgumentException $e) {
    echo "InvalidArgumentException: " . $e->getMessage() . "\n";
} catch (CustomException $e) {
    echo "CustomException: " . $e->getMessage() . "\n";
} catch (OutOfRangeException $e) {
    echo "OutOfRangeException: " . $e->getMessage() . "\n";
} finally {
    echo "Execution has finished.\n";
}

try {
    error_processor(0, 2);
} catch (InvalidArgumentException $e) {
    echo "InvalidArgumentException: " . $e->getMessage() . "\n";
} catch (CustomException $e) {
    echo "CustomException: " . $e->getMessage() . "\n";
} catch (OutOfRangeException $e) {
    echo "OutOfRangeException: " . $e->getMessage() . "\n";
} finally {
    echo "Execution has finished.\n";
}
