<?php

// This is a single line comment: https://www.php.net/manual/en/

/*this 
is 
a 
multiline 
comment 
*/

// Variables
$variable ="I am a siple basic variable."
// Constants

define("constant", "I am inmutable.");

// Strings
$var = 'String';
$multilineString ='This
is
a
multiline
string';

// Null
$nullType = NULL;

// Boolean
$bool = True;

// Numbers
$decimal = 1234;
$octals = 0123;
$hechadecimal =0x1A;
$binary = 0b11111111;

// Floats
$fl= 3.141632;

// Arrays
$arr =array(
    "key"  => "value",
    "key2" => "value2",
    "key3" => "value3",
);

$arr2 = [
    "key"  => "value",
    "key2" => "value2",
    "key3" => "value3",
];

// Objects
class obj 
{
    function do_sth()
    {
        echo "Hello, Php";
    }
};

$object = new obj;

$object->do_sth();

?>